from django.db import models
from app.Enums.ModelEnums import EnergyStorageType
from objects.models.ObjectBase import ObjectBase

class EnergyStorageUnit(ObjectBase):
    capacity = models.FloatField(default=0)
    charge_level = models.FloatField(default=0)
    price = models.FloatField(default=0)
    type = models.CharField(choices=EnergyStorageType.choices, default=EnergyStorageType.Default)