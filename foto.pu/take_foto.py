# coding: utf-8
from __future__ import unicode_literals
import sys
import datetime
import json
import os
import urllib
import logging
import logging.handlers
import random
from selenium import webdriver


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

logger = root_logger

DELAY = 120


class ItemsCrawler(object):
    def __init__(self, parent=None):
        self.search_form = {}
        try:
            if not os.path.exists("search_list.txt"):
                with open("search_list.txt", 'w+') as items_list:
                    self.items = json.load(items_list)
            else:
                with open("search_list.txt", 'r+') as items_list:
                    self.items = json.load(items_list)
        except Exception, err:
            self.items = {}
            logger.error(err)
        self.search_dict = {}
        self.running = False

    def run(self, url, *args, **kwargs):
        # self.running = True
        # url = args[0]
        # target =args[0][1]
        # print url
        # print target
        # print args
        images = self.get_items(url=url, target='img')
        # for image in images:
        #     print dir(image)
        #     print image.id
        #     print image.text
        #     print image.tag_name
        #     print image.parent
        #     print image.location
        #     print dir(image.parent)
        #     print image.parent.get()
        #     try:
        #         image.click()
        #     except Exception,err:
        #         logger.error(err)
        #         self.driver.back()
        #         continue
        images_src = [x.get_attribute('src') or x.get_attribute('href') for x in images]
        self.get_image(images_src)
        self.driver.quit()

    def get_image(self, images_src):
        for image in images_src:
            try:
                img = urllib.urlopen(image)
                img_name = image.split('/')[-1]
                with open(img_name, "wb") as code:
                    code.write(img.read())
            except Exception, err:
                logger.error(err)
                continue

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


    def get_items(self, url=None, target='', by='by_tag_name'):
        if not url:
            raise Exception('Need url to parse')
        if not target:
            raise Exception('Need target to parse')
        logger.info(url)
        now = datetime.datetime.now()
        try:
            self.driver.get(url)
        except Exception:
            self.get_web_driver()
            self.driver.get(url)
        items = {}
        items['by_xpath'] = self.driver.find_elements_by_xpath
        items['by_tag_name'] = self.driver.find_elements_by_tag_name
        items['by_id'] = self.driver.find_elements_by_id
        items['by_class_name'] = self.driver.find_elements_by_class_name
        items['by_css_selector'] = self.driver.find_elements_by_css_selector
        #print items[by](target)
        logger.debug(items[by](target))
        #TODO:переделать
        if target=='img':
            return self.driver.find_elements_by_xpath('//a[child::img]')+self.driver.find_elements_by_xpath('//img')
        return items[by](target)


if __name__ == '__main__':
    c = ItemsCrawler()
    args = sys.argv[1:]
    url = str(raw_input("Введите адрес страницы: "))
    print args
    c.run(url)