''' Import NEOPixel Driver Library '''
import neopixel_rp2040

from machine import Pin, PWM
from time import sleep

'''
    Create NEOPixel Object
    Here 'LEDS=' sets the number of LEDs connected in Neopixel string
         'PIN=' is the Pin number used to connect the DIN pin of the Neopixel to the Raspberry Pi Pico
'''
led = neopixel_rp2040.neopixel(LEDS=1, PIN=16)

cur_reading = 0
new_reading = 0
step = -1
low_sensor = Pin(18, Pin.IN, Pin.PULL_UP)
mid_sensor = Pin(19, Pin.IN, Pin.PULL_UP)
high_sensor = Pin(20, Pin.IN, Pin.PULL_UP)
gauge = PWM(Pin(15))
gauge.freq(1000)

def sweep(reading):
    if (cur_reading < reading):
        for duty in range(reading,cur_reading):
            gauge.duty_u16(duty)
            sleep(0.01)
    elif (cur_reading > reading):
        for duty in range(cur_reading,reading,step):
            gauge.duty_u16(duty)
            sleep(0.01)
    cur_reading = reading
    
while True:
    '''pretty gauge sweep'''
    for duty in range(0,65535):
        gauge.duty_u16(duty)
        sleep(0.01)
    sleep(0.5)
    gauge.dutry_u16(0) 
    led.test()
    sleep(2)
    led.reset()
    
    if (not low_sensor.value()):
        if ((not mid_sensor.value()) and (not high_sensor.value())):
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
