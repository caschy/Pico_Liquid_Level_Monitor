# Pico_Liquid_Level_Monitor
Raspberry Pi Pico based water/liquid level tank monitor using analog voltmeter and neopixel 

## Parts:</br>
-Raspberry Pi Pico/Pico W</br>
-XKC-Y25-NPN Waterproof Non Contact Liquid Level Sensors - https://www.amazon.com/XKC-Y25-NPN-Waterproof-Non-Contact-Liquid-Sensor/dp/B074PVF341 (3 qty)</br>
-NEOPIXEL (I used this one: https://www.amazon.com/Adafruit-NeoPixel-Diffused-8mm-Through-Hole/dp/B00KAE40IE/_ (1 qty)</br>
-3.3V Analog VoltMeter (https://www.ebay.com/itm/174080748953)</br>

## Micropython on Pico</br>
Follow the official procedure of getting your Pico to run Micropython here -> https://www.raspberrypi.com/documentation/microcontrollers/micropython.html </br>

## Connecting & Programming the Pico</br>
Download Thonny https://thonny.org/ (used to connect and program the Pico in Micropython)</br>
Connect a micro-usb cable to your Pico and PC</br>
Open Thonny.  You should see the Pico automatically connected in the lower right corner as a Serial or COM port</br>
In Thonny, Goto View-->Files.  This should open up a view pane.  Click on the Pi Pico.  In your PC file explorer find the 'neopixel_rp2040.py' file and drag it into the files pane. Then goto File-->Open in Thonny and open 'pico_tank_monitor.py'  Then goto Save as..., click on On device, and save the file as "main.py."  This will allow the program to run everytime power is applied to the Pico.

