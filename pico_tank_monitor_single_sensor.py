# ''' Import NEOPixel Driver Library '''
# import neopixel_rp2040

import machine
import network
from Onesignal import SMS_Messenger
from machine import Pin, PWM
from time import sleep
from Onesignal import Notifier

messenger =SMS_Messenger ("d44181ad-de37-410f-a285-7f47b0a9fc04",
                          "NjJjZDlkZTItOWU1YS00OTJmLThhZDMtZjM3ZWZjYTA2ODM4",
                         ["+16693382499"],
                          "ATO Bot",
                          "en")

messenger.send_text("The ATO water level is LOW - Top off the Tank",["+17657448305"])

ssid = "It Burns When IP"
password = "Tr0utK0d@9711"

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]    
    print(f"Connected on {ip}")
    return ip

''' 
   Define sensors inputs
'''
low_sensor = Pin(20, Pin.IN, Pin.PULL_UP)

''' 
   simple function to change gauge reading based upon passed parameter
'''
    
if (low_sensor.value()) == True:
        if ((not low_sensor.value()) and (not mid_sensor.value())):
            if (not high_sensor.value()):
                led.set(LED_NUMBER=0, COLOR=led.BLUE, BRIGHTNESS=0.5)
                new_reading = 65535
                print("at least 75 % full")
            else:
                led.set(LED_NUMBER=0, COLOR=led.GREEN, BRIGHTNESS=0.5)
                new_reading = 43330
                print("at least 50 % full")
        else:
            led.set(LED_NUMBER=0, COLOR=led.YELLOW, BRIGHTNESS=0.5)
            new_reading = 21845
            print("at least 25 % full")
    else:
        led.set(LED_NUMBER=0, COLOR=led.RED, BRIGHTNESS=0.5)
        new_reading = 100
        print("at least 50 % full")

    sweep(new_reading)
    sleep(3)
