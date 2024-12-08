from ninja import NinjaAPI
from objects.api import objects_router

api = NinjaAPI()

api.add_router("/objects/", objects_router)