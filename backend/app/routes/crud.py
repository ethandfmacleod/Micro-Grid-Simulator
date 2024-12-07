from typing import List, Optional, Type, TypeVar
from sqlalchemy import desc
from sqlalchemy.orm import Session

T = TypeVar("T")  # Generic type for the model

# Generic get all objects
def get_all(db: Session, model: Type[T]) -> List[T]:
    return db.query(model).order_by(desc(model.id)).all()

# Generic get an object
def get_by_id(db: Session, model: Type[T], id: int) -> Optional[T]:
    return db.query(model).filter(model.id == id).first()

# Generic create an object
def create(db: Session, model: Type[T], item: dict) -> T:
    db_item = model(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Generic update an object
def update(db: Session, model: Type[T], id: int, item_update: dict) -> Optional[T]:
    db_item = db.query(model).filter(model.id == id).first()
    if not db_item:
        return None
    for key, value in item_update.dict(exclude_unset=True).items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

# Generic delete an object
def delete(db: Session, model: Type[T], id: int) -> Optional[T]:
    db_item = db.query(model).filter(model.id == id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item