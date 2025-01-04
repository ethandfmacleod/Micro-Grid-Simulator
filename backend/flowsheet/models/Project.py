from django.db import models
from django.utils import timezone
from flowsheet.models.Controller import Controller

class Project(models.Model):
    name = models.CharField(max_length=32, default="New Project")
    date = models.DateTimeField(null=True)
    controller = models.ForeignKey(Controller, on_delete=models.CASCADE, related_name="controller_project")

    @classmethod
    def create(cls):
        project_number = Project.objects.count() + 1
        new_date = timezone.now()
        controller = Controller.create()
        instance = Project.objects.create(name=f'New Project {project_number}', date=new_date, controller=controller)
        instance.save()
        return instance