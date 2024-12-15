from rest_framework import serializers
from objects.models.Node import Node, NodePosition

class NodePositionSerializer(serializers.ModelSerializer):
    x = serializers.FloatField(required=True)
    y = serializers.FloatField(required=True)
    class Meta:
        model = NodePosition
        fields = ['x', 'y']

class NodeSerializer(serializers.ModelSerializer):
    position = NodePositionSerializer()
    id = serializers.SerializerMethodField()

    class Meta:
        model = Node
        exclude = ['project']

    def get_id(self, obj):
        return str(obj.id)  # Convert id to string
