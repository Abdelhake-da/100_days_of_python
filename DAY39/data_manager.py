import requests

url_sheet_api = 'https://api.sheety.co/0d24386c393200a9fe20203621dd02a7/flightDeals/prices'


class DataManager:
    def __init__(self):
        self.sheet_data = requests.get(url=url_sheet_api).json()['prices']

    def edit_data(self, data):
        for city in data:
            url_sheet_api_edit = f'{url_sheet_api}/{city["id"]}'
            response = requests.put(url=url_sheet_api_edit, json={'price': city})
            print(response.text)

    def delete_iata(self):
        for city in self.sheet_data:
            city['iataCode'] = ''
            url_sheet_api_edit = f'{url_sheet_api}/{city["id"]}'
            response = requests.put(url=url_sheet_api_edit, json={'price': city})
            print(response.text)
