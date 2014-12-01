# -*- coding: utf-8 -*-
# pylint: disable=dangerous-default-value, star-args
'''
Created on Nov 28, 2014

@author: Pavel Bliznakov <pavel@logdaemon.eu>
'''

import importlib
import json
import os
import sys
import tornado.ioloop
import tornado.web

from glob import glob

def __load_modules__(modules_names):
    """
    Dynamically load modules, related to a plugin
    """
    modules = {}
    for name in modules_names:
        try:
            modules[name] = importlib.import_module(name)
        except ImportError:
            sys.stderr.write("Unable to import {0}.".format(name))
    return modules

def __load_plugin__(plugin_dir):
    """
    Load plugin
    """
    plugin_config = os.path.join(plugin_dir, 'plugin.json')
    with open(plugin_config, 'r') as conf_fd:
        config = json.load(conf_fd)
        modules = __load_modules__(config['modules'])
        handlers = [(r'{0}'.format(uri), getattr(modules[mod], cls_name))
                    for (uri, [mod, cls_name]) in
                    [(handler['uri'], handler['class'].rsplit('.', 1))
                     for handler in config['handlers']]]
        return handlers

class Application(tornado.web.Application):
    """
    Wrapper around the tornado Application class
    You should provide plugins path for your application
    as well as a settings dictionary.
    """
    def __init__(self, plugins_path='.', settings={}):
        """
        Constructor
        """
        self.plugins_path = plugins_path
        handlers = []
        lib_path = os.path.join(plugins_path, 'lib')
        sys.path.append(lib_path)
        plugins = glob(os.path.join(lib_path, '*'))
        for plugin_dir in plugins:
            handlers += __load_plugin__(plugin_dir)
        static_path = os.path.join(plugins_path, 'static')
        templates_path = os.path.join(plugins_path, 'templates')
        settings['static_path'] = static_path
        settings['templates_path'] = templates_path
        tornado.web.Application.__init__(self, handlers,
                                         autoescape=None,
                                         **settings)

def run(application, port=8080, address="0.0.0.0"):
    """
    Run the server
    """
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(port, address)
    tornado.ioloop.IOLoop().instance().start()
