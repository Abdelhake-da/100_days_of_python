import requests

USERNAME = 'abdelhake'
TOKEN = 'hakohakohako123'
GRAPH_ID = 'graph1'
pixela_endpoint = 'https://pixe.la/v1/users'
# create a user account
user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
# # create a graph definition
graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
graph_config = {
    'id': 'graph1',
    'name': 'Cycling Graph',
    'unit': 'Km',
    'type': 'float',
    'color': 'ajisai',
}
headers = {
    'X-USER-TOKEN': TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
import datetime as dt

date = str(str(dt.datetime.now()).split()[0]).split('-')
date = f'{date[0]}{date[1]}{date[2]}'

pixel_creation_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

pixela_data = {
    'date': '20220730',
    'quantity': '50',
}
# response = requests.post(url=pixel_creation_endpoint, json=pixela_data, headers=headers)
# print(response.text)

# put requests
update_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}'

new_pixel_data = {
    'quantity': '60',
}
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)
# delete
delete_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20220730'

response = requests.delete(url=update_endpoint, headers=headers)
print(response.text)
