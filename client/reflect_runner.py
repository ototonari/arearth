#!/usr/bin/python
# coding: utf-8; -*-

import RPi.GPIO as GPIO
import time, signal


REF_PIN=21

#GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
GPIO.setup(REF_PIN,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

counter = 0

def event_callback(gpio_pin):
    global counter
    counter = counter + 1

GPIO.add_event_detect(REF_PIN,GPIO.RISING,
                        callback=event_callback,bouncetime=10)



import send_ref
url    = 'http://192.168.1.89:8000/cgi-bin/app.py'


sigtime = 1

def handler(signum, frame):
    global counter
    params = {'count' : counter}
    try:
        send_ref.send_ref(url,params)
    except:
        pass
    print params
    counter = 0
    signal.alarm(sigtime)

signal.signal(signal.SIGALRM, handler)

signal.alarm(sigtime)


try:
    while True:
        continue
except KeyboardInterrupt:
    signal.alarm(0)
    GPIO.cleanup()
