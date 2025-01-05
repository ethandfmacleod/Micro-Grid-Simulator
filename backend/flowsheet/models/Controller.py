from django.db import models
from flowsheet.models.WeatherData import WeatherData

class Controller(models.Model):
    total_energy = models.FloatField(null=True, blank=True)
    total_emissions = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(default=-37.719408)
    longitude = models.FloatField(default=175.248599)
    weather = models.ForeignKey(WeatherData, on_delete=models.CASCADE, related_name='weather_controller')
    grid_emission_factor = models.FloatField(default=0.120)

    @classmethod
    def create(cls):
        weather_data = WeatherData.create()
        instance = Controller.objects.create(weather=weather_data)
        instance.save()
        return instance