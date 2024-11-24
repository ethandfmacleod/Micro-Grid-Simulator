
from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.EnergyStorageUnit import *
from app.routes import crud

energy_storage_router = APIRouter(
    prefix="/models/energy_storages",
    tags=["EnergyStorageUnit"]
)

@energy_storage_router.get("/", response_model=List[EnergyStorageUnitSchema])
def read_energy_storages(db: Session = Depends(get_db)):
    energy_storages = crud.get_all(db, EnergyStorageUnit)
    return energy_storages

@energy_storage_router.get("/{id}", response_model=EnergyStorageUnitSchema)
def read_energy_storage(id: int, db: Session = Depends(get_db)):
    energy_storage = crud.get_by_id(db, EnergyStorageUnit, id)
    if not energy_storage:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EnergyStorageUnit not found")
    return energy_storage

@energy_storage_router.post("/", response_model=EnergyStorageUnitSchema, status_code=status.HTTP_201_CREATED)
def create_energy_storage(energy_storage: EnergyStorageUnitCreate = {}, db: Session = Depends(get_db)):
    return crud.create(db, EnergyStorageUnit, energy_storage)

@energy_storage_router.put("/{id}", response_model=EnergyStorageUnitSchema)
def update_energy_storage(id: int, energy_storage_update: EnergyStorageUnitUpdate = {}, db: Session = Depends(get_db)):
    updated_energy_storage = crud.update(db, EnergyStorageUnit, id, energy_storage_update)
    if not updated_energy_storage:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EnergyStorageUnit not found")
    return updated_energy_storage

@energy_storage_router.delete("/{id}", response_model=EnergyStorageUnitSchema)
def delete_energy_storage(id: int, db: Session = Depends(get_db)):
    deleted_energy_storage = crud.delete(db, EnergyStorageUnit, id)
    if not deleted_energy_storage:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EnergyStorageUnit not found")
    return deleted_energy_storage