from django.db import models
from objects.models.Project import Project

class ObjectBase(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='objects')
    # node = models.ForeignKey(NodeObject, on_delete=models.CASCADE, related_name='object_owner')

    class Meta:
        abstract=True