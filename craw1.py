#!/usr/bin/python3
import time
import csv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
DRIVER_DIR = "C:/Users/user/Desktop/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(DRIVER_DIR)
driver.implicitly_wait(1)
n=1
a=2
c=2
#field = driver.find_element_by_css_selector('div.tit-area > h6')
#who = driver.find_element_by_css_selector('div.tit-area > h6')
#organization =driver.find_element_by_css_selector('div.tit-area > h6')
#homepage = driver.find_element_by_css_selector('div.tit-area > h6')


while(n<20):
    driver.get('https://www.wevity.com/?c=find&s=1&mode=ing&gp='+str(n)+' ')
    time.sleep(2)
    print("---------------"+str(n)+"번째 페이지--------------")
    #hashtag = driver.find_elements_by_css_selector('div.tit-area > h6')
    while(a<16):
        try:
            driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[1]/div[2]/div[3]/div/ul/li['+str(a)+']/div[1]/a').click()
            test1 = driver.find_element_by_class_name("cd-info-list")
            time.sleep(1)
            print(test1.text)
            print("---------------------------- \n")
            a=a+1
            driver.back()

        except NoSuchElementException:
            print("----------NoSuchElementException----------")
            a=a+1
    a=c
    n=n+1
        #hashtag = driver.find_elements_by_css_selector('div.tit-area > h6')
        #for q in hashtag:
        #    print(q._get_attribute('content'))
