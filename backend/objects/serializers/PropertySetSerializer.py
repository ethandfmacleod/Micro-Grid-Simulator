from rest_framework import serializers
from objects.models.ObjectBase import PropertyInfo, PropertySet

class PropertyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyInfo
        fields = '__all__'

class PropertySetSerializer(serializers.ModelSerializer):
    properties = PropertyInfoSerializer(many=True, read_only=True)
    class Meta:
        model = PropertySet
        fields = '__all__'