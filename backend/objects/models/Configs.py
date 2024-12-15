import copy
from app.Enums.ModelEnums import ObjectType, SolarPanelMaterial, SolarPanelType

solar_panel_properties = {
    'name': 'Solar Panel',
    'type': ObjectType.SolarPanel,
    'properties': [
        {'key': 'watts', 'type': 'numeric', 'display_name': 'Watts', 'value': 0.0},
        {'key': 'price', 'type': 'numeric', 'display_name': 'Price', 'value': 0.0},
        {'key': 'daily_emissions', 'type': 'numeric', 'display_name': 'Daily Emissions', 'value': 0.0},
        {'key': 'width', 'type': 'numeric', 'display_name': 'Width', 'value': 0.0},
        {'key': 'length', 'type': 'numeric', 'display_name': 'Length', 'value': 0.0},
        {'key': 'cells', 'type': 'numeric', 'display_name': 'Cells', 'value': 0},
        {'key': 'panel_type', 'type': 'dropdown', 'display_name': 'Panel Type', 'value': SolarPanelType.Default},
        {'key': 'material', 'type': 'dropdown', 'display_name': 'Material', 'value': SolarPanelMaterial.Default}
    ]
}

lithium_ion_battery_properties = {
    'name': 'Lithium Ion Battery',
    'type': ObjectType.LithiumIon,
    'properties': [
        {'key': 'capacity', 'type': 'numeric', 'display_name': 'Capacity', 'value': 0.0},
        {'key': 'charge_level', 'type': 'numeric', 'display_name': 'Charge Level', 'value': 0.0},
        {'key': 'max_charge_rate', 'type': 'numeric', 'display_name': 'Max Charge Rate', 'value': 0.0},
        {'key': 'efficiency', 'type': 'numeric', 'display_name': 'Efficiency', 'value': 0.0},
        {'key': 'current', 'type': 'numeric', 'display_name': 'Current', 'value': 0},
        {'key': 'voltage', 'type': 'numeric', 'display_name': 'Voltage', 'value': 0}
    ]
}

wind_turbine_properties = {
    'name': 'Wind Turbine',
    'type': ObjectType.WindTurbine,
    'properties': [
        {'key': 'watts', 'type': 'numeric', 'display_name': 'Watts', 'value': 0.0},
        {'key': 'price', 'type': 'numeric', 'display_name': 'Price', 'value': 0.0},
        {'key': 'daily_emissions', 'type': 'numeric', 'display_name': 'Daily Emissions', 'value': 0.0},
        {'key': 'rotor_diameter', 'type': 'numeric', 'display_name': 'Rotor Diameter', 'value': 0},
        {'key': 'rotation', 'type': 'numeric', 'display_name': 'Rotation', 'value': 0},
        {'key': 'cut_in_speed', 'type': 'numeric', 'display_name': 'Cut-in Speed', 'value': 0},
        {'key': 'rated_speed', 'type': 'numeric', 'display_name': 'Rated Speed', 'value': 0},
        {'key': 'cut_off_speed', 'type': 'numeric', 'display_name': 'Cut-off Speed', 'value': 0}
    ]
}

propertyInfoMap = {
    ObjectType.SolarPanel: solar_panel_properties,
    ObjectType.LithiumIon: lithium_ion_battery_properties,
    ObjectType.WindTurbine: wind_turbine_properties
}

def get_object_configuration(type):
    return copy.deepcopy(propertyInfoMap.get(type, solar_panel_properties))
