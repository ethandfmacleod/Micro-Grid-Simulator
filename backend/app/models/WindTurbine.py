from typing import Optional
from sqlalchemy import Integer, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from app.models.EnergyIn import EnergyIn, EnergyInBase, EnergyInUpdate
from app.enums.ModelEnums import EnergyInType
from pydantic import ConfigDict


class WindTurbine(EnergyIn):
    __tablename__ = "WindTurbines"
    
    id: Mapped[int] = mapped_column(ForeignKey("EnergyIns.id"), primary_key=True)
    name: Mapped[str] = mapped_column(String, default="Wind Turbine")
    rotor_diameter: Mapped[int] = mapped_column(Integer, default=0)
    rotation: Mapped[int] = mapped_column(Integer, default=0)
    cut_in_speed: Mapped[int] = mapped_column(Integer, default=0)
    rated_speed: Mapped[int] = mapped_column(Integer, default=0)
    cut_off_speed: Mapped[int] = mapped_column(Integer, default=0)

    __mapper_args__ = {
        "polymorphic_identity": EnergyInType.WindTurbine,
    }

# Base class for schemas
class WindTurbineBase(EnergyInBase):
    model_config = ConfigDict(from_attributes=True)

    name: str
    rotor_diameter: int
    rotation: int
    cut_in_speed: int
    rated_speed: int
    cut_off_speed: int

# Create Schema - Same as Base
class WindTurbineCreate(WindTurbineBase):
    pass

# Update/Patch Schema
class WindTurbineUpdate(EnergyInUpdate):
    model_config = ConfigDict(from_attributes=True)

    name: Optional[str]
    rotor_diameter: Optional[int]
    rotation: Optional[int]
    cut_in_speed: Optional[int]
    rated_speed: Optional[int]
    cut_off_speed: Optional[int]

# Get/Delete Operation Schema
class WindTurbineSchema(WindTurbineBase):
    id: int