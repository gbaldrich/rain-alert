
import requests

API_KEY = '2646b503a2c500ca852dedfe7cea4f94'
WEATHER_ENPOINT_URL = 'https://api.openweathermap.org/data/2.5/weather'

response = requests.get(WEATHER_ENPOINT_URL, params={'q': 'London,uk', 'appid': API_KEY})
response.raise_for_status()
print(response.json())

