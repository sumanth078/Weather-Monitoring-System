from django.urls import path
from . import views

urlpatterns = [
    path('current/', views.current_weather, name='current_weather'),
    path('summary/', views.daily_summary, name='daily_summary'),
]
