#!/usr/bin/python3
import time
import csv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
DRIVER_DIR = "c:/Users/user/Desktop/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(DRIVER_DIR)
driver.implicitly_wait(3)
driver.get('https://www.wevity.com/?c=find&s=1&mode=ing&gp=1')
a=2
c=1
hashtag = driver.find_elements_by_css_selector('div.tit > a')

#hashtag = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[1]/div[2]/div[3]/div/ul/li[3]/div[1]/a').text

for q in hashtag:
    #txtFile1 = open("C:/Users/user/Desktop/b.txt","a")#encodint = 'UTF16'
    #txtFile2 = open("C:/Users/user/Desktop/b.txt","a")#encodint = 'UTF16'
    #print(q.text)
    #txtFile1.write(str(q.text))
    #txtFile1.write(',')
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[1]/div[2]/div[3]/div/ul/li['+str(a)+']/div[1]/a').click()
    hashname = driver.find_elements_by_css_selector('div.tit-area > /h6')
    for q in hashname:
        print(q1.text)
    a=a+1
    time.sleep(1)
    driver.back()
    time.sleep(1)
    #txtFile2.write(str(q.text))
    #txtFile2.write(',')
"""
while(c<6):
    try:
        data=1
        time.sleep(1)
        for q in hashtag:
        driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[1]/div[2]/div[3]/div/ul/li['+str(a)+']/div[1]/a').click()
        time.sleep(1)

        if data ==1:
            print("a")
"""

