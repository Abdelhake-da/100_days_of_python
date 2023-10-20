import pandas as pd


names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
student_score = {'Alex': 75, 'Beth': 61, 'Caroline': 34, 'Dave': 28, 'Eleanor': 62, 'Freddie': 80}
# comprehension [new_item for item in list if condition]

five_or_more_in_capitel = [name.upper() for name in names if len(name) >= 5]
print(five_or_more_in_capitel)
# ------------------------
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number * number for number in numbers]
print(squared_numbers)
even_num = [number for number in numbers if number % 2 == 0]
print(even_num)
with open('file1.txt') as file:
    data1 = file.read().split()
with open('file2.txt') as file:
    data2 = file.read().split()
unter = [number for number in data1 if number in data2]
print(unter)

# dictionary comprehension {new_key:new_value for (key,value) in dict.items() if test}
from random import randint


# for i in names:
#     student_score[i] = randint(1, 101)
# print(student_score)
# student_score_comprehension = {student: randint(1, 101) for student in names}
# print(student_score_comprehension)
pass_student = {student: score for (student, score) in student_score.items() if score <= 60}
print(pass_student)
sentence = {word: len(word) for word in 'What is the Airspeed Velocity of an Unladen Swallow?'.split()}
print(sentence)
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day: (temp_c * 9 / 5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)



# iterate over a pandas dataFrame
# loop through rows of a data frame
key, value = [], []
for (k, v) in student_score.items():
    key.append(k)
    value.append(v)
student_dic = {
    'student': key,
    'score': value
}
print(student_dic)
student_data_frame = pd.DataFrame(student_dic)
for (index, row) in student_data_frame.iterrows():
    print(row)

data_f = pd.read_csv('nato_phonetic_alphabet.csv')
dic = {row.letter: row.code for (index, row) in data_f.iterrows()}
print(dic)
name = input('input your name : ').upper()
lis = [dic[item] for item in name]
print(lis)
