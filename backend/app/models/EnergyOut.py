from typing import Optional
from sqlalchemy import Column, Integer, Float, Enum
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
from app.enums.ModelEnums import EnergyOutType
from pydantic import BaseModel, ConfigDict

# DB Model
class EnergyOut(Base):
    __tablename__ = "EnergyOuts"

    id: Mapped[int] = mapped_column(primary_key=True)
    watts: Mapped[int] = mapped_column(Integer, default=0)
    daily_emissions: Mapped[int] = mapped_column(Integer, default=0)
    type: Mapped[EnergyOutType]

    __mapper_args__ = {
        'polymorphic_identity': EnergyOutType.Default,
        'polymorphic_on': 'type',
        'with_polymorphic': '*'
    }

# Base class for schemas
class EnergyOutBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    watts: int
    daily_emissions: int
    type: EnergyOutType

# Create Schema - Same as Base
class EnergyOutCreate(EnergyOutBase):
    pass

# Update/Patch Schema
class EnergyOutUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    watts: Optional[int]
    daily_emissions: Optional[int]

# Get/Delete Operation Schema
class EnergyOutSchema(EnergyOutBase):
    id: int
