from django.db import models
from app.Enums.ModelEnums import EnergyStorageType
from objects.models.EnergyStorageUnit import EnergyStorageUnit

class LithiumIonBattery(EnergyStorageUnit):
    max_charge_rate = models.FloatField(default=0.0)
    efficiency = models.FloatField(default=0.0)
    current = models.IntegerField(default=0)
    voltage = models.IntegerField(default=0)

    @classmethod
    def create(cls, project, **kwargs):
        instance = LithiumIonBattery.objects.create(project=project, type=EnergyStorageType.LithiumIon, name="Lithium Ion Battery", **kwargs)
        instance.save()
        return instance