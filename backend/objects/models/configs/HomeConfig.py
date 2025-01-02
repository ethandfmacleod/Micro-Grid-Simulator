from app.Enums.ModelEnums import CalculationMode


home_config = {
    "calculation_mode": CalculationMode.SimpleHome,
    "propertySets": [
        {
            "name": CalculationMode.Outputs,
            "formulas": [
                {
                    "output_property": "total_energy",
                    "formula_expression": "appliance_energy * number_of_appliances",
                },
            ],
            "properties": [
                {
                    "key": "total_energy",
                    "display_type": "numeric",
                    "display_name": "Total Energy (kWh)",
                    "value": "",
                    "disabled": True,
                },
                {"key": "appliance_energy", "value": 0, "hidden": True},
            ],
        },
        {
            "name": CalculationMode.SimpleHome,
            "formulas": [
                {
                    "output_property": "appliance_energy",
                    "formula_expression": "average_daily_usage * average_power_rating / 1000",
                },
            ],
            "properties": [
                {
                    "key": "number_of_appliances",
                    "display_type": "numeric",
                    "display_name": "Number of Appliances",
                    "value": "",
                },
                {
                    "key": "average_power_rating",
                    "display_type": "numeric",
                    "display_name": "Avg. Power Rating (W)",
                    "value": "",
                },
                {
                    "key": "average_daily_usage",
                    "display_type": "numeric",
                    "display_name": "Avg. Daily Usage (hrs)",
                    "value": "",
                },
                {
                    "key": "grid_emission_factor",
                    "display_type": "numeric",
                    "display_name": "Grid Emission Factor (kgCO₂e / kWh)",
                    "value": 0.120,
                    "defined": True,
                },
            ],
        },
        {
            "name": CalculationMode.ComplexHome,
            "formulas": [
                {
                    "output_property": "appliance_energy",
                    "formula_expression": "daily_usage * power_rating / 1000",
                },
            ],
            "properties": [
                {
                    "key": "appliance_list",
                    "display_type": "json",
                    "display_name": "Appliance List",
                    "value": "[]",
                },
            ],
        },
    ],
}
