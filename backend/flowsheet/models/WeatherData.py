from django.db import models
import requests
from datetime import date
from os import getenv
from app.Enums.APIEnums import Sky, TimeFrame

API_KEY = getenv("WEATHER_API_KEY")
BASE_URL = getenv("WEATHER_BASE_URL")

class WeatherData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    timeframe = models.CharField(choices=TimeFrame.choices, default=TimeFrame.Current)
    sky = models.CharField(choices=Sky.choices, default=Sky.Clear)
    location = models.CharField(max_length=255)
    irradiance = models.FloatField(null=True, blank=True)
    temperature = models.FloatField(null=True, blank=True)
    wind_speed = models.FloatField(null=True, blank=True)
    humidity = models.FloatField(null=True, blank=True)

    @classmethod
    def create(cls, lat=-37.719408, lon=175.248599):
        instance = WeatherData.objects.create(location="Undefined")
        instance.save()
        instance.update_weather_data(lat, lon)
        return instance

    def update_weather_data(self, lat, lon):
        """
        Retrieves current data from OpenWeatherMap
        https://openweathermap.org/api
        :param: lat: latitude
        :param: lon: longitude
        """
        exclude_blocks = [t[0] for t in TimeFrame.choices if t[0] != self.timeframe]
        exclude_blocks.append("alerts")
        try:
            params = {
                "lat": lat,
                "lon": lon,
                "appid": API_KEY,
                "units": "metric",
                "exclude": ",".join(exclude_blocks),
            }
            response = requests.get(BASE_URL, params=params)
            if response.status_code == 200:
                data = response.json()
                self.location = f"{lat},{lon}"
                self.temperature = data.get(self.timeframe).get("temp")
                self.wind_speed = data.get(self.timeframe).get("wind_speed")
                self.humidity = data.get(self.timeframe).get("humidity")
                self.save()
            else:
                raise Exception(f"Failed to fetch weather data: {response.status_code}")
        except Exception as e:
            return str(e)

    def __str__(self):
        return (
            f"WeatherData for {self.location} at {self.timestamp}:\n"
            f"Date: {self.date}, Solar Timeframe: {self.solar_timeframe}, Sky Condition: {self.sky}\n"
            f"Temperature: {self.temperature}°C, "
            f"Humidity: {self.humidity}%, "
            f"Wind Speed: {self.wind_speed} m/s\n"
            f"Irradiance GHI: {self.irradiance_ghi} W/m², "
            f"Irradiance DNI: {self.irradiance_dni} W/m², "
            f"Irradiance DHI: {self.irradiance_dhi} W/m²\n"
            f"Sunrise: {self.sunrise}, Sunset: {self.sunset}"
        )
