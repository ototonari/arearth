# -*- coding: utf-8 -*-

import http.server


def writeFlagFile(): # write a flag to flag.txt
    with open('flag.txt','w') as f:
        f.write('False')


if __name__ == '__main__':
    writeFlagFile()
    http.server.test(HandlerClass=http.server.CGIHTTPRequestHandler)