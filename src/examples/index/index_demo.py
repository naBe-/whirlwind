#!/usr/bin/env python
'''
Created on Dec 1, 2014

@author: Pavel Bliznakov <pavel@logdaemon.eu>
'''

import sys

import whirlwind.web as web

if __name__ == '__main__':
    port = sys.argv[1] if len(sys.argv) > 1 else 8080
    address = sys.argv[2] if len(sys.argv) > 2 else '0.0.0.0'
    app = web.Application()
    web.run(app, port, address) 