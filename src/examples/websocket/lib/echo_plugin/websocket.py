"""
Created on Dec 1, 2014

@author: Pavel Bliznakov <pavel@logdaemon.eu>
"""

import os

from datetime import datetime
from tornado.web import RequestHandler
from tornado.websocket import WebSocketHandler
from uuid import uuid4

_PLUGIN_NAME_ = 'echo_plugin'

echo_clients = dict()

class EchoHandler(RequestHandler):
    """
    Simple index page handler
    """
    def get(self):
        time_string = datetime.now().strftime("%c")
        template_path = os.path.join(_PLUGIN_NAME_, "echo.html")
        self.render(template_path, generation_timestamp=time_string)

class EchoWebSocket(WebSocketHandler):
    """
    Server-side websocket interface
    """
    def open(self, *args):
        self.client_id = uuid4().get_hex()
        self.stream.set_nodelay(True)
        echo_clients[self.client_id] = {"id" : self.client_id, "object" : self}

    def on_message(self, message):
        """
        Send message back
        """
        self.write_message(u"You said: {0}".format(message))

    def on_close(self):
        if self.client_id in echo_clients:
            del echo_clients[self.client_id]

