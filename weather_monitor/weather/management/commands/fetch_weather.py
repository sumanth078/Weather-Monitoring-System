from django.core.management.base import BaseCommand
from weather.views import fetch_weather_data

class Command(BaseCommand):
    help = 'Fetch weather data from OpenWeatherMap'

    def handle(self, *args, **kwargs):
        fetch_weather_data()
        self.stdout.write(self.style.SUCCESS('Successfully fetched weather data.'))
