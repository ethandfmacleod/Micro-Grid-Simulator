from app.Enums.ModelEnums import CalculationMode


wind_config = {
    "calculation_mode": CalculationMode.WindPowerOutput,
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
            "name": CalculationMode.WindPowerOutput,
            "formulas": [
                {
                    "output_property": "daily_energy",
                    "formula_expression": "0.5 * air_density * swept_area * wind_speed**3 * efficiency / 1000",
                },
            ],
            "properties": [
                {
                    "key": "air_density",
                    "display_type": "numeric",
                    "display_name": "Air Density (kg/m³)",
                    "value": 1.225,
                    "defined": True,
                },
                {
                    "key": "swept_area",
                    "display_type": "numeric",
                    "display_name": "Swept Area (m²)",
                    "value": "",
                },
                {
                    "key": "wind_speed",
                    "weather": True
                },
                {
                    "key": "efficiency",
                    "display_type": "numeric",
                    "display_name": "Efficiency (%)",
                    "value": 30.0,
                    "defined": True,
                },
            ],
        },
        {
            "name": CalculationMode.WindRotorBased,
            "formulas": [
                {
                    "output_property": "daily_energy",
                    "formula_expression": "(rotor_diameter**2 * pi / 4) * wind_speed**3 * capacity_factor / 1000",
                },
            ],
            "properties": [
                {
                    "key": "rotor_diameter",
                    "display_type": "numeric",
                    "display_name": "Rotor Diameter (m)",
                    "value": "",
                },
                {
                    "key": "wind_speed",
                    "weather": True
                },
                {
                    "key": "capacity_factor",
                    "display_type": "numeric",
                    "display_name": "Capacity Factor (%)",
                    "value": 40.0,
                    "defined": True,
                },
            ],
        },
        {
            "name": CalculationMode.WindCutInCutOutSpeeds,
            "formulas": [
                {
                    "output_property": "daily_energy",
                    "formula_expression": "(0.5 * air_density * swept_area * wind_speed**3 * efficiency / 1000) if wind_speed > cut_in_speed and wind_speed < cut_out_speed else 0",
                },
            ],
            "properties": [
                {
                    "key": "air_density",
                    "display_type": "numeric",
                    "display_name": "Air Density (kg/m³)",
                    "value": 1.225,
                    "defined": True,
                },
                {
                    "key": "swept_area",
                    "display_type": "numeric",
                    "display_name": "Swept Area (m²)",
                    "value": "",
                },
                {
                    "key": "wind_speed",
                    "weather": True
                },
                {
                    "key": "cut_in_speed",
                    "display_type": "numeric",
                    "display_name": "Cut-In Speed (m/s)",
                    "value": 3.0,
                    "defined": True,
                },
                {
                    "key": "cut_out_speed",
                    "display_type": "numeric",
                    "display_name": "Cut-Out Speed (m/s)",
                    "value": 25.0,
                    "defined": True,
                },
                {
                    "key": "efficiency",
                    "display_type": "numeric",
                    "display_name": "Efficiency (%)",
                    "value": 30.0,
                    "defined": True,
                },
            ],
        },
        {
            "name": CalculationMode.Advanced,
            "properties": [
                {
                    "key": "rotor_diameter",
                    "display_type": "numeric",
                    "display_name": "Rotor Diameter (m)",
                    "value": "",
                },
                {
                    "key": "wind_speed",
                    "weather": True
                },
                {
                    "key": "air_density",
                    "display_type": "numeric",
                    "display_name": "Air Density (kg/m³)",
                    "value": 1.225,
                    "defined": True,
                },
                {
                    "key": "swept_area",
                    "display_type": "numeric",
                    "display_name": "Swept Area (m²)",
                    "value": "",
                },
                {
                    "key": "cut_in_speed",
                    "display_type": "numeric",
                    "display_name": "Cut-In Speed (m/s)",
                    "value": 3.0,
                },
                {
                    "key": "cut_out_speed",
                    "display_type": "numeric",
                    "display_name": "Cut-Out Speed (m/s)",
                    "value": 25.0,
                },
                {
                    "key": "capacity_factor",
                    "display_type": "numeric",
                    "display_name": "Capacity Factor (%)",
                    "value": 40.0,
                },
                {
                    "key": "efficiency",
                    "display_type": "numeric",
                    "display_name": "Efficiency (%)",
                    "value": 30.0,
                },
                {
                    "key": "annual_hours",
                    "display_type": "numeric",
                    "display_name": "Annual Operating Hours",
                    "value": 8760,
                },
            ],
        },
    ],
}
