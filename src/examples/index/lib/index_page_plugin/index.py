'''
Created on Dec 1, 2014

@author: Pavel Bliznakov <pavel@logdaemon.eu>
'''

from datetime import datetime
from tornado.web import RequestHandler

class IndexHandler(RequestHandler):
    '''
    Simple index page handler
    '''
    def get(self):
        time_string = datetime.now().strftime("%c")
        self.write("This is a simple index handler.")
        self.write(" This page was generated at %s." % (time_string))
        self.flush()
