from django.db import models
from app.Enums.ModelEnums import EnergyInType, SolarPanelMaterial, SolarPanelType
from objects.models.EnergyIn import EnergyIn

class SolarPanel(EnergyIn):
    width = models.FloatField(default=0.0)
    length = models.FloatField(default=0.0)
    cells = models.IntegerField(default=0)
    panel_type = models.CharField(choices=SolarPanelType.choices, default=SolarPanelType.Default)
    material = models.CharField(choices=SolarPanelMaterial.choices, default=SolarPanelMaterial.Default)

    @classmethod
    def create(cls, project, **kwargs):
        instance = SolarPanel.objects.create(project=project, type=EnergyInType.SolarPanel, name="Solar Panel", **kwargs)
        instance.save()
        return instance