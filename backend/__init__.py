from flask import Flask
from flask.ext.bower import Bower

from redis import Redis

from .redis_session import RedisSessionInterface

import os
import logging

from logging.handlers import SysLogHandler, SMTPHandler

basedir = os.path.abspath(os.path.dirname(__file__))

# Initialize application
app = Flask(__name__)
app.config.from_object('secret_backend_config')

# Create a Redis connection
redis = Redis()

# Initialize the redis session interface
app.session_interface = RedisSessionInterface(
        redis=redis,
)

# Initialize Bower extension
bower = Bower(app)

# Set up logging to syslog
_syslog_handler = SysLogHandler(
        '/dev/log',
)

_smtp_handler = SMTPHandler(
        app.config['SMTP_LOGGING']['host'],
        app.config['SMTP_LOGGING']['from_addr'],
        app.config['SMTP_LOGGING']['to_addrs'],
        app.config['SMTP_LOGGING']['subject'],
        app.config['SMTP_LOGGING']['credentials'],
        app.config['SMTP_LOGGING']['secure'],
)

if app.debug:
    _syslog_handler.setLevel(logging.VERBOSE)
else:
    _syslog_handler.setLevel(logging.INFO)
    _smtp_handler.setLevel(logging.ERROR)

    app.logger.addHandler(_smtp_handler)

app.logger.addHandler(_syslog_handler)

from . import (
        views,
        confirm,
        api,
)
