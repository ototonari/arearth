import pyautogui as cur
import time
cur.FAILSAFE = True


def defaultPosition():
    (x, y) = cur.size()
    default_x = x / 2
    default_y = 200
    cur.moveTo(default_x, default_y, 0)


def dragMove(count):
    move = int(count) * 10
    cur.dragRel(0, move, 0.7)
