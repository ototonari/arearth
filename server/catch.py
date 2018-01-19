import cgi
from controllers.controller import defaultPosition, dragMove
import sys


with open('flag.txt', 'r') as f: # if flag is True,move cursor.
    flag = f.readline()
    if flag == 'True':
        form = cgi.FieldStorage()
        args = sys.argv
        defaultPosition()
        dragMove(int(args[1]))
