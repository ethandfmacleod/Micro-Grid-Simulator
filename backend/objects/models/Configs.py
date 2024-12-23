import copy
from app.Enums.ModelEnums import ObjectType, CalculationMode

solar_panel_properties = {
    'calculation_mode': CalculationMode.SolarPeakSunlightHours,
    'propertySets': [
        {
            'name': CalculationMode.Outputs,
            'properties': [
                {'key': 'daily_energy', 'display_type': 'numeric', 'display_name': 'Daily Energy (kWh)', 'value': '', 'disabled': True},
                # {'key': 'emmisions_offset', 'display_type': 'numeric', 'display_name': 'Co2 Offset', 'value': '', 'disabled': True},
            ]
        },
        {
            'name': CalculationMode.SolarPeakSunlightHours,
            'formula': '(watts * hours * (efficiency / 100)) / 1000',
            'properties': [
                {'key': 'watts', 'display_type': 'numeric', 'display_name': 'Watts (W)', 'value': ''},
                {'key': 'hours', 'display_type': 'numeric', 'display_name': 'Peak Sunlight Hours (hrs)', 'value': 4, 'defined': True},
                {'key': 'efficiency', 'display_type': 'numeric', 'display_name': 'Efficiency (%)', 'value': 20.0, 'defined': True},
            ]
        },
        {
            'name': CalculationMode.SolarPowerBased,
            'formula': 'watts * irradiance / 1000',
            'properties': [
                {'key': 'watts', 'display_type': 'numeric', 'display_name': 'Watts (W)', 'value': ''},
                {'key': 'irradiance', 'display_type': 'numeric', 'display_name': 'Irradiance (W/m²)', 'value': ''},
            ]
        },
        {
            'name': CalculationMode.SolarElectrical,
            'formula': '(voltage * current * fill_factor * irradiance) / 1000',
            'properties': [
                {'key': 'voltage', 'display_type': 'numeric', 'display_name': 'Voltage (V)', 'value': ''},
                {'key': 'current', 'display_type': 'numeric', 'display_name': 'Current (A)', 'value': ''},
                {'key': 'irradiance', 'display_type': 'numeric', 'display_name': 'Irradiance (W/m²)', 'value': ''},
                {'key': 'fill_factor', 'display_type': 'numeric', 'display_name': 'Fill Factor', 'value': 0.75, 'defined': True},
            ]
        },
        {
            'name': CalculationMode.SolarPhysical,
            'formula': '(length * width * irradiance * efficiency) / 100',
            'properties': [
                {'key': 'length', 'display_type': 'numeric', 'display_name': 'Length (m)', 'value': ''},
                {'key': 'width', 'display_type': 'numeric', 'display_name': 'Width (m)', 'value': ''},
                {'key': 'efficiency', 'display_type': 'numeric', 'display_name': 'Efficiency (%)', 'value': 20.0, 'defined': True},
                {'key': 'irradiance', 'display_type': 'numeric', 'display_name': 'Irradiance (W/m²)', 'value': ''},
            ]
        },
        {
            'name': CalculationMode.Advanced,
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
    'calculation_mode': CalculationMode.WindPowerOutput,
    'propertySets': [
        {
            'name': CalculationMode.Outputs,
            'properties': [
                {'key': 'daily_energy', 'display_type': 'numeric', 'display_name': 'Daily Energy (kWh)', 'value': '', 'disabled': True},
            ]
        },
        {
            'name': CalculationMode.WindPowerOutput,
            'formula': '0.5 * air_density * swept_area * wind_speed**3 * efficiency / 1000',
            'properties': [
                {'key': 'air_density', 'display_type': 'numeric', 'display_name': 'Air Density (kg/m³)', 'value': 1.225, 'defined': True},  # Default for sea level
                {'key': 'swept_area', 'display_type': 'numeric', 'display_name': 'Swept Area (m²)', 'value': ''},
                {'key': 'wind_speed', 'display_type': 'numeric', 'display_name': 'Wind Speed (m/s)', 'value': ''},
                {'key': 'efficiency', 'display_type': 'numeric', 'display_name': 'Efficiency (%)', 'value': 30.0, 'defined': True},  # Default value
            ]
        },
        {
            'name': CalculationMode.WindRotorBased,
            'formula': '(rotor_diameter**2 * pi / 4) * wind_speed**3 * capacity_factor / 1000',
            'properties': [
                {'key': 'rotor_diameter', 'display_type': 'numeric', 'display_name': 'Rotor Diameter (m)', 'value': ''},
                {'key': 'wind_speed', 'display_type': 'numeric', 'display_name': 'Wind Speed (m/s)', 'value': ''},
                {'key': 'capacity_factor', 'display_type': 'numeric', 'display_name': 'Capacity Factor (%)', 'value': 40.0, 'defined': True},  # Default value
            ]
        },
        {
            'name': CalculationMode.WindCutInCutOutSpeeds,
            'formula': '(0.5 * air_density * swept_area * wind_speed**3 * efficiency / 1000) if wind_speed > cut_in_speed and wind_speed < cut_out_speed else 0',
            'properties': [
                {'key': 'air_density', 'display_type': 'numeric', 'display_name': 'Air Density (kg/m³)', 'value': 1.225, 'defined': True},  # Default for sea level
                {'key': 'swept_area', 'display_type': 'numeric', 'display_name': 'Swept Area (m²)', 'value': ''},
                {'key': 'wind_speed', 'display_type': 'numeric', 'display_name': 'Wind Speed (m/s)', 'value': ''},
                {'key': 'cut_in_speed', 'display_type': 'numeric', 'display_name': 'Cut-In Speed (m/s)', 'value': 3.0, 'defined': True},
                {'key': 'cut_out_speed', 'display_type': 'numeric', 'display_name': 'Cut-Out Speed (m/s)', 'value': 25.0, 'defined': True},
                {'key': 'efficiency', 'display_type': 'numeric', 'display_name': 'Efficiency (%)', 'value': 30.0, 'defined': True},
            ]
        },
        {
            'name': CalculationMode.Advanced,
            'properties': [
                {'key': 'rotor_diameter', 'display_type': 'numeric', 'display_name': 'Rotor Diameter (m)', 'value': ''},
                {'key': 'wind_speed', 'display_type': 'numeric', 'display_name': 'Wind Speed (m/s)', 'value': ''},
                {'key': 'air_density', 'display_type': 'numeric', 'display_name': 'Air Density (kg/m³)', 'value': 1.225, 'defined': True},  # Default
                {'key': 'swept_area', 'display_type': 'numeric', 'display_name': 'Swept Area (m²)', 'value': ''},
                {'key': 'cut_in_speed', 'display_type': 'numeric', 'display_name': 'Cut-In Speed (m/s)', 'value': 3.0},
                {'key': 'cut_out_speed', 'display_type': 'numeric', 'display_name': 'Cut-Out Speed (m/s)', 'value': 25.0},
                {'key': 'capacity_factor', 'display_type': 'numeric', 'display_name': 'Capacity Factor (%)', 'value': 40.0},
                {'key': 'efficiency', 'display_type': 'numeric', 'display_name': 'Efficiency (%)', 'value': 30.0},
                {'key': 'annual_hours', 'display_type': 'numeric', 'display_name': 'Annual Operating Hours', 'value': 8760},  # Default for 1 year
            ]
        },
    ]
}

propertyInfoMap = {
    ObjectType.SolarPanel: solar_panel_properties,
    ObjectType.LithiumIon: lithium_ion_battery_properties,
    ObjectType.WindTurbine: wind_turbine_properties
}

def get_object_configuration(type):
    return copy.deepcopy(propertyInfoMap.get(type, solar_panel_properties))
