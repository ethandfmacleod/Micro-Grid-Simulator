
from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.EnergyIn import *
from app.routes import crud

energy_in_router = APIRouter(
    prefix="/models/energy_ins",
    tags=["EnergyIn"]
)

@energy_in_router.get("/", response_model=List[EnergyInSchema])
def read_energy_ins(db: Session = Depends(get_db)):
    energy_ins = crud.get_all(db, EnergyIn)
    return energy_ins

@energy_in_router.get("/{id}", response_model=EnergyInSchema)
def read_energy_in(id: int, db: Session = Depends(get_db)):
    energy_in = crud.get_by_id(db, EnergyIn, id)
    if not energy_in:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EnergyIn not found")
    return energy_in

@energy_in_router.post("/", response_model=EnergyInSchema, status_code=status.HTTP_201_CREATED)
def create_energy_in(energy_in: EnergyInCreate = {}, db: Session = Depends(get_db)):
    return crud.create(db, EnergyIn, energy_in)

@energy_in_router.put("/{id}", response_model=EnergyInSchema)
def update_energy_in(id: int, energy_in_update: EnergyInUpdate = {}, db: Session = Depends(get_db)):
    updated_energy_in = crud.update(db, EnergyIn, id, energy_in_update)
    if not updated_energy_in:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EnergyIn not found")
    return updated_energy_in

@energy_in_router.delete("/{id}", response_model=EnergyInSchema)
def delete_energy_in(id: int, db: Session = Depends(get_db)):
    deleted_energy_in = crud.delete(db, EnergyIn, id)
    if not deleted_energy_in:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EnergyIn not found")
    return deleted_energy_in