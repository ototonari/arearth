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
    cur.dragRel(0, move, 0.5)

def rightDir():
    cur.keyDown('shift')
    cur.dragRel(-100, 0, 0.2)
    cur.keyUp('shift')

def leftDir():
    cur.keyDown('shift')
    cur.dragRel(100, 0, 0.2)
    cur.keyUp('shift')

def lateFire(seconds, callback):
    sleep(seconds)
    callback = callback
    handler(callback)

def handler(func,*args):
    return func(*args)

def testLeftDir():
    sleep(5)
    defaultPosition()
    lateFire(1, leftDir)
    lateFire(1, leftDir)

def testLeftAndMove():
    sleep(5)
    defaultPosition()
    leftDir()
    defaultPosition()
    dragMove(10)