from sqlalchemy import Column, Integer, Float, ForeignKey, Enum
from app.models.EnergyIn import EnergyIn
from app.enums.ModelEnums import EnergyInType, SolarPanelMaterial, SolarPanelType


class SolarPanel(EnergyIn):
    __tablename__ = "SolarPanels"
    
    id = Column(Integer, ForeignKey('EnergyIns.id'), primary_key=True)
    panel_type = Column(Enum(SolarPanelType), default=SolarPanelType.Default)
    width = Column(Float, nullable=False, default=0)
    length = Column(Float, nullable=False, default=0)
    cells = Column(Integer, nullable=False, default=0)
    material = Column(Enum(SolarPanelMaterial), default=SolarPanelMaterial.Default)

    __mapper_args__ = {
        "polymorphic_identity": EnergyInType.SolarPanel,
    }