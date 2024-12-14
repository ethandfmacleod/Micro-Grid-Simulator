from django.db import models
from app.Enums.ModelEnums import EnergyOutType
from objects.models.ObjectBase import ObjectBase

class EnergyOut(ObjectBase):
    watts = models.IntegerField(default=0)
    daily_emissions = models.IntegerField(default=0)
    type = models.CharField(choices=EnergyOutType.choices, default=EnergyOutType.Default)