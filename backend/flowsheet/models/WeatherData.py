from django.db import models
import requests
from os import getenv
from app.Enums.APIEnums import Sky, TimeFrame
from objects.models.PropertyModels import PropertyInfo

API_KEY = getenv("WEATHER_API_KEY")
BASE_URL = getenv("WEATHER_BASE_URL")
WEATHER_DATA_PROPERTIES = {
    "irradiance": {"key": "irradiance", "display_type": "numeric", "display_name": "Irradiance (W/m²)", "value": 1000, "disabled": True, "defined": True},
    "temperature": {"key": "temperature", "display_type": "numeric", "display_name": "Temperature (°C)", "value": "", "disabled": True,  "defined": True},
    "wind_speed": {"key": "wind_speed", "display_type": "numeric", "display_name": "Wind Speed (m/s)", "value": "", "disabled": True,  "defined": True},
    "humidity": {"key": "humidity", "display_type": "numeric", "display_name": "Humidity (%)", "value": "", "disabled": True,  "defined": True},
}

class WeatherData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    timeframe = models.CharField(choices=TimeFrame.choices, default=TimeFrame.Current)
    sky = models.CharField(choices=Sky.choices, default=Sky.Clear)
    irradiance = models.ForeignKey(PropertyInfo, on_delete=models.CASCADE, null=True, blank=True, related_name="weather_irradiance")
    temperature = models.ForeignKey(PropertyInfo, on_delete=models.CASCADE, null=True, blank=True, related_name="weather_temperature")
    wind_speed = models.ForeignKey(PropertyInfo, on_delete=models.CASCADE, null=True, blank=True, related_name="weather_wind_speed")
    humidity = models.ForeignKey(PropertyInfo, on_delete=models.CASCADE, null=True, blank=True, related_name="weather_humidity")

    @classmethod
    def create(cls, lat=-37.719408, lon=175.248599):
        try:
            instance = WeatherData.objects.create()
            instance.irradiance = PropertyInfo.objects.create(**WEATHER_DATA_PROPERTIES.get("irradiance"))
            instance.temperature = PropertyInfo.objects.create(**WEATHER_DATA_PROPERTIES.get("temperature"))
            instance.wind_speed = PropertyInfo.objects.create(**WEATHER_DATA_PROPERTIES.get("wind_speed"))
            instance.humidity = PropertyInfo.objects.create(**WEATHER_DATA_PROPERTIES.get("humidity"))
            instance.save()
            instance.update_weather_data(lat, lon)
            return instance
        except Exception as e:
            print(str(e))

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
                self.temperature.value = data.get(self.timeframe).get("temp")
                self.wind_speed.value = data.get(self.timeframe).get("wind_speed")
                self.humidity.value = data.get(self.timeframe).get("humidity")
                self.temperature.save()
                self.wind_speed.save()
                self.humidity.save()
                self.save()
            else:
                raise Exception(f"Failed to fetch weather data: {response.status_code}")
        except Exception as e:
            return str(e)

    def __str__(self):
        return (
            f"WeatherData at {self.timestamp}:\n"
            f"Sky Condition: {self.sky}\n"
            f"Temperature: {self.temperature.value}°C, "
            f"Humidity: {self.humidity.value}%, "
            f"Wind Speed: {self.wind_speed.value} m/s\n"
            f"Irradiance: {self.irradiance.value} W/m², "
        )
