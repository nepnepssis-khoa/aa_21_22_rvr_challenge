import board
import busio
import time
import math

import adafruit_hcsr04
from sphero_rvr import RVRDrive

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.B1, echo_pin=board.B0)    # M4 Metro express

rvr = RVRDrive(uart = busio.UART(board.A2, board.A3, baudrate=115200))       # M4 Metro express

time.sleep(0.5)

rvr.set_all_leds(255,0,0) #set leds to red
time.sleep(0.1)
rvr.set_all_leds(0,255,0) #set leds to green
time.sleep(0.1)
rvr.set_all_leds(0,0,255) #set leds to blue
time.sleep(0.1) #turn off
rvr.set_all_leds(255,255,255) #turn off leds or make them all black



print("starting up")

rvr.sensor_start()

print("sensor_start")

# CODE BELOW THIS LINE WILL WORK FOR ANY BOARD ********************************************
MAX_SPEED = 100
rvr.sensor_start()

rvr.drive(100,90)
time.sleep(1.0)
rvr.stop()

setMotors(self,left,right):
