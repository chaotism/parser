#!/usr/bin/python
# coding=utf-8
from __future__ import unicode_literals
import sys
import os
import json
from qt.parser_qt import QtGui, ParserForm
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = ParserForm()
    myapp.setWindowTitle("Парсер auto.ru")
    myapp.show()
    sys.exit(app.exec_())