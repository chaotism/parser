#coding: utf-8
from __future__ import unicode_literals
import time
import os
import sys
import logging
from PyQt4 import QtCore
import logging.handlers


formatter = logging.Formatter(fmt='%(levelname)s:%(name)s:  %(filename)s:%(lineno)d %(message)s '
    '(%(asctime)s; %(filename)s:%(lineno)d)',
    datefmt="%Y-%m-%d %H:%M:%S")
handlers = [
    logging.handlers.RotatingFileHandler('loger.log', encoding='utf8', backupCount=1),
    logging.StreamHandler(),
    #logging.handlers.MemoryHandler(capacity=9, flushLevel=logging.INFO, target=sys.stdout)
]


root_logger = logging.getLogger(__name__)
root_logger.setLevel(logging.DEBUG)


for handler in handlers:
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)
    root_logger.addHandler(handler)


def tail_generator(file):
    with open(file, 'r') as f:
        f.seek(0,2)
        while True:
            line = f.read(1)
            if not line:
                time.sleep(0.1)
                continue
            yield line


def tail(file):
    if not os.path.exists(file):
        f = open(file, 'w+')

    else:
        f = open(file, 'r+')
        lines = []
    f.seek(0,2)
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue
        lines.append(line)
        f.close()
        return lines

# while True:
#     print tail_generator('loger.log').next()
