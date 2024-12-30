from sqlalchemy import ForeignKey, func, Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from database import Base

class Device(Base):
    __tablename__ = 'devices'
    id = Column(Integer, primary_key=True, index=True)
    device_name = Column(String, nullable=False)

    results = relationship("ProcessingResult", back_populates="device")


class ProcessingResult(Base):
    __tablename__ = 'processing_results'
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(Integer, ForeignKey('devices.id'), nullable=False, index=True)
    data_size = Column(Integer, nullable=False)
    average_before_normalization = Column(Float, nullable=False)
    average_after_normalization = Column(Float, nullable=False)
    created_date = Column(DateTime, default=func.now(), nullable=False)
    updated_date = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    device = relationship("Device", back_populates="results")