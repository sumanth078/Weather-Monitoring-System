from django.db import models

# Create your models here.
from django.db import models

class WeatherData(models.Model):
    city_name = models.CharField(max_length=100)
    main = models.CharField(max_length=50)
    temp = models.FloatField()
    feels_like = models.FloatField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.city_name} - {self.temp}°C - {self.main}"

class DailySummary(models.Model):
    city_name = models.CharField(max_length=100)
    date = models.DateField()
    avg_temp = models.FloatField()
    max_temp = models.FloatField()
    min_temp = models.FloatField()
    dominant_weather = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.city_name} - {self.date} - {self.avg_temp}°C"

class WeatherSummary(models.Model):
    temperature = models.FloatField()
    feels_like = models.FloatField()
    condition = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.condition} on {self.date}"