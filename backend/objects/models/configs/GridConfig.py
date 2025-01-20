from app.Enums.ModelEnums import CalculationMode

grid_config = {
    "calculation_mode": CalculationMode.GridUsage,
    "propertySets": [
        {
            "name": CalculationMode.Outputs,
            "formulas": [
                {
                    "output_property": "total_power_required",
                    "formula_expression": "energy_required - energy_produced"
                },
                {
                    "output_property": "total_cost",
                    "formula_expression": "total_power_required * power_cost",
                },
                {
                    "output_property": "total_co2",
                    "formula_expression": "total_power_required * grid_emission_factor",
                },
            ],
            "properties": [
                {
                    "key": "total_power_required",
                    "display_type": "numeric",
                    "display_name": "Total Power Required (kWh)",
                    "value": "",
                    "disabled": True,
                },
                {
                    "key": "total_cost",
                    "display_type": "numeric",
                    "display_name": "Total Cost ($)",
                    "value": "",
                    "disabled": True,
                },
                {
                    "key": "total_co2",
                    "display_type": "numeric",
                    "display_name": "Total CO₂ Generated (kgCO₂e / year)",
                    "value": "",
                    "disabled": True,
                }
            ],
        },
        {
            "name": CalculationMode.GridUsage,
            "formulas": [],
            "properties": [
                {
                    "key": "power_cost",
                    "display_type": "numeric",
                    "display_name": "Cost of Power ($/kWh)",
                    "value": "",
                },
            ],
        },
    ],
}
