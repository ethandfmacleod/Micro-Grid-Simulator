from rest_framework import serializers
from objects.models.Node import Node, NodePosition
from drf_spectacular.utils import extend_schema_field

class NodePositionSerializer(serializers.ModelSerializer):
    x = serializers.FloatField(required=True)
    y = serializers.FloatField(required=True)
    class Meta:
        model = NodePosition
        fields = ['x', 'y']

class NodeSerializer(serializers.ModelSerializer):
    position = NodePositionSerializer()
    id = serializers.SerializerMethodField()
    data = serializers.SerializerMethodField()

    class Meta:
        model = Node
        fields = '__all__'

    @extend_schema_field(serializers.CharField())
    def get_id(self, obj):
        return str(obj.id)
    
    @extend_schema_field(serializers.DictField())
    def get_data(self, obj):
        property_sets = obj.property_sets.all()
        return {
            'calculationMode': obj.calculation_mode,
            'ids': [property_set.id for property_set in property_sets],
            'nodeID': obj.id
        }

    # Update position object from Node
    def update(self, instance, validated_data):
        # Handle position update
        position_data = validated_data.pop('position', None)

        # Get positional data
        if position_data:
            NodePosition.objects.filter(pk=instance.position.pk).update(**position_data)

        # Check for calculation_mode change
        new_calculation_mode = validated_data.get('calculation_mode')
        if new_calculation_mode and new_calculation_mode != instance.calculation_mode:
            instance.calculation_mode = new_calculation_mode
            instance.save()
            # Trigger recalculation
            instance.calculate_outputs()

        # Update other fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

