from pydantic import BaseModel, RootModel, Field
from typing import List, Dict, Optional
from datetime import datetime

class ElementCreate(BaseModel):
    device_name: str

    class Config:
        from_attributes = True

class ElementRead(BaseModel):
    id: int
    device_name: str

class ProcessingResultCreate(BaseModel):
    id: str
    data: List[str]
    device_name: str = Field(alias="deviceName")

    class Config:
        from_attributes = True
        populate_by_name = True

class ProcessingResultsDict(RootModel[Dict[str, ProcessingResultCreate]]):
    pass

class ProcessingResultRead(BaseModel):
    id: int
    device_id: int
    data_size: int
    average_before_normalization: float
    average_after_normalization: float
    created_date: datetime
    updated_date: datetime

    class Config:
        from_attributes = True

class ProcessingResultUpdate(BaseModel):
    id: int = None
    device_id: int = None
    data_size: int = None
    average_before_normalization: float = None
    average_after_normalization: float = None
    created_date: datetime = None
    updated_date: datetime = None