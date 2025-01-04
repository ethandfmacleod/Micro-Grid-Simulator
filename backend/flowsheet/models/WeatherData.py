from django.db import models
import requests
from os import getenv

API_KEY = getenv("WEATHER_API_KEY")
BASE_URL = getenv("WEATHER_BASE_URL")

class WeatherData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=255)
    irradiance = models.FloatField(null=True, blank=True)
    temperature = models.FloatField(null=True, blank=True)
    wind_speed = models.FloatField(null=True, blank=True)
    humidity = models.FloatField(null=True, blank=True)

    @classmethod
    def create(self, lat, lon):

        params = {
            "lat": lat,
            "lon": lon,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(BASE_URL, params=params)
        print(response)
        print(response.json())
        if response.status_code == 200:
            data = response.json()
            weather = WeatherData.objects.create(
                location=f"{lat},{lon}",
                irradiance=data.get("clouds", {}).get("all", 0) * 10,
                temperature=data.get("main", {}).get("temp"),
                wind_speed=data.get("wind", {}).get("speed"),
                humidity=data.get("main", {}).get("humidity"),
            )
            weather.save()
            print(weather)
            return weather
        else:
            raise Exception(f"Failed to fetch weather data: {response.status_code}")
