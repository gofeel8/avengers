#!/usr/bin/python3
import time
import csv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

driver = webdriver.Chrome(DRIVER_DIR)
driver.implicitly_wait(3)

n=1
a=1
while(n<20):
    driver.get('https://www.wevity.com/?c=find&s=1&mode=ing&gp='+str(n)+' ')
    n=n+1
    time.sleep(2)
    #hashtag = driver.find_elements_by_css_selector('div.tit-area > h6')
    while(a<16):
        driver.find_elements_by_xpath('//*[@id="container"]/div[2]/div[1]/div[2]/div[3]/div/ul/li['+str(a)+']/div[1]/a').click()
        a=a+1
        #hashtag = driver.find_elements_by_css_selector('div.tit-area > h6')
        #for q in hashtag:
        #    print(q._get_attribute('content'))

#pre_elem = driver.find_element_

