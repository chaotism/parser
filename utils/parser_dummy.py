#coding: utf-8
from __future__ import unicode_literals
import time
import json
import logging
import os
import logging.handlers
from lib.selenium import webdriver
from lib.selenium.webdriver.common.keys import Keys
from lib.selenium.common.exceptions import TimeoutException, NoSuchAttributeException, StaleElementReferenceException
from lib.selenium.webdriver.support.ui import WebDriverWait
from lib.selenium.webdriver.common.action_chains import ActionChains
from lib.selenium.webdriver.support.select import Select


f = logging.Formatter(fmt='%(levelname)s:%(name)s: %(message)s '
    '(%(asctime)s; %(filename)s:%(lineno)d)',
    datefmt="%Y-%m-%d %H:%M:%S")
handlers = [
    logging.handlers.RotatingFileHandler('rotated.log', encoding='utf8',
        maxBytes=100000, backupCount=1),
    logging.StreamHandler()
]
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)

for h in handlers:
    h.setFormatter(f)
    h.setLevel(logging.INFO)
    root_logger.addHandler(h)

logger = logging.getLogger(__name__)

cwd = os.getcwd()
print cwd

# print os.path.exists("cars_list.txt")

cars = {}
cars_marks_and_models = {}
periods = {}
# cars_marks_dict = {}
# cars_models_dict = {}


try:
    if not os.path.exists("cars_list.txt"):
        with open("cars_list.txt", 'w+') as cars_list:
            cars = json.load(cars_list)
    else:
        with open("cars_list.txt", 'r+') as cars_list:
            cars = json.load(cars_list)
except Exception,err:
    cars = {}
    logger.error(err)

try:
    if not os.path.exists("cars_marks_and_models.txt"):
        with open("cars_marks_and_models.txt", 'w+') as cars_marks_and_models:
            cars_marks_and_models = json.load(cars_marks_and_models)
    else:
        with open("cars_marks_and_models.txt", 'r+') as cars_marks_and_models:
            cars_marks_and_models = json.load(cars_marks_and_models)
except Exception,err:
    cars_marks_and_models = {}
    logger.error(err)


try:
    if not os.path.exists("cities.txt"):
        with open("cities.txt", 'w+') as cities:
            cities = json.load(cities)
    else:
        with open("cities.txt", 'r+') as cities:
            cities = json.load(cities)
except Exception,err:
    cities = {}
    logger.error(err)

try:
    if not os.path.exists("regions.txt"):
        with open("regions.txt", 'w+') as regions:
            regions = json.load(regions)
    else:
        with open("regions.txt", 'r+') as regions:
            regions = json.load(regions)
except Exception,err:
    regions = {}
    logger.error(err)


try:
    if not os.path.exists("periods.txt"):
        with open("periods.txt", 'w+') as periods:
            periods = json.load(periods)
    else:
        with open("periods.txt", 'r+') as periods:
            periods = json.load(periods)
except Exception,err:
    periods = {}
    logger.error(err)


print cars
print cars_marks_and_models
print periods
print cities
print regions
driver = webdriver.Firefox()
# driver = webdriver.Chrome()
driver.get('http://auto.ru/items/all/?search[state]=1&search[geo_region]=89&search[custom]=1&show_sales=1&advanced_search=1&search[period]=0&search[country_group_id][1]=1&search[price][min]=100+000&search[price][max]=200+000&search[year][min]=2005&search[year][max]=2006')

for i in xrange(1,1000):
    driver.get('http://auto.ru/items/all/?search[state]=1&search[custom]=1&show_sales=1&advanced_search=1&search[geo_country]=&search[geo_region]=%s'%i)
    regions = driver.find_element_by_css_selector('label.dashed')
    time.sleep(1)
    #regions = driver.find_element_by_css_selector('li.geo-open-trigger.geo-regions.filter-list-items.geo-item-regions-1 > label.dashed')
    print regions.text
    print i
    #li.geo-open-trigger.geo-regions.filter-list-items.geo-item-regions-1 > label
    if regions.text not in cities:
        cities[regions.text] = i
        with open("regions.txt", 'w+') as regions_file:
            cities_write = json.dump(cities, regions_file)
    # else:
    #     break

for i in xrange(1,1000):
    driver.get('http://auto.ru/items/all/?search[state]=1&search[custom]=1&show_sales=1&advanced_search=1&search[geo_country]=&search[geo_region]=&search[geo_city]=%s'%i)
    city = driver.find_element_by_css_selector('label.dashed')
    time.sleep(1)
    #city = driver.find_element_by_css_selector('li.geo-open-trigger.geo-city.filter-list-items.geo-item-city-1 > label.dashed')
    print city.text
    print i
    #li.geo-open-trigger.geo-city.filter-list-items.geo-item-city-1 > label
    if city.text not in cities:
        cities[city.text] = i
        with open("cities.txt", 'w+') as cities_file:
            cities_write = json.dump(cities, cities_file)
    # else:
    #     break



driver.get('http://auto.ru/items/all/?search%5Bstate%5D=1&search%5Bcustom%5D=1&show_sales=1&advanced_search=1')
try:
    logger.info(driver.title)
    logger.info(driver.current_url)
except:
    pass

period_selector = driver.find_element_by_xpath('//select[@name="search[period]"]')
period_selector.click()
period_selector_list = period_selector.find_elements_by_xpath('.//option')
for period in period_selector_list:

    #if i == 5:break
    #print car_mark.text
    #print car_mark.get_attribute('value')
    #.is_displayed()
    logger.info(period.text, period.get_attribute('value'))
    if period.text not in periods:
        periods[period.text] = period.get_attribute('value')
        logger.info(period.text, period.get_attribute('value'))


        with open("periods.txt", 'w+') as periods_file:
             periods_dump = json.dump(periods, periods_file)

# cars_marks = driver.find_element_by_xpath('//select[@name="search[mark][]"]')
cars_marks_selector = driver.find_element_by_xpath('//select[@name="search[mark][]"]')
cars_marks_selector.click()
cars_marks_list = cars_marks_selector.find_elements_by_xpath('.//option')
# cars_marks = driver.find_element_by_name('search[mark][]')

#print cars_marks.text
# cars_marks.click()
# cars_marks_list = cars_marks.find_elements_by_tag_name('option')
# cars_marks_list = cars_marks.find_elements_by_xpath('.//option')
#//*[@id="filter"]/fieldset/div[1]/div/div[2]/div/div[1]/select/option[1]
# print cars_marks
#logger TypeError
#StaleElementReferenceException


for car_mark in cars_marks_list:

    #if i == 5:break
    #print car_mark.text
    #print car_mark.get_attribute('value')
    #.is_displayed()
    logger.info(car_mark.text, car_mark.get_attribute('value'))
    if car_mark.text not in cars_marks_and_models:
        cars_marks_and_models[car_mark.text] = {'id':car_mark.get_attribute('value'), 'models':{}}
        logger.info(car_mark.text, car_mark.get_attribute('value'))
    # else:
    #     continue
    #Select(cars_marks_list).select_by_value(car_mark.get_attribute('value'))
    try:

        Select(cars_marks_selector).select_by_value(car_mark.get_attribute('value'))
        models_this_mark_selector = driver.find_element_by_xpath('//select[@name="search[mark-folder][]"]')
        models_this_mark_selector.click()
        #Select(models_this_mark).select_by_value(car_mark.get_attribute('value'))
        models_this_mark_list = models_this_mark_selector.find_elements_by_xpath('.//option')

    except (AttributeError,Exception),err:
        print err
        logger.error(err)
        models_this_mark = []

    for model in models_this_mark_list:
        try:
            print model.text
            logger.info(model.text)
            #Select(models_this_mark_selector).select_by_value(model.get_attribute('value'))
            if model.text not in cars_marks_and_models[car_mark.text]['models']:
                cars_marks_and_models[car_mark.text]['models'][model.text] = model.get_attribute('value')
                logger.info(model.text, model.get_attribute('value'))
                with open("cars_marks_and_models.txt", 'w+') as cars_marks_and_models_file:
                    cars_marks_and_models_dump = json.dump(cars_marks_and_models, cars_marks_and_models_file)
                #logger.info(car_mark.text, cars_marks_and_models[car_mark.text])
        except (TypeError,StaleElementReferenceException),err:
            logger.error(err)






submit_search = driver.find_element_by_xpath('//*[@id="all7_sale_filter_submit"]')
submit_search.submit()
# driver.quit()



# opTimeout = 5
# page = driver
# WebDriverWait(page, opTimeout).until(lambda element:
#     (element.find_element_by_xpath("//div[@id='main']/..//div[contains(text(), 'Основные параметры')]")) and
#     (element.find_element_by_xpath("//div[@id='main']/..//input[@id='save']")), 'Таймаут! Элементы на форме не появились!')



#submit_search.click()
#/html/body/div[1]/div[2]/article/div[2]/div[1]/div[1]/div[12]/div/span[3]
# #body > div.branding_fix > div.content.content_style > article > div.clearfix > div.b-page-wrapper > div:nth-child(1) > div.pager-box > div > span.b-pager-ctrl.b-pager-ctrl_next
# next_url = driver.find_element_by_css_selector('body > div.branding_fix > div.content.content_style > article > div.clearfix > div.b-page-wrapper > div:nth-child(1) > div.pager-box > div > span.b-pager-ctrl.b-pager-ctrl_next')
# # next_url = driver.find_elements_by_css_selector('div >span.b-pager-ctrl.b-pager-ctrl_next')
# next_url1 = driver.find_elements_by_xpath('.//*[@class="b-pager"]')
# # next_url1 = driver.find_elements_by_class_name('b-pager-ctrl')
# next_url11 = driver.find_elements_by_class_name('b-pager-ctrl_next')
# print next_url
# print next_url1
# print


"""
#Метод perform() - выполнение сохраненных действий
#Примеры использования:
# Переместить мышь на пункт меню и подождать выпадающее меню:
administrationTab = page.find_element_by_xpath("//ul[@class='dropdown']/li[11]/div") # Ищем выпадающее меню.
hover = ActionChains(page).move_to_element(administrationTab) # Сохраняем действие в объекте ActionChains.
hover.perform() # применяем действие
# Ждем, пока выпадающее меню не откроется, то есть не станет видимой одна из его ссылок:
WebDriverWait(page, opTimeout).until(
    lambda el: el.find_element_by_xpath("//a[@href='/polidon2/ScheduledEntity']").is_displayed(),
    'Timeout while we are wait pop-up menu.')

#Метод is_displayed() - проверка видимости элемента
#Примеры использования:
# 1. Определение того, является ли элемент, найденный по xpath, видимым на форме:
element = page.find_element_by_xpath("//div[@id='treeWrapper']") # В данном случае определяется, виден ли выпадающий список
flag = element.is_displayed() # flag = True - если элемент видим, flag = False - если нет
# Или можно сразу:
flag = page.find_element_by_xpath("//div[@id='treeWrapper']").is_displayed()
# 2. Использование в блоке ожидания появления элемента на форме:
WebDriverWait(page, 5).until(
    lambda element: element.find_element_by_xpath("//div[@id='treeWrapper']").is_displayed(),
    'Timeout while waiting popup-tree list.') # Ждём 5 сек. пока не появится выпадающий список, иначе - п
"""



while True:
    car_urls = driver.find_elements_by_xpath('.//table/tbody/tr/td/a')
    for car in car_urls:
        if car.get_attribute('href') not in cars:
            logger.info('find new car')
            logger.info(car.text)
            logger.info(car.get_attribute('href'))
            cars[car.get_attribute('href')]={'name':car.text, 'sended':False}
            #print items
            with open("cars_list.txt", 'w+') as cars_file:
                 cars = json.dump(cars, cars_file)
    try:
#body > div.branding_fix > div.content.content_style > article > div.clearfix > div.b-page-wrapper > div:nth-child(1) > div.pager-box > div > span.b-pager-ctrl.b-pager-ctrl_next
        next = driver.find_element_by_xpath('.//div[@class="b-pager"]/span[@class="b-pager-ctrl b-pager-ctrl_next"]').find_element_by_xpath('.//a')
        # print dir(next)
        # print next.location
        # print next.parent
        # print next.tag_name
        # print next.id
        # next.click()
    except Exception,err:
        logger.error(err)
        break

    #cars_list.write(json.dumps(items))

driver.quit()
exit()

# list_links = driver.find_elements_by_tag_name('a')
# for i in list_links:
#     print i.get_attribute('href')
#     print i.text
driver.quit()


# try:
#     # we have to wait for the page to refresh, the last thing that seems to be updated is the title
#     WebDriverWait(driver, 10).until(lambda driver : driver.title.lower().startswith("cheese!"))
#
#     # You should see "cheese! - Google Search"
#     logger.info(driver.title)
# except Exception,err:
#     logger.error(err)
#
# finally:
#     driver.quit()
