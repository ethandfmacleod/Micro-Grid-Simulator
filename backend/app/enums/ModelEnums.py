from enum import Enum

class EnergyInType(Enum):
    Default = "default"
    SolarPanel = "solar_panel"
    WindTurbine = "wind_turbine"

class EnergyOutType(Enum):
    Default = "default"
    FactoryModel = "factory_model"
    ComplexHome = "complex_home"
    GeneralConsumer = "general_consumer"

class EnergyStorageType(Enum):
    Default = "default"
    LithiumIon = "lithium_ion"

class SolarPanelType(Enum):
    Default = "default"

class SolarPanelMaterial(Enum):
    Default = "default"