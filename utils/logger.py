#coding: utf-8
from __future__ import unicode_literals
import time
from PyQt4 import QtCore
import sys
import logging
import logging.handlers

f = logging.Formatter(fmt='%(levelname)s:%(name)s:  %(filename)s:%(lineno)d %(message)s '
    '(%(asctime)s; %(filename)s:%(lineno)d)',
    datefmt="%Y-%m-%d %H:%M:%S")
handlers = [
    logging.handlers.RotatingFileHandler('loger.log', encoding='utf8', backupCount=1),
    logging.StreamHandler(),
    #logging.handlers.MemoryHandler(capacity=9, flushLevel=logging.INFO, target=sys.stdout)
]




root_logger = logging.getLogger(__name__)

root_logger.setLevel(logging.DEBUG)

for h in handlers:
    h.setFormatter(f)
    h.setLevel(logging.INFO)
    root_logger.addHandler(h)

#print dir(root_logger)

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
    with open(file, 'r') as f:
        lines = []
        f.seek(0,2)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue
            lines.append(line)
            return lines

# while True:
#     print tail_generator('loger.log').next()