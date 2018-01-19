#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cgi
import shlex
import subprocess


def index(count):
    html_body = """
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset='utf-8'>
    <title>app</title>
    <style>
    h1 {
    font-size: 3em;
    }
    </style>
    </head>
    <body>
    <h1>クエリ</h1>
    <p>クエリ名はcount</p>
    <p>count=%s</p>
    </body>
    </html>
    """

    print ('Content-type: text/html; charset=UTF-8')
    print(html_body % count)


def getCountQuery(): # get count query
    try:
        count = form['count'].value
        return count
    except KeyError:
        return 0


def writeFlag(): # execute flag.py
    try:
        flag = form['flag'].value
        cmd = "python /home/tenma/Desktop/class/tech_kawamoto/Nagata/Server/flag.py %s" % flag
        augs = shlex.split(cmd)
        p = subprocess.Popen(augs)
    except KeyError:
        pass


def startControlScript(): # execute catch.py
    cmd = "python /home/tenma/Desktop/class/tech_kawamoto/Nagata/Server/catch.py %s" % count
    augs = shlex.split(cmd)
    p = subprocess.Popen(augs)


if __name__ == '__main__':
    form = cgi.FieldStorage()
    count = getCountQuery()
    writeFlag()
    index(count)
    startControlScript()
