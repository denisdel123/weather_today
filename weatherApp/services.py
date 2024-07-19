import requests


def get_weather(city, token):
    result = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric')
    data = result.json()
    return data
