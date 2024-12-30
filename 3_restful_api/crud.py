from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
import schemas, utils, models

def create_element(element: schemas.ElementCreate, db: Session):
    element_to_create = element.dict()
    new_element = models.Device(
        device_name=element_to_create["device_name"]
    )
    db.add(new_element)
    db.commit()
    db.refresh(new_element)
    return {"response:": "Element created"}

def create_processing_result(db: Session, result: schemas.ProcessingResultCreate):
    normalized, avg_before, avg_after = utils.validate_and_normalize(result.data)

    device = db.query(models.Device).filter_by(device_name=result.device_name).first()
    if not device:
        device = models.Device(device_name=result.device_name)
        db.add(device)
        db.commit()
        db.refresh(device)

    new_result = models.ProcessingResult(
        device_id=device.id,
        data_size=len(normalized),
        average_before_normalization=avg_before,
        average_after_normalization=avg_after,
    )
    db.add(new_result)
    db.commit()
    db.refresh(new_result)
    return new_result

def update_result(id:int, update_result: schemas.ProcessingResultUpdate, db: Session):
    result = get_result_by_id(id, db)
    if not result:
        return {"response": "Result not found"}

    update_data = update_result.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(result, key, value)

    db.commit()
    db.refresh(result)
    return {"response": "Result updated"}


def get_results(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.ProcessingResult).offset(skip).limit(limit).all()

def get_result_by_id(id:int, db: Session):
    result = db.query(models.ProcessingResult).filter(models.ProcessingResult.id == id).first()
    return result

def delete_result_by_id(id:int, db: Session):
    result = get_result_by_id(id, db)
    if not result:
        return {"response": "Result not found"}
    db.delete(result)
    db.commit()
    return {"response": "Result deleted successfully"}
