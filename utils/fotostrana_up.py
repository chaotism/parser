#coding: utf-8
from __future__ import unicode_literals
import time
import datetime
from utils.logger import root_logger
from PyQt4 import QtCore
from selenium import webdriver


logger = root_logger


class FotoStranaClicker(QtCore.QThread):
    sign_url = "http://fotostrana.ru/signup/"
    target_url = "http://fotostrana.ru/rating/?fromServiceBlock=0&ls=0&fsrating=photoid-2352143031+offset-0+album-ratingfeed+currentPhoto-0+pageSource-28"

    def __init__(self, login, password, parent=None):
        self.login = login
        self.password = password
        QtCore.QThread.__init__(self, parent)
        self.running = False

    def run(self,  *args, **kwargs):
        self.running = True
        self.get_clicks()

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

    def get_clicks(self):
        import random
        now = datetime.datetime.now()
        self.get_web_driver()
        self.driver.get(self.sign_url)
        time.sleep(2)
        self.driver.find_element_by_class_name("signup-link-login").click()
        time.sleep(2)  # TODO: переделать sleeps
        self.driver.find_element_by_id("user_email").send_keys('chaotism@mail.ru')
        self.driver.find_element_by_id("user_password").send_keys('herotizm')
        self.driver.find_element_by_id("loginPopupSubmitButton").click()
        time.sleep(10)
        self.driver.get(self.sign_url)
        self.driver.get(self.target_url)
        logger.info(self.target_url)
        while True:
            try:
                random.choice((self.driver.find_element_by_id("fsr-unique-photo").click(),self.driver.find_element_by_class_name("fsr-photo-like").click()))
            except Exception, err:
                print err
            if (datetime.datetime.now() - now).seconds > 300:
                now = datetime.datetime.now()
                time.sleep(random.randrange(20,60))
            time.sleep(0.8)


if __name__ == '__main__':
    login = raw_input("input login: ")
    password = raw_input("input password: ")
    c = FotoStranaClicker(login, password)
    c.run()