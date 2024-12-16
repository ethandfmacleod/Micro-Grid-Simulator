from django.db import models
from app.Enums.ModelEnums import ObjectType
from flowsheet.models import Project

class Node(models.Model):
    name = models.CharField(max_length=64, default="New Object")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_nodes')
    position = models.ForeignKey("NodePosition", on_delete=models.CASCADE, related_name="position_node")
    type = models.CharField(choices=ObjectType, default=ObjectType.SolarPanel)
    data = models.ForeignKey("PropertySet", on_delete=models.CASCADE, related_name="set_node")

    @classmethod
    def create(self, set, project, x=0, y=0, type=ObjectType.SolarPanel, name="New Object"):
        node_pos = NodePosition.objects.create(x=x, y=y)
        node_pos.save()

        instance = Node.objects.create(project=project, position=node_pos, type=type, data=set, name=name)
        instance.save()

        return instance

class NodePosition(models.Model):
    x = models.FloatField(default=0.0)
    y = models.FloatField(default=0.0)