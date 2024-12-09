from django.db import models
from app.Enums.ModelEnums import EnergyInType
from objects.models.EnergyIn import EnergyIn

class WindTurbine(EnergyIn):
    rotor_diameter = models.IntegerField(default=0)
    rotation = models.IntegerField(default=0)
    cut_in_speed = models.IntegerField(default=0)
    rated_speed = models.IntegerField(default=0)
    cut_off_speed = models.IntegerField(default=0)

    @classmethod
    def create(cls, project, **kwargs):
        instance = WindTurbine.objects.create(project=project, type=EnergyInType.WindTurbine, name="Solar Panel", **kwargs)
        instance.save()
        return instance