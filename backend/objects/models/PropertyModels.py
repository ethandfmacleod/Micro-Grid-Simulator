from typing import List
from django.db import models
from app.Enums.ModelEnums import DisplayType

class PropertyInfo(models.Model):
    set = models.ForeignKey("PropertySet", on_delete=models.CASCADE, related_name="properties")
    display_type = models.CharField(choices=DisplayType.choices, default=DisplayType.numeric)
    value = models.JSONField(null=True, blank=True)
    key = models.CharField(max_length=64)
    display_name = models.CharField(max_length=64, default="Unnamed")
    disabled = models.BooleanField(default=False)
    defined = models.BooleanField(default=False)
    hidden = models.BooleanField(default=False)

    class Meta:
        ordering = ['pk']

class Formula(models.Model):
    property_set = models.ForeignKey("PropertySet", on_delete=models.CASCADE, related_name="formulas")
    output_property = models.CharField(max_length=64)
    formula_expression = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.output_property}: {self.formula_expression}"
    
class PropertySet(models.Model):
    name = models.CharField(max_length=64, default="Property Set")
    node = models.ForeignKey("Node", on_delete=models.CASCADE, related_name='property_sets')

    def get_property(self, property_key) -> PropertyInfo:
        try:
            return self.properties.get(key=property_key)
        except PropertyInfo.DoesNotExist:
            print(f"PropertyInfo with key '{property_key}' does not exist in PropertySet '{self.name}'")
            raise
    
    def get_formulas(self) -> List[Formula]:
        return self.formulas.all()

