import traceback
from rest_framework.response import Response
from rest_framework import viewsets
from objects.models.PropertyModels import PropertyInfo
from objects.serializers.PropertySetSerializer import PropertyInfoSerializer

class PropertyInfoViewSet(viewsets.ModelViewSet):
    queryset = PropertyInfo.objects.all()
    serializer_class = PropertyInfoSerializer

    def get_queryset(self):
        return self.queryset

    def list(self, request):
        return super().list(request)
    
    def error_response(self, e):
        tb_info = traceback.format_exc()
        error_message = str(e)
        response_data = {'status': 'error', 'message': error_message, 'traceback': tb_info}
        return Response(response_data, status=400)