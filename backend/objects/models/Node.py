from django.db import models
from app.Enums.ModelEnums import ObjectType
from objects.models.PropertyModels import PropertyInfo, PropertySet
from objects.models.Configs import get_object_configuration
from flowsheet.models import Project

class Node(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_nodes')
    position = models.ForeignKey("NodePosition", on_delete=models.CASCADE, related_name="position_node")
    type = models.CharField(choices=ObjectType, default=ObjectType.SolarPanel)
    calculation_mode = models.CharField(default='Default')
    isOpen = models.BooleanField(default=False)

    @classmethod
    def create(cls, project, type, x=0, y=0):
        """
        Create a Node with associated properties and property sets based on the configuration.
        """
        # Get configuration for the Node type
        config = get_object_configuration(type=type)
        property_sets_config = config.pop('propertySets')  # Retrieve property sets configuration

        # Create the Node instance
        position = NodePosition.objects.create(x=x, y=y)
        node = cls.objects.create(
            project=project,
            position=position,
            type=type,
            **config
        )

        # Create Property Sets and Properties
        for property_set_config in property_sets_config:
            property_set = PropertySet.objects.create(
                name=property_set_config['name'],
                node=node
            )
            property_set.save()
            create_properties(property_set_config['properties'], property_set)

        # Save and return node
        node.save()
        return node

class NodePosition(models.Model):
    x = models.FloatField(default=0.0)
    y = models.FloatField(default=0.0)

def create_properties(properties_config, property_set):
    """
    Create and associate properties with a PropertySet.
    """
    properties = [
        PropertyInfo(set=property_set, **property_config)
        for property_config in properties_config
    ]
    PropertyInfo.objects.bulk_create(properties)
