
from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.EnergyOut import *
from app.routes import crud

energy_out_router = APIRouter(
    prefix="/models/energy_outs",
    tags=["EnergyOut"]
)

@energy_out_router.get("/", response_model=List[EnergyOutSchema])
def read_energy_outs(db: Session = Depends(get_db)):
    energy_outs = crud.get_all(db, EnergyOut)
    return energy_outs

@energy_out_router.get("/{id}", response_model=EnergyOutSchema)
def read_energy_out(id: int, db: Session = Depends(get_db)):
    energy_out = crud.get_by_id(db, EnergyOut, id)
    if not energy_out:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EnergyOut not found")
    return energy_out

@energy_out_router.post("/", response_model=EnergyOutSchema, status_code=status.HTTP_201_CREATED)
def create_energy_out(energy_out: EnergyOutCreate = {}, db: Session = Depends(get_db)):
    return crud.create(db, EnergyOut, energy_out)

@energy_out_router.put("/{id}", response_model=EnergyOutSchema)
def update_energy_out(id: int, energy_out_update: EnergyOutUpdate = {}, db: Session = Depends(get_db)):
    updated_energy_out = crud.update(db, EnergyOut, id, energy_out_update)
    if not updated_energy_out:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EnergyOut not found")
    return updated_energy_out

@energy_out_router.delete("/{id}", response_model=EnergyOutSchema)
def delete_energy_out(id: int, db: Session = Depends(get_db)):
    deleted_energy_out = crud.delete(db, EnergyOut, id)
    if not deleted_energy_out:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EnergyOut not found")
    return deleted_energy_out