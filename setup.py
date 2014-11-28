try:
    import minify.command
    minify_js = minify.command.minify_js
    minify_css = minify.command.minify_css
except ImportError:
    minify_js = None
    minify_css = None

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name = "Whirlwind",
    version = "0.1",
    packages = ['whirlwind'],
    package_dir = {'whirlwind' : 'src/whirlwind'},
    install_requires=['tornado>=3'],
    author = "Pavel Bliznakov",
    author_email = "pavel@logdaemon.eu",
    description = "A wrapper for tornado web to run easily web applications as plugins.",
    license = "Apache License 2.0",
)
