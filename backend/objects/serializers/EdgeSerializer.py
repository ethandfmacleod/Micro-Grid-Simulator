from rest_framework import serializers
from objects.models import Edge
from drf_spectacular.utils import extend_schema_field

class EdgeSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    source = serializers.SerializerMethodField()
    target = serializers.SerializerMethodField()

    class Meta:
        model = Edge
        fields = '__all__'

    @extend_schema_field(serializers.CharField())
    def get_id(self, obj):
        return str(obj.id)

    @extend_schema_field(serializers.CharField())
    def get_source(self, obj):
        return str(obj.source.id)
    
    @extend_schema_field(serializers.CharField())
    def get_target(self, obj):
        return str(obj.target.id)