import datetime
from time import sleep
import pyttsx3


from selenium import webdriver


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


print(int(str(datetime.datetime.now())[11:13]))
print(int(str(datetime.datetime.now())[14:16]) + 1)
option = webdriver.ChromeOptions()
option.add_argument('headless')

import requests

url = "https://www.fast2sms.com/dev/bulk"

headers = {
    'authorization': "aWmyldGXYkqTQFo9cb5K1st6geJARZ4uLnP2jVEMH0Sr3DziIxWviBmqXgeTV25xcwFjdaPsZERk8G9D",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
}
previous = []





while True:
    driver = webdriver.Chrome(r"chromedriver.exe", options=option)

    driver.get("https://in.bookmyshow.com/buytickets/rrr-hyderabad/movie-hyd-ET00094579-MT/20220325")
    flag = 3
    theatres = driver.find_elements_by_class_name("__venue-name")
    theatres1 = [i.text for i in theatres]
    print(theatres1)
    sent = 0

    t = []
    new = list(set(theatres1) - set(previous))


    print("New theatres: " + str(new))
    given = ['Sudarshan' , 'Galleria', 'INOX', 'Devi', 'Shanti', 'PVR']

    for theatre in theatres1:
        if theatre in given:
            t.append(theatre)

    if len(t)>0:
        talk("Bookings opened at a given station")
        hr = int(str(datetime.datetime.now())[11:13])
        min = int(str(datetime.datetime.now())[14:16]) + 2
        payload = f"sender_id=FSTSMS&message=BOOKINGS OPEN in {str(t)}&language=english&route=p&numbers=9676153216,9059031725"
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)
        print("msg sent")

    else:
        print(f"booking not opened in given theatres at {datetime.datetime.now()}")

    if len(new)>0:
        talk("New Theatre added :"+ new[0])
        hr = int(str(datetime.datetime.now())[11:13])
        min = int(str(datetime.datetime.now())[14:16]) + 2
        payload = f"sender_id=FSTSMS&message=NEW THEATRE ADDED :  {str(new)}&language=english&route=p&numbers=9676153216, 9059031725"
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)
        print("msg sent")

    previous = theatres1
    driver.close()
    sleep(30)
