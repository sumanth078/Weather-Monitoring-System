# weather/views.py

from django.shortcuts import render
import requests
from django.http import HttpResponse
from .models import WeatherSummary
from django.utils import timezone
from datetime import timedelta


def current_weather(request):
    api_key = 'e79e8f1fb3cba4c9b531cf509b645a75'
    city = 'Delhi'  # Example city, you can change this to any city you want
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        # Check if the request was successful
        if response.status_code != 200:
            return HttpResponse(f"Error fetching weather data: {data.get('message', 'Unknown error')}", status=400)

        # Extract the relevant information
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        condition = data['weather'][0]['main']

        # Render the current weather template with context data
        return render(request, 'weather/current_weather.html', {
            'temperature': temperature,
            'feels_like': feels_like,
            'condition': condition
        })

    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}", status=500)


def daily_summary(request):
    # Get today's date and the date from 24 hours ago
    now = timezone.now()
    today = now.date()
    yesterday = today - timedelta(days=1)

    # Query to summarize the weather data for the past day
    summaries = WeatherSummary.objects.filter(date__range=[yesterday, today])

    # Calculate daily aggregates
    average_temp = summaries.aggregate(avg_temp=models.Avg('temperature'))['avg_temp']
    max_temp = summaries.aggregate(max_temp=models.Max('temperature'))['max_temp']
    min_temp = summaries.aggregate(min_temp=models.Min('temperature'))['min_temp']

    # You may want to determine the dominant weather condition
    # For this example, we'll just count occurrences of each condition
    condition_counts = summaries.values('condition').annotate(count=models.Count('condition'))
    dominant_condition = max(condition_counts, key=lambda x: x['count'], default=None)

    # Render the daily summary template with context data
    return render(request, 'weather/daily_summary.html', {
        'average_temp': average_temp,
        'max_temp': max_temp,
        'min_temp': min_temp,
        'dominant_condition': dominant_condition['condition'] if dominant_condition else 'N/A',
    })
