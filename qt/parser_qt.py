#!/usr/bin/python
# coding=utf-8
from __future__ import unicode_literals
import sys
import os
import json
import time
import datetime

from PyQt4 import QtGui, QtCore

from .search_form import Ui_Dialog
from .search_form_large import Ui_Auto_ru_parser
from utils.parser_auto import CarCrawler
from utils.logger import root_logger, tail, tail_generator
from utils.simple_thread import SimpleThread

logger = root_logger

try:
    if not os.path.exists("./config/cars_marks_and_models.txt"):
        with open("../config/cars_marks_and_models.txt", 'w+') as cars_marks_and_models:
            cars_marks_and_models = json.load(cars_marks_and_models)
    else:
        with open("./config/cars_marks_and_models.txt", 'r+') as cars_marks_and_models:
            cars_marks_and_models = json.load(cars_marks_and_models)
except Exception, err:
    cars_marks_and_models = {}
    logger.error(err)

try:
    if not os.path.exists("./config/cars_marks_and_models.txt"):
        with open("./config/cars_marks_and_models.txt", 'w+') as cars_marks_and_models:
            cars_marks_and_models = json.load(cars_marks_and_models)
    else:
        with open("./config/cars_marks_and_models.txt", 'r+') as cars_marks_and_models:
            cars_marks_and_models = json.load(cars_marks_and_models)
except Exception, err:
    cars_marks_and_models = {}
    logger.error(err)

try:
    if not os.path.exists("./config/cities.txt"):
        with open("./config/cities.txt", 'w+') as cities:
            cities = json.load(cities)
    else:
        with open("./config/cities.txt", 'r+') as cities:
            cities = json.load(cities)
except Exception, err:
    cities = {}
    logger.error(err)

try:
    if not os.path.exists("./config/periods.txt"):
        with open("./config/periods.txt", 'w+') as periods:
            periods = json.load(periods)
    else:
        with open("./config/periods.txt", 'r+') as periods:
            periods = json.load(periods)
except Exception, err:
    periods = {}
    logger.error(err)

try:
    if not os.path.exists("./config/states.txt"):
        with open("./config/states.txt", 'w+') as states:
            states = json.load(states)
    else:
        with open("./config/states.txt", 'r+') as states:
            states = json.load(states)
except Exception, err:
    states = {}
    logger.error(err)

try:
    if not os.path.exists("./config/send_to.txt"):
        with open("./config/send_to.txt", 'w+') as send_to:
            send_to = json.load(send_to)
    else:
        with open("./config/send_to.txt", 'r+') as send_to:
            send_to = json.load(send_to)
except Exception, err:
    send_to = {}
    logger.error(err)


class Logger(object):
    def __init__(self, output):
        self.output = output

    def write(self, string):
        if not (string == "\n"):
            trstring = QtGui.QApplication.translate("MainWindow", string.strip(), None, QtGui.QApplication.UnicodeUTF8)
        self.output.append(trstring)


class ParserUi(Ui_Dialog, QtCore.QObject):
    def __init__(self, parent=None):
        super(ParserUi, self).__init__()


class ParserForm(QtGui.QWidget):
    def __init__(self, parent=None):
        super(ParserForm, self).__init__(parent)
        self.setWindowTitle("Парсер auto.ru")
        self.ui = Ui_Auto_ru_parser()
        self.ui.setupUi(self)
        sizePolice = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolice.setHeightForWidth(True)
        self.setSizePolicy(sizePolice)
        # from utils.parser_auto import the_end  #
        # end = the_end - datetime.date.today()
        # self.ui.weblog.append('Времени для использования осталось %s дня'%(end.days))
        # if end.days < 0:
        #     self.logger.info('Времени использования не осталось')
        #     print 'Времени использования не осталось'
        #     exit()
        self.logger = Logger(self.ui.weblog)
        self.ui.weblog.append(tail('logger.log'))
        self.ui.period.addItems(sorted(periods.keys()))
        self.ui.geo_city.addItems(sorted(cities.keys()))
        self.ui.mark.addItems(sorted(cars_marks_and_models.keys()))
        self.ui.mark_folder.addItems(
            sorted(cars_marks_and_models[sorted(cars_marks_and_models.keys())[0]]['models'].keys()))
        self.ui.state.addItems(sorted(states.keys()))
        self.ui.send_to.addItems(sorted(send_to.keys()))
        self.ui.weblog.setReadOnly(True)
        self.ui.weblog.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.connect(self.ui.mark, QtCore.SIGNAL("activated(const QString&)"), self.change_mark)
        self.connect(self.ui.search, QtCore.SIGNAL("clicked()"), self.start_search)
        self.thread = CarCrawler()
        self.log_to_console(thr_start=True)

    def change_mark(self, mark):
        mark = unicode(mark)
        self.ui.mark_folder.clear()
        self.ui.mark_folder.addItems(cars_marks_and_models[mark]['models'].keys())

    def start_search(self):
        logger.info('search started')
        get_dict = {}
        get_dict['search[mark][]'] = cars_marks_and_models[unicode(self.ui.mark.currentText()).strip()]['id']
        try:
            get_dict['search[mark-folder][]'] = \
                cars_marks_and_models[unicode(self.ui.mark.currentText()).strip()]['models'][
                    unicode(self.ui.mark_folder.currentText())]
        except KeyError:
            logger.error('Неккорректное название марки')
            return
        # print dir(self.ui.send_target)
        get_dict['search[year][min]'] = unicode(self.ui.year_min.text()).strip()
        get_dict['search[year][max]'] = unicode(self.ui.year_max.text()).strip()
        get_dict['search[price][min]'] = unicode(self.ui.price_min.text()).strip()
        get_dict['search[price][max]'] = unicode(self.ui.price_max.text()).strip()
        get_dict['search[state]'] = states[unicode(self.ui.state.currentText())]
        get_dict['search[period]'] = periods[unicode(self.ui.period.currentText())]
        get_dict['search[geo_region]'] = cities[unicode(self.ui.geo_city.currentText())]
        get_dict['send_to'] = send_to[unicode(self.ui.send_to.currentText()).strip()]
        get_dict['send_target'] = unicode(self.ui.send_target.text()).strip()
        # self.thread.get_cars(get_dict)
        self.thread.search_dict = get_dict
        self.connect(self.ui.search, QtCore.SIGNAL("clicked()"), self.start_search)
        if self.thread.running:
            # self.thread.thr_stop()
            if hasattr(self.thread, 'driver'):
                self.thread.driver.quit()
            self.thread.wait(2000)
            self.thread.terminate()
        self.thread.start()

    @SimpleThread
    def log_to_console(self):
        import sys
        while True:
            f = sys.stderr
            sys.stderr.mode = 'r'
            print sys.stderr.mode
            if f.readline():
                print f.readline()
            else:
                time.sleep(1)
                continue


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = ParserForm().setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    myapp.setWindowTitle("Парсер auto.ru")
    myapp.show()
    sys.exit(app.exec_())
