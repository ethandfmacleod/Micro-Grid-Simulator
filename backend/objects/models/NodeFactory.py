import copy
from app.Enums.ModelEnums import ObjectType
from objects.models.PropertyModels import PropertyInfo
from .configs import *

class NodeFactory:
    def __init__(self, weather_data=None):
        self.weather_data=weather_data
        self.property_info_map = {
            ObjectType.SolarPanel: solar_config,
            ObjectType.LithiumIon: lithium_ion_config,
            ObjectType.WindTurbine: wind_config,
            ObjectType.Home: home_config,
            ObjectType.Inverter: inverter_config
        }

    def get_configuration(self, object_type):
        return copy.deepcopy(self.property_info_map.get(object_type, solar_config))

    def create_properties(self, properties_config, property_set, project):
        properties = []
        for prop_config in properties_config:
            # Handle shared properties
            if prop_config.get("weather"):
                shared_property = getattr(self.weather_data, prop_config["key"], None)
                if shared_property:
                    property_set.properties.add(shared_property)
                continue
            if prop_config.get("shared"):
                from objects.models.Node import Node
                model = Node.objects.filter(type=prop_config["model"], project=project).first()
                if model:
                    outputs_set = model.get_property_set(prop_config["set"])
                    print(f"Properties in 'Outputs': {[prop.key for prop in outputs_set.properties.all()]}")
                prop_set = model.get_property_set(prop_config["set"])
                property = prop_set.get_property(prop_config["key"])
                if property:
                    property_set.properties.add(property)
                    properties.append(property)
                continue

            # Create new PropertyInfo for non-shared properties
            property = PropertyInfo.objects.create(
                key=prop_config["key"],
                display_type=prop_config["display_type"],
                display_name=prop_config["display_name"],
                value=prop_config.get("value", ""),
                disabled=prop_config.get("disabled", False),
                defined=prop_config.get("defined", False),
                hidden=prop_config.get("hidden", False)
            )
            property.save()
            property_set.properties.add(property)
            property_set.save()
            properties.append(property)

        for prop in property_set.properties.all():
            print

        return properties
