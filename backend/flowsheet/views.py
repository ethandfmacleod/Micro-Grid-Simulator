from rest_framework import viewsets
from flowsheet.models import Project
from rest_framework.response import Response
from flowsheet.serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def create(self, request):
        try:
            instance = Project.create()
            instance.save()

            # Serialize and return the created object
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=201)

        except Exception as e:
            return str(e)
