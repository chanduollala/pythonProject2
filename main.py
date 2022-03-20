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

    driver.get("https://paytm.com/movies/hyderabad/rrr-movie-ticket-booking-73yjnt3qp")

    db = driver.find_elements_by_tag_name('span')

    f= [i.text for i in db]

    for e in f :
        if '3D' in f:
            talk("3D booking open in paytm")
            break
        else:
            print("3d bookings not open at", str(datetime.datetime.now()))
            break


    driver.close()
    sleep(30)