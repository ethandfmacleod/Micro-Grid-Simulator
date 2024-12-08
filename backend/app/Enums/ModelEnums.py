from django.db import models

class EnergyInType(models.TextChoices):
    Default = "default"
    SolarPanel = "solar_panel"
    WindTurbine = "wind_turbine"

class EnergyOutType(models.TextChoices):
    Default = "default"
    FactoryModel = "factory_model"
    ComplexHome = "complex_home"
    GeneralConsumer = "general_consumer"

class EnergyStorageType(models.TextChoices):
    Default = "default"
    LithiumIon = "lithium_ion"

class SolarPanelType(models.TextChoices):
    Default = "default"

class SolarPanelMaterial(models.TextChoices):
    Default = "default"