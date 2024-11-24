from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column, declared_attr
from app.models.Project import Project

class ProjectObjectMixin:
    @declared_attr
    def id(cls) -> Mapped[int]:
        return mapped_column(primary_key=True)

    @declared_attr
    def project_id(cls) -> Mapped[int]:
        return mapped_column(ForeignKey("Projects.id"))

    @declared_attr
    def project(cls) -> Mapped["Project"]:
        return relationship("Project", back_populates="related_items")