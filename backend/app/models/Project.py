from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from pydantic import BaseModel, ConfigDict, Field
from app.models.ObjectBase import ObjectBase
from datetime import datetime
from sqlalchemy import DateTime

# DB Model
class Project(Base):
    __tablename__ = "Projects"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, default="New Project", nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    description: Mapped[str] = mapped_column(String, default="No Description Provided", nullable=False)
    
    # related_items: Mapped[list[ObjectBase]] = relationship(
    #     "ObjectBase",
    #     back_populates="project",
    #     cascade="all, delete-orphan",
    # )


# Base class for schemas
class ProjectBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)    
    name: str = Field(default="New Project")
    description: str = Field(default="No Description Provided")
    created_at: datetime = Field(default_factory=datetime.utcnow)

# Create Schema - Same as Base
class ProjectCreate(ProjectBase):
    pass

# Update/Patch Schema
class ProjectUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: Optional[str]
    description: Optional[str] = None

# Get/Delete Operation Schema
class ProjectSchema(ProjectBase):
    id: int
