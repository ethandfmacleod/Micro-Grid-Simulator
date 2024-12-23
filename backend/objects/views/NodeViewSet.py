import traceback
from rest_framework.response import Response
from rest_framework import viewsets, serializers
from flowsheet.models import Project
from objects.serializers.NodeSerializer import NodeSerializer
from objects.models.Node import Node
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes
from rest_framework.decorators import action

class CreateNodeSerializer(serializers.Serializer):
    project = serializers.IntegerField(required=True)
    type = serializers.CharField(required=True)

class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer

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
    
    @extend_schema(request=CreateNodeSerializer, responses=None)
    def create(self, request):
        try:
            # Extract data from the request
            projectID = request.data.get("project")
            project = Project.objects.get(pk=projectID)
            type = request.data.get("type", None)

            # Use the Node.create method
            instance = Node.create(
                project=project,
                type=type
            )

            instance.save()

            # Serialize and return the created object
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=201)

        except Exception as e:
            return self.error_response(e)