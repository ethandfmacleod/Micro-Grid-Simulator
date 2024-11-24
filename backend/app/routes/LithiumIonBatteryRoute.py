
from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.routes import crud
from app.models.LithiumIonBattery import *

lithium_ion_router = APIRouter(
    prefix="/models/lithium_ions",
    tags=["LithiumIonBattery"]
)

@lithium_ion_router.get("/", response_model=List[LithiumIonBatterySchema])
def read_lithium_ions(db: Session = Depends(get_db)):
    lithium_ions = crud.get_all(db, LithiumIonBattery)
    return lithium_ions

@lithium_ion_router.get("/{id}", response_model=LithiumIonBatterySchema)
def read_lithium_ion(id: int, db: Session = Depends(get_db)):
    lithium_ion = crud.get_by_id(db, LithiumIonBattery, id)
    if not lithium_ion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="LithiumIonBattery not found")
    return lithium_ion

@lithium_ion_router.post("/", response_model=LithiumIonBatterySchema, status_code=status.HTTP_201_CREATED)
def create_lithium_ion(lithium_ion: LithiumIonBatteryCreate = {}, db: Session = Depends(get_db)):
    return crud.create(db, LithiumIonBattery, lithium_ion)

@lithium_ion_router.put("/{id}", response_model=LithiumIonBatterySchema)
def update_lithium_ion(id: int, lithium_ion_update: LithiumIonBatteryUpdate, db: Session = Depends(get_db)):
    updated_lithium_ion = crud.update(db, LithiumIonBattery, id, lithium_ion_update)
    if not updated_lithium_ion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="LithiumIonBattery not found")
    return updated_lithium_ion

@lithium_ion_router.delete("/{id}", response_model=LithiumIonBatterySchema)
def delete_lithium_ion(id: int, db: Session = Depends(get_db)):
    deleted_lithium_ion = crud.delete(db, LithiumIonBattery, id)
    if not deleted_lithium_ion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="LithiumIonBattery not found")
    return deleted_lithium_ion