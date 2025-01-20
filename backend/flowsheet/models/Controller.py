from typing import List
from django.db import models
from app.Enums.ModelEnums import ObjectType
from flowsheet.models.WeatherData import WeatherData

class Controller(models.Model):
    energy_produced = models.FloatField(null=True, blank=True)
    energy_required = models.FloatField(null=True, blank=True)
    total_emissions = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(default=-37.719408)
    longitude = models.FloatField(default=175.248599)
    weather = models.OneToOneField(WeatherData, on_delete=models.CASCADE, related_name='weather_controller')
    grid_emission_factor = models.FloatField(default=0.120)

    @classmethod
    def create(cls):
        weather_data = WeatherData.create()
        instance = Controller.objects.create(weather=weather_data)
        instance.save()
        return instance
    
    def recalculate_energy_ins(self):
        valid_nodes = [ObjectType.SolarPanel, ObjectType.WindTurbine, ObjectType.Home]
        for node in self.controller_project.project_nodes.all():
            if node.type in valid_nodes:
                node.calculate_outputs()