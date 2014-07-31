import os
import logging
from twisted.python import log
import json

CONFIG_FILE = 'config.json'


def get_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'rb') as f:
            options = json.load(f)
        return options
    else:
        return {}


def start_log(level=logging.INFO):
    observer = logger(level)
    log.startLoggingWithObserver(observer)


def logger(loglevel):
    numeric_level = getattr(logging, loglevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % loglevel)
    logging.basicConfig(
        format='%(asctime)s-[%(levelname)s]-%(name)s :  %(message)s',
        level=numeric_level)
    observer = log.PythonLoggingObserver()
    return observer.emit
