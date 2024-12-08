from ninja import Router
from objects.views.ProjectViewSet import router

objects_router = Router()

objects_router.add_router("projects", router)