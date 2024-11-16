from typing import Optional
from sqlalchemy import Column, Integer, Float, Enum
from app.enums.ModelEnums import EnergyInType
from pydantic import BaseModel, ConfigDict
from app.models.Base import Base

# DB Model
class EnergyIn(Base):
    __tablename__ = "EnergyIns"

    id = Column(Integer, primary_key=True, nullable=False)
    watts = Column(Integer, nullable=False, default=0)
    price = Column(Float, nullable=False, default=0)
    daily_emissions = Column(Integer, nullable=False, default=0)
    type = Column(Enum(EnergyInType), default=EnergyInType.Default)

    __mapper_args__ = {
        'polymorphic_identity': 'energyin',
        'polymorphic_on': 'type',
        'with_polymorphic': '*'
    }

# Base class for schemas
class EnergyInBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    watts: int
    price: float
    daily_emissions: int
    type: Optional[str]

# Create Schema - Same as Base
class EnergyInCreate(EnergyInBase):
    pass

# Update/Patch Schema
class EnergyInUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    watts: Optional[int]
    price: float
    daily_emissions: int
    type: Optional[str]

# Get/Delete Operation Schema
class EnergyInSchema(EnergyInBase):
    id: int
