import requests
from datetime import datetime

MY_LAT = 36.043419
MY_LNG = 0.896377
my_email = 'abdelhake.da@gmail.com'
password = 'xqlefzsmibpzyvgy'


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(f'{iss_latitude}/{iss_longitude}')
    # Your position is within +5 or -5 degrees of the ISS position.
    if (iss_longitude - 5 <= MY_LNG <= iss_longitude + 5) and (
            iss_latitude + 5 <= MY_LAT or iss_latitude - 5 <= MY_LAT):
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }
    response = requests.get("http://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now >= sunset or time_now <= sunrise:
        return True


# Then send me an email to tell me to look up.
import smtplib
import time
while True:
    if is_night() and is_iss_overhead():
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg='Subject:LOOK UP \n\n The ISS is above you in the sky'
        )
    time.sleep(60)
# BONUS: run the code every 60 seconds.
