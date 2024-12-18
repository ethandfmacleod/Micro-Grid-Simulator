from django.db import models
from flowsheet.models import Project

class Edge(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_edges')
    source = models.ForeignKey("ObjectBase", on_delete=models.CASCADE, related_name="from_node")
    target = models.ForeignKey("ObjectBase", on_delete=models.CASCADE, related_name="to_node")