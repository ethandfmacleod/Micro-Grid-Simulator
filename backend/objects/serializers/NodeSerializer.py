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

    # Update position object from Node
    def update(self, instance, validated_data):
        # Handle position update
        position_data = validated_data.pop('position', None)

        if position_data:
            NodePosition.objects.filter(pk=instance.position.pk).update(**position_data)

        # Update other fields of Node (if any)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

