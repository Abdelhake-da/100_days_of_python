# ----------------------- Extra Hard Starting Project ---------------
import pandas as pd
import datetime as dt

# 1. Update the birthdays.csv
data = pd.read_csv('birthdays.csv')
# 2. Check if today matches a birthday in the birthdays.csv
val = -1
today = dt.datetime.now()
for month, day, index in zip(data.month, data.day, range(len(data))):
    if today.day == day and today.month == month:
        val = index
        break

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv
import random

letter = ''
letters = {
    '0': 'letter_templates/letter_1.txt',
    '1': 'letter_templates/letter_2.txt',
    '2': 'letter_templates/letter_3.txt'
}
if val != -1:
    with open(letters[str(random.randint(0, 2))]) as file:
        letter = file.read()
# 4. Send the letter generated in step 3 to that person's email address.
import smtplib
my_mail = 'abdelhake.da@gmail.com'
password = 'xqlefzsmibpzyvgy'
letter = letter.replace('[NAME]', data.name[val])
with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(my_mail, password)
    connection.sendmail(from_addr=my_mail, to_addrs=my_mail, msg=f'Subject: Happy BirthDay\n\n'
                                                                 f'{letter}')