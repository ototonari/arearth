#!/usr/bin/python
# coding: utf-8; -*-

import RPi.GPIO as GPIO
import time
import datetime
import signal

REF_PIN=21
LED_PIN=20

GPIO.setmode(GPIO.BCM)
GPIO.setup(REF_PIN,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

#current = int(datetime.datetime.now().second) + int(datetime.datetime.now().microsecond)*0.000001
current = 0
old = 0
dtime = 0

counter = 0

def event_callback(gpio_pin):
    global current
    old = current
    current = int(datetime.datetime.now().second) + int(datetime.datetime.now().microsecond)*0.000001
    dtime = current - old
    if dtime<0:
        dtime = current + 60 - old
    print(dtime)

GPIO.add_event_detect(REF_PIN,GPIO.RISING,
                        callback=event_callback,bouncetime=10)

try:
    while True:
        continue
except KeyboardInterrupt:
    GPIO.cleanup()

"""
while True:
    ref=GPIO.input(REF_PIN)
    if ref == True:
        old = current
        current = int(datetime.datetime.now().second) + int(datetime.datetime.now().microsecond)*0.000001
        dtime = current - old
        if dtime<0:
            dtime = current+60 - old
        print(dtime)
    time.sleep(0.0001)
"""
