# for emailing:
import requests

def Exceeded():
    # Alerts API Url , You can use any other also.
    url = 'https://api.thingspeak.com/alerts/send'

    header = {
        "Thingspeak-Alerts-API-Key":"xxxxxxx",   # Paste your Alert-Api-Key.
        "Content-Type":"application/json"
        }

    content= """ This is the Body of Alert Email. """
        
    data={
        "subject":"This is subject",
        "body":content
    }

    r = requests.post(url , headers=header , json=data)
    
    print("Email sent with code : {r.status_code}")
    
    if r.raise_for_status() is None:
        print("Error : None")
    else:
        r.raise_for_status()

#...



# main project code ...

import grovepi
import time


# 1 ultrasonic sensor ;
# Connect the Grove Ultrasonic Ranger to digital port D4
# SIG,NC,VCC,GND
ultrasonic_ranger = 4


# 2 buzzer
# Connect the Grove Buzzer to digital port D8
# SIG,NC,VCC,GND
buzzer = 8
grovepi.pinMode(buzzer,"OUTPUT")



ulrange = 9878   #random Initialisation

while True:

    try:
        # Read distance value from Ultrasonic
        ulrange = grovepi.ultrasonicRead(ultrasonic_ranger)
        print(ulrange)
        
    except Exception as e:
        print ("Error:{}".format(e))
        grovepi.digitalWrite(buzzer,0)
        break
    
    if ulrange > 1000:
        #buzzer 
        grovepi.digitalWrite(buzzer,0)

    elif ulrange > 500:
        grovepi.digitalWrite(buzzer,1)
        time.sleep(0.5)
        grovepi.digitalWrite(buzzer,0)
    
    elif ulrange > 200:
        grovepi.digitalWrite(buzzer,1)
        time.sleep(0.2)
        grovepi.digitalWrite(buzzer,0)
    
    else:           # If water comes under given Range :
        grovepi.digitalWrite(buzzer,1)
        #send_email_alert
        Exceeded()


        time.sleep(5)
        break

    time.sleep(0.1) # don't overload the i2c bus
