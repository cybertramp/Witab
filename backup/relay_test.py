# Python3 code

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pins = [25,8,7,1]

for i in pins:
    GPIO.setup(i, GPIO.OUT)

for i in pins:
    GPIO.output(i,GPIO.HIGH)
    print(i,"ON")
    time.sleep(1)

for i in pins:
    GPIO.output(i,GPIO.LOW)
    print(i,"OFF")
    time.sleep(1)

for i in pins:
    GPIO.output(i,GPIO.HIGH)
    print(i,"ON")
    time.sleep(2)
    GPIO.output(i,GPIO.LOW)
    print(i,"OFF")
    time.sleep(2)

GPIO.cleanup()
