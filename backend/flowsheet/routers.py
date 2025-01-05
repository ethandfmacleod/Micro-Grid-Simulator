from rest_framework.routers import DefaultRouter
from flowsheet.views import ControllerViewSet, ProjectViewSet, WeatherDataViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename="projects")
router.register(r"controllers", ControllerViewSet, basename="controllers")
router.register(r"weather_data", WeatherDataViewSet, basename="weather_data")

urlpatterns = router.urls
