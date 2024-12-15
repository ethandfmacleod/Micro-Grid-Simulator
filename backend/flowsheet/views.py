from rest_framework import viewsets
from flowsheet.models import Project
from flowsheet.serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer