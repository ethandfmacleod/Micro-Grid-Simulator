from rest_framework import serializers
from objects.models.PropertyModels import PropertyInfo, PropertySet

class PropertyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyInfo
        fields = '__all__'
    
    def update(self, instance, validated_data):
        """
        Triggers a recalculation of connected node(s) on change
        """
        instance = super().update(instance, validated_data)
        instance.defined = True
        instance.save()

        if instance.value is not None:
            instance.set.node.calculate_outputs()

        return instance

class PropertySetSerializer(serializers.ModelSerializer):
    properties = PropertyInfoSerializer(many=True, read_only=True)
    class Meta:
        model = PropertySet
        fields = '__all__'