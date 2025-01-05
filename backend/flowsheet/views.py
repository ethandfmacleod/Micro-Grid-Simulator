import traceback
from rest_framework import viewsets
from flowsheet.models.WeatherData import WeatherData
from flowsheet.models.Controller import Controller
from flowsheet.models import Project
from rest_framework.response import Response
from flowsheet.serializers import ControllerSerializer, ProjectSerializer, WeatherDataSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes

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
            return self.error_response(e)
    
    def error_response(self, e):
        tb_info = traceback.format_exc()
        error_message = str(e)
        response_data = {
            "status": "error",
            "message": error_message,
            "traceback": tb_info,
        }
        return Response(response_data, status=400)

class ControllerViewSet(viewsets.ModelViewSet):
    queryset = Controller.objects.all()
    serializer_class = ControllerSerializer

    def get_queryset(self):
        queryset = self.queryset
        projectID = self.request.query_params.get("projectID")
        if projectID is not None:
            queryset = queryset.filter(controller_project=projectID)
        return queryset

    @extend_schema(
        parameters=[
            OpenApiParameter(name="projectID", required=True, type=OpenApiTypes.INT),
        ]
    )
    def list(self, request):
        return super().list(request)


class WeatherDataViewSet(viewsets.ModelViewSet):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer

    def get_queryset(self):
        queryset = self.queryset
        controllerID = self.request.query_params.get("controllerID")
        if controllerID is not None:
            queryset = queryset.filter(weather_controller=controllerID)
        return queryset

    @extend_schema(
        parameters=[
            OpenApiParameter(name="controllerID", required=True, type=OpenApiTypes.INT),
        ]
    )
    def list(self, request):
        return super().list(request)
