import pyautogui as cur
from time import sleep
cur.FAILSAFE = True

def defaultPosition():
    (x, y) = cur.size()
    default_x = x / 2
    default_y = 200
    cur.moveTo(default_x, default_y, 0)


def dragMove(count):
    move = int(count) * 10
    cur.dragRel(0, move, 0.7)

def rightDir():
    cur.keyDown('shift')
    cur.dragRel(-200, 0, 0.5)
    cur.keyUp('shift')

def leftDir():
    cur.keyDown('shift')
    cur.dragRel(200, 0, 0.5)
    cur.keyUp('shift')

def lateFire(seconds, callback):
    sleep(seconds)
    callback = callback
    handler(callback)

def handler(func,*args):
    return func(*args)

def testLeftDir():
    defaultPosition()
    lateFire(5, leftDir)