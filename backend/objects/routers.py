from rest_framework.routers import DefaultRouter
from objects.views.PropertySetViewSet import PropertySetViewSet
from objects.views.NodeViewSet import NodeViewSet
from objects.views.EdgeViewSet import EdgeViewSet
from objects.views.ObjectViewSets import ObjectViewSet

router = DefaultRouter()
router.register(r'objects', ObjectViewSet, basename="objects")
router.register(r'edges', EdgeViewSet, basename="edges")
router.register(r'nodes', NodeViewSet, basename="nodes")
router.register(r'sets', PropertySetViewSet, basename='sets')

urlpatterns = router.urls