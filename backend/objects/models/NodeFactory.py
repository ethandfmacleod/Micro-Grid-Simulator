import copy
from app.Enums.ModelEnums import ObjectType
from .configs import *

class NodeFactory:
    def __init__(self):
        self.property_info_map = {
            ObjectType.SolarPanel: solar_config,
            ObjectType.LithiumIon: lithium_ion_config,
            ObjectType.WindTurbine: wind_config,
            ObjectType.Home: home_config,
        }

    def get_configuration(self, object_type):
        return copy.deepcopy(self.property_info_map.get(object_type, solar_config))
