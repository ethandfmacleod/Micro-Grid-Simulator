from django.db import models
from django.utils import timezone

class Project(models.Model):
    name = models.CharField(max_length=32, default="New Project")
    date = models.DateTimeField(null=True)

    @classmethod
    def create(cls):
        project_number = Project.objects.count() + 1
        new_date = timezone.now()
        instance = Project.objects.create(name=f'New Project {project_number}', date=new_date)
        instance.save()
        return instance