from rest_framework import serializers
from objects.models import ObjectBase

class ObjectBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectBase
        fields = '__all__'