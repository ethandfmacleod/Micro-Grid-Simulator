from rest_framework import serializers
from objects.models import Edge

class EdgeSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    source = serializers.SerializerMethodField()
    target = serializers.SerializerMethodField()

    class Meta:
        model = Edge
        fields = '__all__'

    def get_id(self, obj):
        return str(obj.id)

    def get_source(self, obj):
        return str(obj.source)
    
    def get_target(self, obj):
        return str(obj.target)