from django.db import models

class TimeFrame(models.TextChoices):
    Current = "current"
    Minutely = "minutely"
    Hourly = "hourly"
    Daily = "daily"
    
class Sky(models.TextChoices):
    Cloudy = "cloudy_sky"
    Clear = "clear_sky"