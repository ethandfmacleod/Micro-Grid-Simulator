import copy
from app.Enums.ModelEnums import ObjectType, CalculationMode

solar_panel_properties = {
    'calculation_mode': CalculationMode.SolarPowerBased,
    'propertySets': [
        {
            'name': 'Outputs',
            'properties': [
                {'key': 'daily_energy', 'display_type': 'numeric', 'display_name': 'Daily Energy', 'value': '', 'disabled': True},
                # {'key': 'emmisions_offset', 'display_type': 'numeric', 'display_name': 'Co2 Offset', 'value': '', 'disabled': True},
            ]
        },
        {
            'name': CalculationMode.SolarPowerBased,
            'formula': 'watts * irradiance / 1000',
            'properties': [
                {'key': 'watts', 'display_type': 'numeric', 'display_name': 'Watts', 'value': ''},
                {'key': 'irradiance', 'display_type': 'numeric', 'display_name': 'Irradiance', 'value': ''},
            ]
        },
        {
            'name': CalculationMode.Electrical,
            'formula': '(voltage * current * fill_factor * irradiance) / 1000',
            'properties': [
                {'key': 'voltage', 'display_type': 'numeric', 'display_name': 'Voltage', 'value': ''},
                {'key': 'current', 'display_type': 'numeric', 'display_name': 'Current', 'value': ''},
                {'key': 'irradiance', 'display_type': 'numeric', 'display_name': 'Irradiance', 'value': ''},
                {'key': 'fill_factor', 'display_type': 'numeric', 'display_name': 'Fill Factor', 'value': 0.75, 'defined': True},
            ]
        },
        {
            'name': CalculationMode.Physical,
            'formula': '(length * width * irradiance * efficiency) / 100',
            'properties': [
                {'key': 'length', 'display_type': 'numeric', 'display_name': 'Length (m)', 'value': ''},
                {'key': 'width', 'display_type': 'numeric', 'display_name': 'Width (m)', 'value': ''},
                {'key': 'efficiency', 'display_type': 'numeric', 'display_name': 'Efficiency (%)', 'value': 20.0, 'defined': True},
                {'key': 'irradiance', 'display_type': 'numeric', 'display_name': 'Irradiance', 'value': ''},
            ]
        },
        {
            'name': 'Advanced',
            'properties': [
                {'key': 'watts', 'display_type': 'numeric', 'display_name': 'Watts', 'value': ''},
                {'key': 'voltage', 'display_type': 'numeric', 'display_name': 'Voltage', 'value': ''},
                {'key': 'current', 'display_type': 'numeric', 'display_name': 'Current', 'value': ''},
                {'key': 'fill_factor', 'display_type': 'numeric', 'display_name': 'Fill Factor', 'value': 0.75},
                {'key': 'length', 'display_type': 'numeric', 'display_name': 'Length (m)', 'value': ''},
                {'key': 'width', 'display_type': 'numeric', 'display_name': 'Width (m)', 'value': ''},
                {'key': 'efficiency', 'display_type': 'numeric', 'display_name': 'Efficiency (%)', 'value': 20.0},
                {'key': 'irradiance', 'display_type': 'numeric', 'display_name': 'Irradiance', 'value': ''},
                {'key': 'ambient_temp', 'display_type': 'numeric', 'display_name': 'Ambient Temperature (°C)', 'value': 25},
                {'key': 'tilt_angle', 'display_type': 'numeric', 'display_name': 'Tilt Angle (°)', 'value': 30},
                {'key': 'degradation_rate', 'display_type': 'numeric', 'display_name': 'Degradation Rate (%)', 'value': 0.5},
                {'key': 'temperature_coefficient', 'display_type': 'numeric', 'display_name': 'Temperature Coefficient (%/°C)', 'value': -0.3},
                {'key': 'reflectance_loss', 'display_type': 'numeric', 'display_name': 'Reflectance Loss (%)', 'value': 3},
            ]
        },
    ]
}

lithium_ion_battery_properties = {
    'type': ObjectType.LithiumIon,
    'properties': [
        {'key': 'capacity', 'display_type': 'numeric', 'display_name': 'Capacity', 'value': ''},
        {'key': 'charge_level', 'display_type': 'numeric', 'display_name': 'Charge Level', 'value': ''},
        {'key': 'max_charge_rate', 'display_type': 'numeric', 'display_name': 'Max Charge Rate', 'value': ''},
        {'key': 'efficiency', 'display_type': 'numeric', 'display_name': 'Efficiency', 'value': ''},
        {'key': 'current', 'display_type': 'numeric', 'display_name': 'Current', 'value': ''},
        {'key': 'voltage', 'display_type': 'numeric', 'display_name': 'Voltage', 'value': ''}
    ]
}

wind_turbine_properties = {
    'type': ObjectType.WindTurbine,
    'properties': [
        {'key': 'watts', 'display_type': 'numeric', 'display_name': 'Watts', 'value': ''},
        {'key': 'price', 'display_type': 'numeric', 'display_name': 'Price', 'value': ''},
        {'key': 'daily_emissions', 'display_type': 'numeric', 'display_name': 'Daily Emissions', 'value': ''},
        {'key': 'rotor_diameter', 'display_type': 'numeric', 'display_name': 'Rotor Diameter', 'value': ''},
        {'key': 'rotation', 'display_type': 'numeric', 'display_name': 'Rotation', 'value': ''},
        {'key': 'cut_in_speed', 'display_type': 'numeric', 'display_name': 'Cut-in Speed', 'value': ''},
        {'key': 'rated_speed', 'display_type': 'numeric', 'display_name': 'Rated Speed', 'value': ''},
        {'key': 'cut_off_speed', 'display_type': 'numeric', 'display_name': 'Cut-off Speed', 'value': ''}
    ]
}

propertyInfoMap = {
    ObjectType.SolarPanel: solar_panel_properties,
    ObjectType.LithiumIon: lithium_ion_battery_properties,
    ObjectType.WindTurbine: wind_turbine_properties
}

def get_object_configuration(type):
    return copy.deepcopy(propertyInfoMap.get(type, solar_panel_properties))
