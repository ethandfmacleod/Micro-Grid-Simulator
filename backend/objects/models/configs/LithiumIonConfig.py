from app.Enums.ModelEnums import CalculationMode

lithium_ion_config = {
    "calculation_mode": CalculationMode.BatteryManagement,
    "propertySets": [
        {
            "name": CalculationMode.Outputs,
            "formulas": [
                {
                    "output_property": "usable_energy",
                    "formula_expression": "min(max(capacity * (state_of_charge / 100), 0), capacity)",
                },
                {
                    "output_property": "state_of_charge",
                    "formula_expression": "max(min(((energy_in - energy_out) / capacity) * 100 + initial_state_of_charge, 100), 0)",
                },
                {
                    "output_property": "energy_stored",
                    "formula_expression": "min(max(energy_in - energy_out, 0), capacity)",
                },
            ],
            "properties": [
                {
                    "key": "usable_energy",
                    "display_type": "numeric",
                    "display_name": "Usable Energy (kWh)",
                    "value": "",
                    "disabled": True,
                },
                {
                    "key": "state_of_charge",
                    "display_type": "numeric",
                    "display_name": "State of Charge (%)",
                    "value": 100,  # Default: Fully charged
                    "disabled": True,
                },
                {
                    "key": "energy_stored",
                    "display_type": "numeric",
                    "display_name": "Energy Stored (kWh)",
                    "value": "",
                    "disabled": True,
                },
            ],
        },
        {
            "name": CalculationMode.BatteryManagement,
            "formulas": [
                {
                    "output_property": "capacity",
                    "formula_expression": "nominal_voltage * amp_hours / 1000",
                },
            ],
            "properties": [
                {
                    "key": "nominal_voltage",
                    "display_type": "numeric",
                    "display_name": "Nominal Voltage (V)",
                    "value": 48,
                    "defined": True
                },
                {
                    "key": "amp_hours",
                    "display_type": "numeric",
                    "display_name": "Battery Capacity (kWh)",
                    "value": 100,
                    "defined": True
                },
                {
                    "key": "energy_in",
                    "display_type": "numeric",
                    "display_name": "Energy In (kWh)",
                    "value": 0,
                },
                {
                    "key": "energy_out",
                    "display_type": "numeric",
                    "display_name": "Energy Out (kWh)",
                    "value": 0,  # Energy consumption
                },
                {
                    "key": "initial_state_of_charge",
                    "display_type": "numeric",
                    "display_name": "Initial State of Charge (%)",
                    "value": 100,
                    "defined": True
                },
            ],
        },
        {
            "name": CalculationMode.BatteryPerformance,
            "formulas": [
                {
                    "output_property": "charge_energy",
                    "formula_expression": "min(max((charge_rate * charge_time) * round_trip_efficiency / 100, 0), capacity)",
                },
                {
                    "output_property": "discharge_energy",
                    "formula_expression": "min(max((discharge_rate * discharge_time) * round_trip_efficiency / 100, 0), energy_stored)",
                },
            ],
            "properties": [
                {
                    "key": "charge_rate",
                    "display_type": "numeric",
                    "display_name": "Charge Rate (kW)",
                    "value": "",
                },
                {
                    "key": "charge_time",
                    "display_type": "numeric",
                    "display_name": "Charge Time (hours)",
                    "value": "",
                },
                {
                    "key": "discharge_rate",
                    "display_type": "numeric",
                    "display_name": "Discharge Rate (kW)",
                    "value": "",
                },
                {
                    "key": "discharge_time",
                    "display_type": "numeric",
                    "display_name": "Discharge Time (hours)",
                    "value": "",
                },
                {
                    "key": "round_trip_efficiency",
                    "display_type": "numeric",
                    "display_name": "Round Trip Efficiency (%)",
                    "value": 90,
                    "defined": True
                },
            ],
        },
    ],
}
