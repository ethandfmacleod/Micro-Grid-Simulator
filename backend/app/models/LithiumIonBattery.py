from typing import Optional
from sqlalchemy import ForeignKey, Integer, Float, String
from sqlalchemy.orm import Mapped, mapped_column
from app.enums.ModelEnums import EnergyStorageType
from pydantic import BaseModel, ConfigDict
from app.models import EnergyStorageUnit

# DB Model
class LithiumIonBattery(EnergyStorageUnit):
    __tablename__ = "LithiumIonBatteries"

    id: Mapped[int] = mapped_column(ForeignKey("EnergyStorageUnits.id"), primary_key=True)
    max_charge_rate: Mapped[float] = mapped_column(Float, default=0)
    name: Mapped[str] = mapped_column(String, default="Lithium Ion Battery")
    efficiency: Mapped[float] = mapped_column(Float, default=0)
    current: Mapped[int] = mapped_column(Integer, default=0)
    voltage: Mapped[int] = mapped_column(Integer, default=0)



    __mapper_args__ = {
        'polymorphic_identity': EnergyStorageType.LithiumIon,
    }

# Base class for schemas
class LithiumIonBatteryBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    max_charge_rate: float
    name: str
    efficiency: float
    current: int
    voltage: int

# Create Schema - Same as Base
class LithiumIonBatteryCreate(LithiumIonBatteryBase):
    pass

# Update/Patch Schema
class LithiumIonBatteryUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    max_charge_rate: Optional[float]
    name: Optional[str]
    efficiency: Optional[float]
    current: Optional[int]
    voltage: Optional[int]

# Get/Delete Operation Schema
class LithiumIonBatterySchema(LithiumIonBatteryBase):
    id: int
