Whirlwind
=========

A wrapper for tornado web to run easily web applications as plugins.

## How to use it?

The simplest way to use Whirlwind is to instantiate the ```Application``` class along with plugins directory and run its instance with the ```run``` method.

```
import whirlwind.web

my_app = whirlwind.web.Application('data/plugins')
whirlwind.web.run(my_app)
```

## How to write a plugin and manually import it?

In your plugins directory, create a directory with the plugin name, i.e. ```test_plugin``` in the following directories: ```lib```, ```static``` and ```templates```. The plugins directory should contain a similar structure:

Directory structure:
```
├── plugins/
│   ├── lib
│   │   ├── test_plugin
│   │   │   ├── __init__.py
│   │   │   ├── my_plugin.py
│   │   │   ├── plugin.json
│   ├── static
│   │   ├── test_plugin
│   │   │   ├── js
│   │   │   │   ├── some_javascript.js
│   ├── templates
│   │   ├── test_plugin
│   │   │   ├── my_html_template.html
```

The ```plugin.json``` file contains information on URI mapping to plugin classes.

```
{
    "modules" : ["test_plugin.my_plugin"],
    "handlers" : [
                 ["/someaction/", "test_plugin.my_plugin.MyActionHandler"],
                 ["/otheraction/(\w+)", "test_plugin.my_plugin.MyActionSecondHandler"],
                 ]
}
```

```MyActionHandler``` and ```MyActionSecondHandler``` are classes that extend either ```tornado.web.RequestHandler``` or ```tornado.websocket.WebSocketHandler``` and all the documentation of these parent classes applies to them. You can find more information in the [Tornado documentation](http://www.tornadoweb.org/en/stable/webframework.html)
