
from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.EnergyIn import *
from app.routes import crud
from app.models.SolarPanel import *

solar_panel_router = APIRouter(
    prefix="/models/solar_panels",
    tags=["SolarPanel"]
)

@solar_panel_router.get("/", response_model=List[SolarPanelSchema])
def read_solar_panels(db: Session = Depends(get_db)):
    solar_panels = crud.get_all(db, SolarPanel)
    return solar_panels

@solar_panel_router.get("/{id}", response_model=SolarPanelSchema)
def read_solar_panel(id: int, db: Session = Depends(get_db)):
    solar_panel = crud.get_by_id(db, SolarPanel, id)
    if not solar_panel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Solar Panel not found")
    return solar_panel

@solar_panel_router.post("/", response_model=SolarPanelSchema, status_code=status.HTTP_201_CREATED)
def create_solar_panel(solar_panel: SolarPanelCreate = {}, db: Session = Depends(get_db)):
    return crud.create(db, SolarPanel, solar_panel)

@solar_panel_router.put("/{id}", response_model=SolarPanelSchema)
def update_solar_panel(id: int, solar_panel_update: SolarPanelUpdate, db: Session = Depends(get_db)):
    updated_solar_panel = crud.update(db, SolarPanel, id, solar_panel_update)
    if not updated_solar_panel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Solar Panel not found")
    return updated_solar_panel

@solar_panel_router.delete("/{id}", response_model=SolarPanelSchema)
def delete_solar_panel(id: int, db: Session = Depends(get_db)):
    deleted_solar_panel = crud.delete(db, SolarPanel, id)
    if not deleted_solar_panel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Solar Panel not found")
    return deleted_solar_panel