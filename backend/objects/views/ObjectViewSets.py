import traceback
from rest_framework.response import Response
from rest_framework import viewsets
from flowsheet.models import Project
from objects.models import ObjectBase
from objects.serializers.ObjectSerializers import ObjectBaseSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes

class ObjectViewSet(viewsets.ModelViewSet):
    queryset = ObjectBase.objects.all()
    serializer_class = ObjectBaseSerializer

    def get_queryset(self):
        queryset = self.queryset
        projectID = self.request.query_params.get("projectID")
        if projectID is not None:
            queryset = queryset.filter(project=projectID)
        return queryset

    @extend_schema(
        parameters=[ 
            OpenApiParameter(name="projectID", required=True, type=OpenApiTypes.INT),
        ]
    )
    def list(self, request):
        return super().list(request)
    
    def error_response(self, e):
        tb_info = traceback.format_exc()
        error_message = str(e)
        response_data = {'status': 'error', 'message': error_message, 'traceback': tb_info}
        return Response(response_data, status=400)
    
    def create(self, request, *args, **kwargs):
        try:
            # Extract data from the request
            projectID = request.data.get("project")
            project = Project.objects.get(pk=projectID)
            object_type = request.data.get("type")
            x = request.data.get("x", 0)  # Default to 0 if not provided
            y = request.data.get("y", 0)  # Default to 0 if not provided
            
            # Ensure required fields are provided
            if not project or not object_type:
                return Response({"error": "Missing required fields: 'project' or 'object_type'"}, status=400)

            # Use the ObjectBase.create method
            instance = ObjectBase.create(
                project=project,
                type=object_type,
                x=x,
                y=y,
            )

            # Serialize and return the created object
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=201)

        except Exception as e:
            return self.error_response(e)