from fastapi import FastAPI, Depends
from app.models import * # Required for folder structure
from app.routes import *
from app.database import engine, Base

app = FastAPI()
Base.metadata.create_all(bind=engine)

# Set routes
routers = [energy_in_router, solar_panel_router, wind_turbine_router, energy_out_router, project_router, energy_storage_router, lithium_ion_router]

# Include all defined routes
for router in routers:
    app.include_router(router)
