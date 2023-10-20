MY_LAT = 21.145800
MY_LNG = 79.088158
API_KEY = 'fba1bd2455973d81d201287c7ea588a7'
country = 'London,UK'
url = 'https://api.openweathermap.org/data/2.5/weather'
url1 = 'https://api.openweathermap.org/data/2.5/onecall'
# ?q={country}&appid={API_KEY}
params = {
    'q': country,
    'appid': API_KEY
}
params1 = {
    'lat': MY_LAT,
    'lon': MY_LNG,
    'appid': API_KEY,
    'exclude': 'daily,current,minutely'
}
import requests

response = requests.get(url1, params=params1)
response.raise_for_status()
data = response.json()
first12 = data['hourly'][0:12]
h = False
for hour in first12:
    if hour['weather'][0]['id'] < 700:
        h = True
        break
from twilio.rest import Client

account_sid = 'AC3e38fc8efcfd2736707615630aa5509a'
auth_token = '21b05d1b27c6993e81a1b1acbff95adf'
if h:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='It\'s going to rain today. Remember to bring an umbrella☂️',
        from_='+18787688918',
        to='+213797873139'
    )
    print(message.status)
# for create environment (export name_env=value)
# for show the environment (env)
# for get value of environment (we should import os lib and write os.environ.get(name_env))
