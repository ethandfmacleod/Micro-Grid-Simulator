from typing import Optional
from sqlalchemy import Column, Integer, Float, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column
from app.models.EnergyIn import EnergyIn, EnergyInBase, EnergyInUpdate
from app.enums.ModelEnums import EnergyInType, SolarPanelMaterial, SolarPanelType
from pydantic import BaseModel, ConfigDict


class SolarPanel(EnergyIn):
    __tablename__ = "SolarPanels"
    
    id: Mapped[int] = mapped_column(ForeignKey("EnergyIns.id"), primary_key=True)
    panel_type: Mapped[SolarPanelType] = mapped_column(Enum(SolarPanelType), default=SolarPanelType.Default)
    width: Mapped[float] = mapped_column(Float, default=0)
    length: Mapped[float] = mapped_column(Float, default=0)
    cells: Mapped[int] = mapped_column(Integer, default=0)
    material: Mapped[SolarPanelMaterial] = mapped_column(Enum(SolarPanelMaterial), default=SolarPanelMaterial.Default)

    __mapper_args__ = {
        "polymorphic_identity": EnergyInType.SolarPanel,
    }

# Base class for schemas
class SolarPanelBase(EnergyInBase):
    model_config = ConfigDict(from_attributes=True)

    panel_type: SolarPanelType
    width: float
    length: float
    cells: int
    material: SolarPanelMaterial

# Create Schema - Same as Base
class SolarPanelCreate(SolarPanelBase):
    pass

# Update/Patch Schema
class SolarPanelUpdate(EnergyInUpdate):
    model_config = ConfigDict(from_attributes=True)

    panel_type: Optional[SolarPanelType]
    width: Optional[float]
    length: Optional[float]
    cells: Optional[int]
    material: Optional[SolarPanelMaterial]

# Get/Delete Operation Schema
class SolarPanelSchema(SolarPanelBase):
    id: int