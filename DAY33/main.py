import requests

MY_LAT = 47.796530
MY_LNG = 11.774210
'''
response = requests.get(url='http://api.open-notify.org/iss-now.json')
print(response)
response.raise_for_status()
data = response.json()
print(data)
longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']
iss_position = (longitude, latitude)
print(iss_position)
'''
parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0
}
response = requests.get('http://api.sunrise-sunset.org/json', params=parameters)
                        #https://api.sunrise-sunset.org/json
response.raise_for_status()
data = response.json()
sunrise =( str(data['results']['sunrise']).split('T')[1]).split(':')[0:2]
sunset = (str(data['results']['sunset']).split('T')[1]).split(':')[0:2]
print(f'{sunrise}/{sunset}')
import datetime as dt

time_now = dt.datetime.now()
print(time_now)
