from ninja import Router
from objects.views.ProjectViewSet import router
from objects.views.ObjectViewSets import energy_in_router, energy_out_router, energy_storage_router, ion_router, wind_turbine_router, solar_panel_router

objects_router = Router()

objects_router.add_router("projects", router)
objects_router.add_router("energy-ins", energy_in_router)
objects_router.add_router("energy-outs", energy_out_router)
objects_router.add_router("energy-storages", energy_storage_router)
objects_router.add_router("lithium-ions", ion_router)
objects_router.add_router("wind-turbines", wind_turbine_router)
objects_router.add_router("solar_panels", solar_panel_router)