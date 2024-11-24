from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from pydantic import BaseModel, ConfigDict
from app.models.ObjectBase import ObjectBase

# DB Model
class Project(Base):
    __tablename__ = "Projects"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, default="New Project")
    
    related_items: Mapped[list[ObjectBase]] = relationship(
        back_populates="project",
        cascade="all, delete-orphan",
    )


# Base class for schemas
class ProjectBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    name: str

# Create Schema - Same as Base
class ProjectCreate(ProjectBase):
    pass

# Update/Patch Schema
class ProjectUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: Optional[str]

# Get/Delete Operation Schema
class ProjectSchema(ProjectBase):
    id: int
