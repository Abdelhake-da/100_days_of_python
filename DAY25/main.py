# with open('29152028-weather-data.csv') as file:
#     lines = file.readlines()
# data = []
# for line in lines:
#     data.append((line.strip()).split(','))
# print(data)
#
# # csv file librarie
# import csv
#
# with open('29152028-weather-data.csv')as data_file:
#     data = csv.reader(data_file)
#     temperarures = []
#     for row in data:
#         temperarures.append(row)
# print(temperarures)

# pandas librarie
import pandas

data = pandas.read_csv('29152028-weather-data.csv')
# print(data)
#
# # from pandas_dataFrame to dictionnere
# dic = data.to_dict()
# print(dic)
# # from pandas series to list
# temp_lis = data['temp'].tolist()
# print(temp_lis)
# count = data['temp'].count()
# sum = data['temp'].sum()
# avg = sum / count
# print(f'avg = {sum}/{count} = {round(avg, 2)}')
# print(f'mean = {round(data["temp"].mean(), 2)}')
# print(f'max = {data["temp"].max()}')
# print(f'max_temp =\n{data[data.temp == data["temp"].max()]}\nmin_temp =\n{data[data.temp == data["temp"].min()]}')
# monday = data[data.day == 'Monday']
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9 / 5 + 32
# print(f'fehrinhit = {monday_temp_f}')

# Create a dataframe form scratch
# data_dict = {
#     'students': ['amy', 'james', 'angela'],
#     'scores': [76, 56, 65]
# }
# data_frame = pandas.DataFrame(data_dict)
# print(data_frame)
# data_frame.to_csv('new_csv.csv')

# data1 = pandas.read_csv('29569130-2018-Central-Park-Squirrel-Census-Squirrel-Data.csv')
# gray = data1[data1['Primary Fur Color'] == 'Gray']
# print(len(gray))
# cinnamon = data1[data1['Primary Fur Color'] == 'Cinnamon']
# print(len(cinnamon))
# Black = data1[data1['Primary Fur Color'] == 'Black']
# print(len(Black))
# dic = {'Fur Color': ['Gray', 'Cinnamon', 'Black'],
#        'Count': [len(gray), len(cinnamon), len(Black)]}
# df = pandas.DataFrame(dic)
# df.to_csv('squirrel_count.csv')

data = pandas.read_csv('50_states_game/algeria_states.csv')
print(data)