from app.Enums.ModelEnums import ObjectType, SolarPanelMaterial, SolarPanelType

solar_panel_properties = {
    'name': 'Solar Panel',
    'type': ObjectType.SolarPanel,
    'properties': [
        {'key': 'watts', 'type': 'numeric', 'displayName': 'Watts', 'value': 0.0},
        {'key': 'price', 'type': 'numeric', 'displayName': 'Price', 'value': 0.0},
        {'key': 'daily_emissions', 'type': 'numeric', 'displayName': 'Daily Emissions', 'value': 0.0},
        {'key': 'width', 'type': 'numeric', 'displayName': 'Width', 'value': 0.0},
        {'key': 'length', 'type': 'numeric', 'displayName': 'Length', 'value': 0.0},
        {'key': 'cells', 'type': 'numeric', 'displayName': 'Cells', 'value': 0},
        {'key': 'panel_type', 'type': 'dropdown', 'displayName': 'Panel Type', 'value': SolarPanelType.Default},
        {'key': 'material', 'type': 'dropdown', 'displayName': 'Material', 'value': SolarPanelMaterial.Default}
    ]
}

lithium_ion_battery_properties = {
    'name': 'Lithium Ion Battery',
    'type': ObjectType.LithiumIon,
    'properties': [
        {'key': 'capacity', 'type': 'numeric', 'displayName': 'Capacity', 'value': 0.0},
        {'key': 'charge_level', 'type': 'numeric', 'displayName': 'Charge Level', 'value': 0.0},
        {'key': 'max_charge_rate', 'type': 'numeric', 'displayName': 'Max Charge Rate', 'value': 0.0},
        {'key': 'efficiency', 'type': 'numeric', 'displayName': 'Efficiency', 'value': 0.0},
        {'key': 'current', 'type': 'numeric', 'displayName': 'Current', 'value': 0},
        {'key': 'voltage', 'type': 'numeric', 'displayName': 'Voltage', 'value': 0}
    ]
}

wind_turbine_properties = {
    'name': 'Wind Turbine',
    'type': ObjectType.WindTurbine,
    'properties': [
        {'key': 'watts', 'type': 'numeric', 'displayName': 'Watts', 'value': 0.0},
        {'key': 'price', 'type': 'numeric', 'displayName': 'Price', 'value': 0.0},
        {'key': 'daily_emissions', 'type': 'numeric', 'displayName': 'Daily Emissions', 'value': 0.0},
        {'key': 'rotor_diameter', 'type': 'numeric', 'displayName': 'Rotor Diameter', 'value': 0},
        {'key': 'rotation', 'type': 'numeric', 'displayName': 'Rotation', 'value': 0},
        {'key': 'cut_in_speed', 'type': 'numeric', 'displayName': 'Cut-in Speed', 'value': 0},
        {'key': 'rated_speed', 'type': 'numeric', 'displayName': 'Rated Speed', 'value': 0},
        {'key': 'cut_off_speed', 'type': 'numeric', 'displayName': 'Cut-off Speed', 'value': 0}
    ]
}

propertyInfoMap = {
    ObjectType.SolarPanel: solar_panel_properties,
    ObjectType.LithiumIon: lithium_ion_battery_properties,
    ObjectType.WindTurbine: wind_turbine_properties
}

def get_object_configuration(type):
    return propertyInfoMap.get(type, solar_panel_properties)
