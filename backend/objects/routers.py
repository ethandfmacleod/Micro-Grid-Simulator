from rest_framework.routers import DefaultRouter
from objects.views.PropertyInfoViewSet import PropertyInfoViewSet
from objects.views.PropertySetViewSet import PropertySetViewSet
from objects.views.NodeViewSet import NodeViewSet
from objects.views.EdgeViewSet import EdgeViewSet

router = DefaultRouter()
router.register(r'edges', EdgeViewSet, basename="edges")
router.register(r'nodes', NodeViewSet, basename="nodes")
router.register(r'sets', PropertySetViewSet, basename='sets')
router.register(r'properties', PropertyInfoViewSet, basename='properties')

urlpatterns = router.urls