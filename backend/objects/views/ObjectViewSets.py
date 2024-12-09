from typing import List
from ninja import Router
from ninja_crud import views, viewsets
from objects.schemas import (
    EnergyInSchema, EnergyInPatchSchema, EnergyInCreateSchema,
    EnergyOutSchema, EnergyOutPatchSchema, EnergyOutCreateSchema,
    EnergyStorageUnitSchema, EnergyStorageUnitPatchSchema, EnergyStorageUnitCreateSchema,
    LithiumIonBatterySchema, LithiumIonBatteryPatchSchema, LithiumIonBatteryCreateSchema,
    SolarPanelSchema, SolarPanelPatchSchema, SolarPanelCreateSchema,
    WindTurbineSchema, WindTurbinePatchSchema, WindTurbineCreateSchema,
)
from objects.models import (
    EnergyIn, EnergyOut, EnergyStorageUnit, LithiumIonBattery, SolarPanel, WindTurbine
)

energy_in_router = Router()

# EnergyIn ViewSet
class EnergyInViewSet(viewsets.APIViewSet):
    router = energy_in_router
    model = EnergyIn

    list = views.ListView(response_body=List[EnergyInSchema])
    create = views.CreateView(request_body=EnergyInCreateSchema, response_body=EnergyInSchema)
    read = views.ReadView(response_body=EnergyInSchema)
    update = views.UpdateView(request_body=EnergyInPatchSchema, response_body=EnergyInSchema)
    delete = views.DeleteView()

energy_out_router = Router()

# EnergyOut ViewSet
class EnergyOutViewSet(viewsets.APIViewSet):
    router = energy_out_router
    model = EnergyOut

    list = views.ListView(response_body=List[EnergyOutSchema])
    create = views.CreateView(request_body=EnergyOutCreateSchema, response_body=EnergyOutSchema)
    read = views.ReadView(response_body=EnergyOutSchema)
    update = views.UpdateView(request_body=EnergyOutPatchSchema, response_body=EnergyOutSchema)
    delete = views.DeleteView()

energy_storage_router = Router()

# EnergyStorageUnit ViewSet
class EnergyStorageUnitViewSet(viewsets.APIViewSet):
    router = energy_storage_router
    model = EnergyStorageUnit

    list = views.ListView(response_body=List[EnergyStorageUnitSchema])
    create = views.CreateView(request_body=EnergyStorageUnitCreateSchema, response_body=EnergyStorageUnitSchema)
    read = views.ReadView(response_body=EnergyStorageUnitSchema)
    update = views.UpdateView(request_body=EnergyStorageUnitPatchSchema, response_body=EnergyStorageUnitSchema)
    delete = views.DeleteView()

ion_router = Router()

# LithiumIonBattery ViewSet
class LithiumIonBatteryViewSet(viewsets.APIViewSet):
    router = ion_router
    model = LithiumIonBattery

    list = views.ListView(response_body=List[LithiumIonBatterySchema])
    create = views.CreateView(request_body=LithiumIonBatteryCreateSchema, response_body=LithiumIonBatterySchema)
    read = views.ReadView(response_body=LithiumIonBatterySchema)
    update = views.UpdateView(request_body=LithiumIonBatteryPatchSchema, response_body=LithiumIonBatterySchema)
    delete = views.DeleteView()

solar_panel_router = Router()

# SolarPanel ViewSet
class SolarPanelViewSet(viewsets.APIViewSet):
    router = solar_panel_router
    model = SolarPanel

    list = views.ListView(response_body=List[SolarPanelSchema])
    create = views.CreateView(request_body=SolarPanelCreateSchema, response_body=SolarPanelSchema)
    read = views.ReadView(response_body=SolarPanelSchema)
    update = views.UpdateView(request_body=SolarPanelPatchSchema, response_body=SolarPanelSchema)
    delete = views.DeleteView()

wind_turbine_router = Router()

# WindTurbine ViewSet
class WindTurbineViewSet(viewsets.APIViewSet):
    router = wind_turbine_router
    model = WindTurbine

    list = views.ListView(response_body=List[WindTurbineSchema])
    create = views.CreateView(request_body=WindTurbineCreateSchema, response_body=WindTurbineSchema)
    read = views.ReadView(response_body=WindTurbineSchema)
    update = views.UpdateView(request_body=WindTurbinePatchSchema, response_body=WindTurbineSchema)
    delete = views.DeleteView()
