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
                {
                    "output_property": "minimum_size",
                    "formula_expression": "average_power_rating * number_of_appliances",
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
                {
                    "key": "appliance_energy", 
                    "display_type": "numeric",
                    "display_name": "Appliance Energy",
                    "value": 0,
                    "disabled": True,
                    "hidden": True
                },
                {
                    "key": "minimum_size",
                    "display_type": "numeric",
                    "display_name": "Minimum Inverter Size (W)",
                    "value": "",
                    "disabled": True,
                    "hidden": False,
                },
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
                    "display_type": "list",
                    "display_name": "Appliance List",
                    "value": [],
                },
            ],
        },
    ],
}
