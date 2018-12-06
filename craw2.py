#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

#someone use this project you shoud change DRIVER_DIR  cuz your chromedriver.exe is not same point
DRIVER_DIR = "C:/Users/user/Desktop/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(DRIVER_DIR)
driver.implicitly_wait(1)

pagenum=1 #pagenumber
infonum=2 #cuz number start 2 not 1
cnt=1 #crawling number
while(pagenum<1):
    driver.get('https://www.thinkcontest.com/Contest/CateField.html?page='+str(pagenum)+'&s=ing')
    time.sleep(2)

    while(infonum<16):
