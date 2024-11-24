from typing import Optional
from sqlalchemy import Integer, Float
from sqlalchemy.orm import Mapped, mapped_column
from app.enums.ModelEnums import EnergyInType
from pydantic import BaseModel, ConfigDict
from app.models.ObjectBase import ObjectBase

# DB Model
class EnergyIn(ObjectBase):
    __tablename__ = "EnergyIns"

    id: Mapped[int] = mapped_column(primary_key=True)
    watts: Mapped[int] = mapped_column(Integer, default=0)
    price: Mapped[float] = mapped_column(Float, default=0)
    daily_emissions: Mapped[int] = mapped_column(Integer, default=0)
    type: Mapped[EnergyInType]

    __mapper_args__ = {
        'polymorphic_identity': EnergyInType.Default,
        'polymorphic_on': 'type',
        'with_polymorphic': '*'
    }

# Base class for schemas
class EnergyInBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    watts: int
    price: float
    daily_emissions: int
    type: EnergyInType

# Create Schema - Same as Base
class EnergyInCreate(EnergyInBase):
    pass

# Update/Patch Schema
class EnergyInUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    watts: Optional[int]
    price: Optional[float]
    daily_emissions: Optional[int]

# Get/Delete Operation Schema
class EnergyInSchema(EnergyInBase):
    id: int
