
from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.Project import *
from app.routes import crud

project_router = APIRouter(
    prefix="/projects",
    tags=["Project"]
)

@project_router.get("/", response_model=List[ProjectSchema])
def read_projects(db: Session = Depends(get_db)):
    projects = crud.get_all(db, Project)
    return projects

@project_router.get("/{id}", response_model=ProjectSchema)
def read_project(id: int, db: Session = Depends(get_db)):
    project = crud.get_by_id(db, Project, id)
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    return project

@project_router.post("/", response_model=ProjectSchema, status_code=status.HTTP_201_CREATED)
def create_project(project: ProjectCreate = {}, db: Session = Depends(get_db)):
    return crud.create(db, Project, project)

@project_router.put("/{id}", response_model=ProjectSchema)
def update_project(id: int, project_update: ProjectUpdate = {}, db: Session = Depends(get_db)):
    updated_project = crud.update(db, Project, id, project_update)
    if not updated_project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    return updated_project

@project_router.delete("/{id}", response_model=ProjectSchema)
def delete_project(id: int, db: Session = Depends(get_db)):
    deleted_project = crud.delete(db, Project, id)
    if not deleted_project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    return deleted_project