from app.Enums.ModelEnums import CalculationMode, ObjectType

inverter_config = {
    "calculation_mode": CalculationMode.Outputs,
    "propertySets": [
        {
            "name": CalculationMode.Outputs,
            "properties": [
                {
                    "key": "minimum_size",
                    "shared": True,
                    "model": "home",
                    "set": "Outputs",
                },
            ],
        }
    ]
}