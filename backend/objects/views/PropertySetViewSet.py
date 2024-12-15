import traceback
from rest_framework.response import Response
from rest_framework import viewsets
from objects.models.ObjectBase import PropertySet
from objects.serializers.PropertySetSerializer import PropertySetSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes

class PropertySetViewSet(viewsets.ModelViewSet):
    queryset = PropertySet.objects.all()
    serializer_class = PropertySetSerializer

    def get_queryset(self):
        queryset = self.queryset
        projectID = self.request.query_params.get("projectID")
        if projectID is not None:
            queryset = queryset.filter(object_owner__project_id=projectID)
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