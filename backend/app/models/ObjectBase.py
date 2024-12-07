from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, declared_attr, relationship
from app.database import Base

# DB Model
class ObjectBase(Base):
    __abstract__ = True

    @declared_attr
    def id(cls) -> Mapped[int]:
        return mapped_column(primary_key=True)

    @declared_attr
    def project_id(cls) -> Mapped[int]:
        return mapped_column(ForeignKey("Projects.id"))

    # @declared_attr
    # def project(cls) -> Mapped["Project"]: # type: ignore
    #     return relationship("Project", back_populates="related_items")