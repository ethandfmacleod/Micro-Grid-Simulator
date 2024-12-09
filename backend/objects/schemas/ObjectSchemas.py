from ninja import ModelSchema, Schema
from typing import Optional
from objects.models import (
    EnergyIn,
    EnergyOut,
    EnergyStorageUnit,
    LithiumIonBattery,
    SolarPanel,
    WindTurbine,
)

# EnergyIn Schemas
class EnergyInSchema(ModelSchema):
    class Meta:
        model = EnergyIn
        fields = "__all__"

class EnergyInPatchSchema(ModelSchema):
    class Meta:
        model = EnergyIn
        fields = ["watts", "price", "daily_emissions", "type"]
        fields_optional = ["watts", "price", "daily_emissions", "type"]

class EnergyInCreateSchema(Schema):
    watts: int
    price: float
    daily_emissions: int
    type: Optional[str] = None

# EnergyOut Schemas
class EnergyOutSchema(ModelSchema):
    class Meta:
        model = EnergyOut
        fields = "__all__"

class EnergyOutPatchSchema(ModelSchema):
    class Meta:
        model = EnergyOut
        fields = ["watts", "daily_emissions", "type"]
        fields_optional = ["watts", "daily_emissions", "type"]

class EnergyOutCreateSchema(Schema):
    watts: int
    daily_emissions: int
    type: Optional[str] = None

# EnergyStorageUnit Schemas
class EnergyStorageUnitSchema(ModelSchema):
    class Meta:
        model = EnergyStorageUnit
        fields = "__all__"

class EnergyStorageUnitPatchSchema(ModelSchema):
    class Meta:
        model = EnergyStorageUnit
        fields = ["capacity", "charge_level", "price", "type"]
        fields_optional = ["capacity", "charge_level", "price", "type"]

class EnergyStorageUnitCreateSchema(Schema):
    capacity: float
    charge_level: float
    price: float
    type: Optional[str] = None

# LithiumIonBattery Schemas
class LithiumIonBatterySchema(ModelSchema):
    class Meta:
        model = LithiumIonBattery
        fields = "__all__"

class LithiumIonBatteryPatchSchema(ModelSchema):
    class Meta:
        model = LithiumIonBattery
        fields = ["max_charge_rate", "efficiency", "current", "voltage", "charge_level"]
        fields_optional = ["max_charge_rate", "efficiency", "current", "voltage", "charge_level"]

class LithiumIonBatteryCreateSchema(Schema):
    max_charge_rate: float
    efficiency: float
    current: int
    voltage: int
    charge_level: float

# SolarPanel Schemas
class SolarPanelSchema(ModelSchema):
    class Meta:
        model = SolarPanel
        fields = "__all__"

class SolarPanelPatchSchema(ModelSchema):
    class Meta:
        model = SolarPanel
        fields = ["width", "length", "cells", "panel_type", "material"]
        fields_optional = ["width", "length", "cells", "panel_type", "material"]

class SolarPanelCreateSchema(Schema):
    width: float
    length: float
    cells: int
    panel_type: Optional[str] = None
    material: Optional[str] = None

# WindTurbine Schemas
class WindTurbineSchema(ModelSchema):
    class Meta:
        model = WindTurbine
        fields = "__all__"

class WindTurbinePatchSchema(ModelSchema):
    class Meta:
        model = WindTurbine
        fields = ["rotor_diameter", "rotation", "cut_in_speed", "rated_speed", "cut_off_speed"]
        fields_optional = ["rotor_diameter", "rotation", "cut_in_speed", "rated_speed", "cut_off_speed"]

class WindTurbineCreateSchema(Schema):
    rotor_diameter: int
    rotation: int
    cut_in_speed: int
    rated_speed: int
    cut_off_speed: int
