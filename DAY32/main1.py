# import smtplib
#
my_email = 'abdelhake.da@gmail.com'
password = 'xqlefzsmibpzyvgy'
# connection = smtplib.SMTP('smtp.gmail.com') # smtp.mail.yahoo.com,smtp.live.com(hotmail)
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs='abdohako92@gmail.com', msg='subject:hello\n\nhello this is the first app with send email ')
# connection.close()
#
# import datetime as dt
#
# now = dt.datetime.now()
# print(now.weekday())
# my_date_of_birth = dt.datetime(year=2000, month=5, day=2, hour=12)
# print(my_date_of_birth)
# ===========================================================================================================================================================

import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open('quotes.txt')as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)
print(quote)

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(my_email, password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg=f'Subject: Monday Motivation\n\n{quote}'
    )
