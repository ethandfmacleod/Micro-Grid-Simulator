
from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.routes import crud
from app.models.WindTurbine import *

wind_turbine_router = APIRouter(
    prefix="/models/wind_turbines",
    tags=["WindTurbine"]
)

@wind_turbine_router.get("/", response_model=List[WindTurbineSchema])
def read_wind_turbines(db: Session = Depends(get_db)):
    wind_turbines = crud.get_all(db, WindTurbine)
    return wind_turbines

@wind_turbine_router.get("/{id}", response_model=WindTurbineSchema)
def read_wind_turbine(id: int, db: Session = Depends(get_db)):
    wind_turbine = crud.get_by_id(db, WindTurbine, id)
    if not wind_turbine:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Wind Turbine not found")
    return wind_turbine

@wind_turbine_router.post("/", response_model=WindTurbineSchema, status_code=status.HTTP_201_CREATED)
def create_wind_turbine(wind_turbine: WindTurbineCreate = {}, db: Session = Depends(get_db)):
    return crud.create(db, WindTurbine, wind_turbine)

@wind_turbine_router.put("/{id}", response_model=WindTurbineSchema)
def update_wind_turbine(id: int, wind_turbine_update: WindTurbineUpdate, db: Session = Depends(get_db)):
    updated_wind_turbine = crud.update(db, WindTurbine, id, wind_turbine_update)
    if not updated_wind_turbine:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Wind Turbine not found")
    return updated_wind_turbine

@wind_turbine_router.delete("/{id}", response_model=WindTurbineSchema)
def delete_wind_turbine(id: int, db: Session = Depends(get_db)):
    deleted_wind_turbine = crud.delete(db, WindTurbine, id)
    if not deleted_wind_turbine:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Wind Turbine not found")
    return deleted_wind_turbine