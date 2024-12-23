from django.db import models

class BaseType(models.TextChoices):
    EnergyIn = "energy_in"
    EnergyOut = "energy_out"
    EnergyStorage = "energy_storage"

class ObjectType(models.TextChoices):
    SolarPanel = "solar_panel"
    WindTurbine = "wind_turbine"
    FactoryModel = "factory_model"
    ComplexHome = "complex_home"
    GeneralConsumer = "general_consumer"
    LithiumIon = "lithium_ion"

class SolarPanelType(models.TextChoices):
    Residential = "Residential"
    Commercial = "Commercial"

class SolarPanelMaterial(models.TextChoices):
    Monocrystalline  = "Monocrystalline"
    Polycrystalline = "Polycrystalline"
    ThinFilm = "Thin-Film"

class CalculationMode(models.TextChoices):
    SolarPowerBased = "Power Based"
    Electrical = "Electrical"
    Physical = "Physical"

class DisplayType(models.TextChoices):
    numeric = "numeric"
    dropdown = "dropdown"
    checkbox = "checkbox"
    segmented = "segmented"
    text = "text"