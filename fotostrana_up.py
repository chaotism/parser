#coding: utf-8
from __future__ import unicode_literals
import time
import datetime
import json
import os
from utils.logger import root_logger
from PyQt4 import QtCore
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchAttributeException, NoSuchElementException, \
    StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from utils.send_message import send_message

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
        self.get_cars()

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
    def get_cars(self):
        import random
        now = datetime.datetime.now()
        self.get_web_driver()

        auto_ru_url = "http://fotostrana.ru/signup/"
        self.driver.get(auto_ru_url)
        time.sleep(2)
        self.driver.find_element_by_class_name("signup-link-login").click()
        time.sleep(2)
        self.driver.find_element_by_id("user_email").send_keys('chaotism@mail.ru')
        self.driver.find_element_by_id("user_password").send_keys('herotizm')
        self.driver.find_element_by_id("loginPopupSubmitButton").click()
        time.sleep(10)
        self.driver.get(auto_ru_url)
        auto_ru_url = "http://fotostrana.ru/rating/?fromServiceBlock=0&ls=0&fsrating=photoid-2352143031+offset-0+album-ratingfeed+currentPhoto-0+pageSource-28"
        self.driver.get(auto_ru_url)
        logger.info(auto_ru_url)
        while True:
            #time.sleep(0.8)
           # "user_email"
            #self.driver.find_element_by_class_name("fsr-photo-like").click()
            try:
                random.choice((self.driver.find_element_by_id("fsr-unique-photo").click(),self.driver.find_element_by_class_name("fsr-photo-like").click()))
            except Exception, err:
                print err
            #self.driver.find_element_by_id("fsr-unique-photo").click()
            #self.driver.find_element_by_id("fsr-photo-like").click()
            if (datetime.datetime.now() - now).seconds > 300:
                now = datetime.datetime.now()
                time.sleep(random.randrange(20,60))
            time.sleep(0.8)

if __name__ == '__main__':
    c = CarCrawler()
    c.run()