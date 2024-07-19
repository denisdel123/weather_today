import os
from django.shortcuts import render
from weatherApp.forms import CityForm
from weatherApp.models import SearchHistory
from weatherApp.services import get_weather


def main(request):
    token = os.environ.get('TOKEN_OPEN_WEATHER')
    weather_set = None
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            try:
                weather_data = get_weather(city, token)
                temperature = weather_data['main']['temp']  # температура
                humidity = weather_data['main']['humidity']  # влажность
                pressure = weather_data['main']['pressure']  # давление
                wind_speed = weather_data['wind']['speed']  # скорость ветра
                weather_set = {
                    'city': city,
                    'temperature': temperature,
                    'humidity': humidity,
                    'pressure': pressure,
                    'wind_speed': wind_speed,
                }

                # обновление истории
                search, created = SearchHistory.objects.get_or_create(city=city)
                search.count += 1
                search.save()
            except ValueError as e:
                # Обработка ошибок, если город или данные не найдены
                weather_set = {
                    'city': city,
                    'error': str(e),
                }
    else:
        form = CityForm()
    return render(
        request,
        'weatherApp/main.html',
        {'form': form, 'weather_set': weather_set}
    )
