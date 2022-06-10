
import requests
import os
from twilio.rest import Client

params={
    # 'lat': 47.003819, 
    # 'lon': -123.407806,
    'lat': 10.397699, 
    'lon': -75.464003,
    'exclude': 'current,minutely,daily,alerts,flags',
    'appid': '2646b503a2c500ca852dedfe7cea4f94',
    }

response = requests.get('https://api.openweathermap.org/data/2.5/onecall', params)
response.raise_for_status()
weather_data = response.json()['hourly'][:12]

ids_list_lower_than_700 = [hour['weather'][0]['id'] for hour in weather_data if hour['weather'][0]['id'] < 700]

is_going_to_rain = len(ids_list_lower_than_700) > 0 # if there is at least one id less than 700, then it is going to rain
if is_going_to_rain:
    print('Bring an umbrella!')

