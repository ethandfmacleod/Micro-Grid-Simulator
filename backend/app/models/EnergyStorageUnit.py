from typing import Optional
from sqlalchemy import Float
from sqlalchemy.orm import Mapped, mapped_column
from app.enums.ModelEnums import EnergyStorageType
from pydantic import BaseModel, ConfigDict
from app.models.ObjectBase import ObjectBase

# DB Model
class EnergyStorageUnit(ObjectBase):
    __tablename__ = "EnergyStorageUnits"

    capacity: Mapped[float] = mapped_column(Float, default=0)
    charge_level: Mapped[float] = mapped_column(Float, default=0)
    price: Mapped[float] = mapped_column(Float, default=0)
    type: Mapped[EnergyStorageType]

    __mapper_args__ = {
        'polymorphic_identity': EnergyStorageType.Default,
        'polymorphic_on': 'type',
        'with_polymorphic': '*'
    }

# Base class for schemas
class EnergyStorageUnitBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    capacity: float
    charge_level: float
    price: float
    type: EnergyStorageType

# Create Schema - Same as Base
class EnergyStorageUnitCreate(EnergyStorageUnitBase):
    pass

# Update/Patch Schema
class EnergyStorageUnitUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    capacity: Optional[float]
    charge_level: Optional[float]
    price: Optional[float]

# Get/Delete Operation Schema
class EnergyStorageUnitSchema(EnergyStorageUnitBase):
    id: int
