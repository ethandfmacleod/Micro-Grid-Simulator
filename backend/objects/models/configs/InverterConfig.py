from app.Enums.ModelEnums import CalculationMode

inverter_config = {
    "calculation_mode": CalculationMode.InverterEfficiency,
    "propertySets": [
        {
            "name": CalculationMode.Outputs,
            "formulas": [
                {
                    "output_property": "total_energy",
                    "formula_expression": "energy_produced * efficiency",
                },
            ],
            "properties": [
                {
                    "key": "minimum_size",
                    "shared": True,
                    "model": "home",
                    "set": "Outputs",
                },
                {
                    "key": "total_energy",
                    "display_type": "numeric",
                    "display_name": "Usable Energy (kWh)",
                    "value": "",
                    "disabled": True,
                },
            ],
        },
        {
            "name": CalculationMode.InverterEfficiency,
            "properties": [
                {
                    "key": "efficiency",
                    "display_type": "numeric",
                    "display_name": "Efficiency (%)",
                    "value": 95,
                    "defined": True
                },
            ]
        }
    ]
}