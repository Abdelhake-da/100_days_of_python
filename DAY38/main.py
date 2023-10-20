import requests
import os
API_KEY = os.environ['API_KEY']
ID_APP = os.environ['ID_APP']
PASSWORD = os.environ['PASSWORD']
user_name = os.environ['user_name']
email = os.environ['email']
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_url = 'https://api.sheety.co/0d24386c393200a9fe20203621dd02a7/myWorkouts/workouts'
gender = 'male'
weight_kg = 76.1
height_cm = 170
age = 22
query = input('Tell mew which exercises you did: ')
headers = {
    'x-app-id': ID_APP,
    'x-app-key': API_KEY
}
data_json_nutrition_Ix = {
    'query': query,
    'gender': gender,
    'weight_kg': weight_kg,
    'height_cm': height_cm,
    'age': age
}
response_from_nutrition_Ix = requests.post(url=exercise_endpoint, json=data_json_nutrition_Ix, headers=headers)
data_from_nutrition_Ix = response_from_nutrition_Ix.json()
print(data_from_nutrition_Ix)

##################################
from datetime import datetime

today_date = datetime.now().strftime('%d/%m/%Y')
now_time = datetime.now().strftime('%X')
for item in data_from_nutrition_Ix['exercises']:
    sheet_input = {
        'workout': {
            'date': today_date,
            'time': now_time,
            'exercise': item['name'].title(),
            'duration': int(item['duration_min']),
            'calories': item['nf_calories']
        }
    }
    print()
    # rep = requests.post(url=sheety_url, json=sheet_input)
    # print(rep.text)
####################
#Basic Authentication
sheet_response = requests.post(
  sheety_url,
  json=sheet_input,
  auth=(
      'abdelhake',
      'abdohako92',
  )
)

# #Bearer Token Authentication
# bearer_headers = {
# "Authorization": "Bearer YOUR_TOKEN"
# }
# sheet_response = requests.post(
#     sheet_endpoint,
#     json=sheet_inputs,
#     headers=bearer_headers
# )
