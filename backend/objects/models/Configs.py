import copy
from app.Enums.ModelEnums import ObjectType, CalculationMode

solar_panel_properties = {
    'calculation_mode': CalculationMode.SolarPeakSunlightHours,
    'propertySets': [
        {
            'name': CalculationMode.Outputs,
            # TODO: user input grid emission factor
            'formulas': [
                {'output_property': 'emissions_offset', 'formula_expression': '(daily_energy * 0.120) * 365'}
            ],
            'properties': [
                {'key': 'daily_energy', 'display_type': 'numeric', 'display_name': 'Daily Energy (kWh)', 'value': '', 'disabled': True},
                {'key': 'emissions_offset', 'display_type': 'numeric', 'display_name': 'Co2 Offset (kgCO₂e / year)', 'value': '', 'disabled': True},
            ]
        },
        {
            'name': CalculationMode.SolarPeakSunlightHours,
            'formulas': [
                {'output_property': 'daily_energy', 'formula_expression': '(watts * hours * (efficiency / 100)) / 1000'},
            ],
            'properties': [
                {'key': 'watts', 'display_type': 'numeric', 'display_name': 'Watts (W)', 'value': ''},
                {'key': 'hours', 'display_type': 'numeric', 'display_name': 'Peak Sunlight Hours (hrs)', 'value': 4, 'defined': True},
                {'key': 'efficiency', 'display_type': 'numeric', 'display_name': 'Efficiency (%)', 'value': 20.0, 'defined': True},
            ]
        },
        {
            'name': CalculationMode.SolarPowerBased,
            'formulas': [
                {'output_property': 'daily_energy', 'formula_expression': 'watts * irradiance / 1000'},
            ],
            'properties': [
                {'key': 'watts', 'display_type': 'numeric', 'display_name': 'Watts (W)', 'value': ''},
                {'key': 'irradiance', 'display_type': 'numeric', 'display_name': 'Irradiance (W/m²)', 'value': ''},
            ]
        },
        {
            'name': CalculationMode.SolarElectrical,
            'formulas': [
                {'output_property': 'daily_energy', 'formula_expression': '(voltage * current * fill_factor * irradiance) / 1000'},
            ],
            'properties': [
                {'key': 'voltage', 'display_type': 'numeric', 'display_name': 'Voltage (V)', 'value': ''},
                {'key': 'current', 'display_type': 'numeric', 'display_name': 'Current (A)', 'value': ''},
                {'key': 'irradiance', 'display_type': 'numeric', 'display_name': 'Irradiance (W/m²)', 'value': ''},
                {'key': 'fill_factor', 'display_type': 'numeric', 'display_name': 'Fill Factor', 'value': 0.75, 'defined': True},
            ]
        },
        {
            'name': CalculationMode.SolarPhysical,
            'formulas': [
                {'output_property': 'daily_energy', 'formula_expression': '(length * width * irradiance * efficiency) / 100'},
            ],
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
    'calculation_mode': CalculationMode.SolarPeakSunlightHours,
    'propertySets': [
        {
            'name': CalculationMode.Outputs,
            'properties': [

            ]
        },
        {

        }
    ]
}

wind_turbine_properties = {
    'calculation_mode': CalculationMode.WindPowerOutput,
    'propertySets': [
        {
            'name': CalculationMode.Outputs,
            # TODO: user input grid emission factor
            'formulas': [
                {'output_property': 'emissions_offset', 'formula_expression': '(daily_energy * 0.120) * 365'}
            ],
            'properties': [
                {'key': 'daily_energy', 'display_type': 'numeric', 'display_name': 'Daily Energy (kWh)', 'value': '', 'disabled': True},
                {'key': 'emissions_offset', 'display_type': 'numeric', 'display_name': 'Co2 Offset (kgCO₂e / year)', 'value': '', 'disabled': True},
            ]
        },
        {
            'name': CalculationMode.WindPowerOutput,
            'formulas': [
                {'output_property': 'daily_energy', 'formula_expression': '0.5 * air_density * swept_area * wind_speed**3 * efficiency / 1000'},
            ],
            'properties': [
                {'key': 'air_density', 'display_type': 'numeric', 'display_name': 'Air Density (kg/m³)', 'value': 1.225, 'defined': True},  # Default for sea level
                {'key': 'swept_area', 'display_type': 'numeric', 'display_name': 'Swept Area (m²)', 'value': ''},
                {'key': 'wind_speed', 'display_type': 'numeric', 'display_name': 'Wind Speed (m/s)', 'value': ''},
                {'key': 'efficiency', 'display_type': 'numeric', 'display_name': 'Efficiency (%)', 'value': 30.0, 'defined': True},  # Default value
            ]
        },
        {
            'name': CalculationMode.WindRotorBased,
            'formulas': [
                {'output_property': 'daily_energy', 'formula_expression': '(rotor_diameter**2 * pi / 4) * wind_speed**3 * capacity_factor / 1000'},
            ],
            'properties': [
                {'key': 'rotor_diameter', 'display_type': 'numeric', 'display_name': 'Rotor Diameter (m)', 'value': ''},
                {'key': 'wind_speed', 'display_type': 'numeric', 'display_name': 'Wind Speed (m/s)', 'value': ''},
                {'key': 'capacity_factor', 'display_type': 'numeric', 'display_name': 'Capacity Factor (%)', 'value': 40.0, 'defined': True},  # Default value
            ]
        },
        {
            'name': CalculationMode.WindCutInCutOutSpeeds,
            'formulas': [
                {'output_property': 'daily_energy', 'formula_expression': '(0.5 * air_density * swept_area * wind_speed**3 * efficiency / 1000) if wind_speed > cut_in_speed and wind_speed < cut_out_speed else 0'},
            ],
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

home_properties = {
    'calculation_mode': CalculationMode.SimpleHome,
    'propertySets': [
        {
            'name': CalculationMode.Outputs,
            'formulas': [
                {'output_property': 'total_energy', 'formula_expression': 'appliance_energy * number_of_appliances'},
            ],
            'properties': [
                {'key': 'total_energy', 'display_type': 'numeric', 'display_name': 'Total Energy (kWh)', 'value': '', 'disabled': True},
                {'key': 'appliance_energy', 'value': 0, 'hidden': True}
            ]
        },
        {
            'name': CalculationMode.SimpleHome,
            'formulas': [
                {'output_property': 'appliance_energy', 'formula_expression': 'average_daily_usage * average_power_rating / 1000'},
            ],
            'properties': [
                {'key': 'number_of_appliances', 'display_type': 'numeric', 'display_name': 'Number of Appliances', 'value': ''},
                {'key': 'average_power_rating', 'display_type': 'numeric', 'display_name': 'Avg. Power Rating (W)', 'value': ''},
                {'key': 'average_daily_usage', 'display_type': 'numeric', 'display_name': 'Avg. Daily Usage (hrs)', 'value': ''},
                {'key': 'grid_emission_factor', 'display_type': 'numeric', 'display_name': 'Grid Emission Factor (kgCO₂e / kWh)', 'value': 0.120, 'defined': True},
            ]
        },
        {
            'name': CalculationMode.ComplexHome,
            'formulas': [
                {'output_property': 'appliance_energy', 'formula_expression': 'daily_usage * power_rating / 1000'},
            ],
            'properties': [
                {'key': 'appliance_list', 'display_type': 'json', 'display_name': 'Appliance List', 'value': '[]'},
            ]
        },
    ]
}

propertyInfoMap = {
    ObjectType.SolarPanel: solar_panel_properties,
    ObjectType.LithiumIon: lithium_ion_battery_properties,
    ObjectType.WindTurbine: wind_turbine_properties,
    ObjectType.Home: home_properties,
}

def get_object_configuration(type):
    return copy.deepcopy(propertyInfoMap.get(type, solar_panel_properties))
