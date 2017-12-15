import pyautogui as cur
from httphandler import Response, Request, get_htmltemplate
import time
import cgi
import os
import sys

cur.FAILSAFE = True

try:
  req = Request()
  res = Response()
  
except:
  raise

try:
  count = req.form['count'].value if 'count' in req.form else 0

except:
  raise


def defaultPosition():
  (x, y) = cur.size()
  default_x = x / 2
  default_y = 200
  cur.moveTo(default_x, default_y, 0)

def startMouseDown():
  default_x = x / 2
  default_y = 0
  cur.mouseDown(default_x, default_y, button='left')

def constMove():
  defaultPosition()

def dragMove(count):
  move = int(count) * 10
  cur.dragRel(0, move, 0.7)



try:
  time.sleep(5)

  count = 0
  while count < 10:
    count += 1

    defaultPosition()
    dragMove(10)
    #cur.moveTo(default_x, default_y, 0)
    #(x, y) = cur.position()
    #cur.dragRel(0, 20, 1)
    #defaultPosition()
    #cur.typewrite(['up'], 0)
    

except:
  raise

