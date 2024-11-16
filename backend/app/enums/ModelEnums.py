import enum

class EnergyInType(enum.Enum):
    Default = "default"
    SolarPanel = "solar_panel"
    WindTurbine = "wind_turbine"

class SolarPanelType(enum.Enum):
    Default = "default"

class SolarPanelMaterial(enum.Enum):
    Default = "default"