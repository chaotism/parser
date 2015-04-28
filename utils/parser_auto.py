#coding: utf-8
from __future__ import unicode_literals
import time
import datetime
import json
import os
from logger import root_logger
from PyQt4 import QtCore
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchAttributeException, NoSuchElementException, \
    StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from send_message import send_message

logger = root_logger

DELAY = 120

class CarCrawler(QtCore.QThread):
    def __init__(self, parent=None):
        self.cars_search_form = {}
        try:
            if not os.path.exists("cars_list.txt"):
                with open("cars_list.txt", 'w+') as cars_list:
                    self.cars = json.load(cars_list)
            else:
                with open("cars_list.txt", 'r+') as cars_list:
                    self.cars = json.load(cars_list)
        except Exception, err:
            self.cars = {}
            logger.error(err)
        self.search_dict = {}
        QtCore.QThread.__init__(self, parent)
        self.running = False

    def run(self,  *args, **kwargs):
        self.running = True
        #while self.running:
        return self.get_cars(self.search_dict)

    def send_message(self, *args, **kwargs):
        return send_message(*args, **kwargs)

    def get_web_driver(self):
        try:
            driver = webdriver.Firefox()
        except Exception, err:
            logger.error(err)
            try:
                driver = webdriver.Chrome()
            except Exception, err:
                logger.error(err)
                driver = webdriver.Ie()
                raise
        self.driver = driver
        self.driver.implicitly_wait(5)
        return driver
    def get_cars(self, get_dict):
        auto_ru_url = "http://auto.ru/items/all/" \
                      "?search[geo_region]=%(search[geo_region])s" \
                      "&search[state]=%(search[state])s" \
                      "&search[mark][]=%(search[mark][])s" \
                      "&search[mark-folder][]=%(search[mark-folder][])s" \
                      "&search[price][min]=%(search[price][min])s" \
                      "&search[price][max]=%(search[price][max])s" \
                      "&search[year][min]=%(search[year][min])s" \
                      "&search[year][max]=%(search[year][max])s" \
                      "&search[period]=%(search[period])s" % get_dict
        logger.info(auto_ru_url)
        now = datetime.datetime.now()
        while True:
            try:
                self.driver.get(auto_ru_url)
            except Exception:
                self.get_web_driver()
                self.driver.get(auto_ru_url)
            while True:
                try:
                    time.sleep(2)
                    car_urls = self.driver.find_elements_by_xpath('.//table/tbody/tr/td/a')
                    for car in car_urls:
                        if car.get_attribute('href') not in self.cars:
                            logger.info('find new car')
                            logger.info(car.text)
                            logger.info(car.get_attribute('href'))
                            self.cars[car.get_attribute('href')] = {'name': car.text, 'sended': False}
                            with open("cars_list.txt", 'w+') as cars_file:
                                cars_dump = json.dump(self.cars, cars_file)
                    #todo:подумать как сделать правильный yield и перересовку интерфейса
                    #yield (car.get_attribute('href'), self.items[car.get_attribute('href')])
                    prev = './/div[@class="b-pager"]/span[@class="b-pager-ctrl b-pager-ctrl_next"]'
                    next = './/div[@class="b-pager"]/span[@class="b-pager-ctrl b-pager-ctrl_next"]'
                    #TODO: указать время с конфига
                    if (datetime.datetime.now() - now).seconds > DELAY:
                        now = datetime.datetime.now()
                        self.cars = self.send_message(get_dict['send_to'], get_dict['send_target'], self.cars)
                        with open("cars_list.txt", 'w+') as cars_file:
                            cars_dump = json.dump(self.cars, cars_file)
                            logger.info('cars_update')
                    next = self.driver.find_element_by_xpath(next).find_element_by_xpath('.//a')
                    next.click()
                except NoSuchElementException, err:
                    #logger.error(err)
                    break
                except Exception, err:
                    logger.error(err)
                    break
        self.driver.quit()
        logger.info('search_end')

the_end = datetime.date(2015, 1, 5)