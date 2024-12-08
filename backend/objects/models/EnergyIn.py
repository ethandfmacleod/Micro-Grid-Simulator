from django.db import models
from app.Enums.ModelEnums import EnergyInType
from objects.models.ObjectBase import ObjectBase

class EnergyIn(ObjectBase):
    watts = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)
    daily_emissions = models.IntegerField(default=0)
    type = models.CharField(choices=EnergyInType.choices, default=EnergyInType.Default)

    class Meta:
        abstract=True