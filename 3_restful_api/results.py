from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from schemas import ProcessingResultRead, ProcessingResultCreate, ProcessingResultsDict, ProcessingResultUpdate
from models import ProcessingResult
from crud import create_processing_result, get_results, get_result_by_id, delete_result_by_id, update_result
from database import get_db


router_results = APIRouter()

@router_results.post("/results/")
def create_result(payload: ProcessingResultsDict, db: Session = Depends(get_db)):
    results = []
    for key, result in payload.root.items():
        processed_result = create_processing_result(db, result)
        results.append(processed_result)
    return {"message": "Processed successfully", "results": results}

@router_results.patch("/results/{result_id}")
def update_result(result_id: int, update_rs:ProcessingResultUpdate, db: Session = Depends(get_db)):
    return update_result(result_id, update_rs, db)

@router_results.get("/results/", response_model=List[ProcessingResultRead])
def read_results(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_results(db, skip=skip, limit=limit)

@router_results.get("/results/{result_id}", response_model=ProcessingResultRead)
def read_result_by_id(result_id: int, db: Session = Depends(get_db)):
    return get_result_by_id(result_id, db)

@router_results.delete("/results/{result_id}")
def delete_result_by_id(result_id: int, db: Session = Depends(get_db)):
    return delete_result_by_id(result_id, db)