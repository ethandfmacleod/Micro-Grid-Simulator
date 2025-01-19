from app.Enums.ModelEnums import CalculationMode, ObjectType

inverter_config = {
    "calculation_mode": CalculationMode.BatteryManagement,
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