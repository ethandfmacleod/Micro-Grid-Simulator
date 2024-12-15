from django.db import models
from app.Enums.ModelEnums import DisplayType, ObjectType
from objects.models.Configs import get_object_configuration
from flowsheet.models import Project

class ObjectBase(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='flowsheet_objects')
    name = models.CharField(max_length=32, default="New Object")
    object_type = models.CharField(choices=ObjectType, default=ObjectType.SolarPanel)
    property_set = models.ForeignKey("PropertySet", on_delete=models.CASCADE, related_name='object_owner', null=True)
    
    @classmethod
    def create(self, project, type):
        config = get_object_configuration(type=type)
        properties = config.pop(properties)

        property_set = PropertySet.objects.create()
        property_set.save()

        instance = ObjectBase.objects.create(project=project, property_set=property_set **config)
        instance.save()

        self.create_properties(config=properties, set=property_set)
        return instance
    
    def create_properties(self, config, set):
        properties = []
        for property in config:
            properties.append(PropertyInfo(set=set, **property))
        PropertyInfo.objects.bulk_create(properties)

class PropertySet(models.Model):
    name = models.CharField(default="Property Set")

class PropertyInfo(models.Model):
    set = models.ForeignKey("PropertySet", on_delete=models.CASCADE, related_name="properties")
    type = models.CharField(choices=DisplayType.choices, default=DisplayType.numeric)
    value = models.JSONField(null=True, blank=True)
    key = models.CharField(max_length=64)
    display_name = models.CharField(max_length=64)

 