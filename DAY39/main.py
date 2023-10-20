# This file will need to use the DataManager,FlightSearch
# , FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch

dataManager = DataManager()
sheet_data = dataManager.sheet_data
flightSearch = FlightSearch()

data_withOut_iatacde = []
for city in sheet_data:
    if city['iataCode'] == '':
        data_withOut_iatacde.append(city['city'])

# dataManager.delete_iata()

from datetime import datetime,timedelta

if sheet_data[0]['iataCode'] == '':
    for city in sheet_data:
        city['iataCode'] = flightSearch.return_iataCode(city['city'])

    dataManager.edit_data(sheet_data)
date = datetime.now() + timedelta(days=(30 * 6))
for city in sheet_data:
    flightSearch.check_flights('LON', city['iataCode'], datetime.now(), date)
'''
 {
      "id": "algiers_dz",
      "active": true,
      "name": "Algiers",
      "slug": "algiers-algeria",
      "slug_en": "algiers-algeria",
      "code": "ALG",
}
'''
