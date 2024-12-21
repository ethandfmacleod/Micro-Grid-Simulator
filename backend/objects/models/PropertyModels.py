from django.db import models
from app.Enums.ModelEnums import DisplayType

class PropertySet(models.Model):
    name = models.CharField(max_length=64, default="Property Set")
    node = models.ForeignKey("Node", on_delete=models.CASCADE, related_name='property_sets')

class PropertyInfo(models.Model):
    set = models.ForeignKey("PropertySet", on_delete=models.CASCADE, related_name="properties")
    display_type = models.CharField(choices=DisplayType.choices, default=DisplayType.numeric)
    value = models.JSONField(null=True, blank=True)
    key = models.CharField(max_length=64)
    display_name = models.CharField(max_length=64)
    disabled = models.BooleanField(default=False)

    class Meta:
        ordering = ['pk']
