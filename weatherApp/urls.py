from django.urls import path
from weatherApp.views import main
from weatherApp.apps import WeatherappConfig

app_name = WeatherappConfig.name

urlpatterns = [
    path('', main,)
]