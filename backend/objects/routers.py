from rest_framework.routers import DefaultRouter
from objects.views.ObjectViewSets import ObjectViewSet

router = DefaultRouter()
router.register(r'objects', ObjectViewSet, basename="objects")

urlpatterns = router.urls