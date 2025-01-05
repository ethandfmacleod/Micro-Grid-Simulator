from app.Enums.ModelEnums import CalculationMode


solar_config = {
    "calculation_mode": CalculationMode.SolarPeakSunlightHours,
    "propertySets": [
        {
            "name": CalculationMode.Outputs,
            "formulas": [
                {
                    "output_property": "emissions_offset",
                    "formula_expression": "(daily_energy * grid_emission_factor) * 365",
                }
            ],
            "properties": [
                {
                    "key": "daily_energy",
                    "display_type": "numeric",
                    "display_name": "Daily Energy (kWh)",
                    "value": "",
                    "disabled": True,
                },
                {
                    "key": "emissions_offset",
                    "display_type": "numeric",
                    "display_name": "Co2 Offset (kgCO₂e / year)",
                    "value": "",
                    "disabled": True,
                },
            ],
        },
        {
            "name": CalculationMode.SolarPeakSunlightHours,
            "formulas": [
                {
                    "output_property": "daily_energy",
                    "formula_expression": "(watts * hours * (efficiency / 100)) / 1000",
                },
            ],
            "properties": [
                {
                    "key": "watts",
                    "display_type": "numeric",
                    "display_name": "Watts (W)",
                    "value": "",
                },
                {
                    "key": "hours",
                    "display_type": "numeric",
                    "display_name": "Peak Sunlight Hours (hrs)",
                    "value": 4,
                    "defined": True,
                },
                {
                    "key": "efficiency",
                    "display_type": "numeric",
                    "display_name": "Efficiency (%)",
                    "value": 20.0,
                    "defined": True,
                },
            ],
        },
        {
            "name": CalculationMode.SolarPowerBased,
            "formulas": [
                {
                    "output_property": "daily_energy",
                    "formula_expression": "watts * irradiance / 1000",
                },
            ],
            "properties": [
                {
                    "key": "watts",
                    "display_type": "numeric",
                    "display_name": "Watts (W)",
                    "value": "",
                },
                {
                    "key": "irradiance",
                    "display_type": "numeric",
                    "display_name": "Irradiance (W/m²)",
                    "value": "",
                },
            ],
        },
        {
            "name": CalculationMode.SolarElectrical,
            "formulas": [
                {
                    "output_property": "daily_energy",
                    "formula_expression": "(voltage * current * fill_factor * irradiance) / 1000",
                },
            ],
            "properties": [
                {
                    "key": "voltage",
                    "display_type": "numeric",
                    "display_name": "Voltage (V)",
                    "value": "",
                },
                {
                    "key": "current",
                    "display_type": "numeric",
                    "display_name": "Current (A)",
                    "value": "",
                },
                {
                    "key": "irradiance",
                    "display_type": "numeric",
                    "display_name": "Irradiance (W/m²)",
                    "value": "",
                },
                {
                    "key": "fill_factor",
                    "display_type": "numeric",
                    "display_name": "Fill Factor",
                    "value": 0.75,
                    "defined": True,
                },
            ],
        },
        {
            "name": CalculationMode.SolarPhysical,
            "formulas": [
                {
                    "output_property": "daily_energy",
                    "formula_expression": "(length * width * irradiance * efficiency) / 100",
                },
            ],
            "properties": [
                {
                    "key": "length",
                    "display_type": "numeric",
                    "display_name": "Length (m)",
                    "value": "",
                },
                {
                    "key": "width",
                    "display_type": "numeric",
                    "display_name": "Width (m)",
                    "value": "",
                },
                {
                    "key": "efficiency",
                    "display_type": "numeric",
                    "display_name": "Efficiency (%)",
                    "value": 20.0,
                    "defined": True,
                },
                {
                    "key": "irradiance",
                    "display_type": "numeric",
                    "display_name": "Irradiance (W/m²)",
                    "value": "",
                },
            ],
        },
        {
            "name": CalculationMode.Advanced,
            "properties": [
                {
                    "key": "watts",
                    "display_type": "numeric",
                    "display_name": "Watts",
                    "value": "",
                },
                {
                    "key": "voltage",
                    "display_type": "numeric",
                    "display_name": "Voltage",
                    "value": "",
                },
                {
                    "key": "current",
                    "display_type": "numeric",
                    "display_name": "Current",
                    "value": "",
                },
                {
                    "key": "fill_factor",
                    "display_type": "numeric",
                    "display_name": "Fill Factor",
                    "value": 0.75,
                },
                {
                    "key": "length",
                    "display_type": "numeric",
                    "display_name": "Length (m)",
                    "value": "",
                },
                {
                    "key": "width",
                    "display_type": "numeric",
                    "display_name": "Width (m)",
                    "value": "",
                },
                {
                    "key": "efficiency",
                    "display_type": "numeric",
                    "display_name": "Efficiency (%)",
                    "value": 20.0,
                },
                {
                    "key": "irradiance",
                    "display_type": "numeric",
                    "display_name": "Irradiance",
                    "value": "",
                },
                {
                    "key": "ambient_temp",
                    "display_type": "numeric",
                    "display_name": "Ambient Temperature (°C)",
                    "value": 25,
                },
                {
                    "key": "tilt_angle",
                    "display_type": "numeric",
                    "display_name": "Tilt Angle (°)",
                    "value": 30,
                },
                {
                    "key": "degradation_rate",
                    "display_type": "numeric",
                    "display_name": "Degradation Rate (%)",
                    "value": 0.5,
                },
                {
                    "key": "temperature_coefficient",
                    "display_type": "numeric",
                    "display_name": "Temperature Coefficient (%/°C)",
                    "value": -0.3,
                },
                {
                    "key": "reflectance_loss",
                    "display_type": "numeric",
                    "display_name": "Reflectance Loss (%)",
                    "value": 3,
                },
            ],
        },
    ],
}
