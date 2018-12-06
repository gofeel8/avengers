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

pagenum=1 #pagenumber
infonum=2 #cuz number start 2 not 1
cnt=1
#field = driver.find_element_by_css_selector('div.tit-area > h6')
#who = driver.find_element_by_css_selector('div.tit-area > h6')
#organization =driver.find_element_by_css_selector('div.tit-area > h6')
#homepage = driver.find_element_by_css_selector('div.tit-area > h6')


while(pagenum<2):
    driver.get('https://www.wevity.com/?c=find&s=1&mode=ing&gp='+str(pagenum)+'')
    time.sleep(2)

    while(infonum<16):
        try:
            print("----- "+str(pagenum)+" page, "+str(infonum-1)+" information -----")
            time.sleep(1)

            driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[1]/div[2]/div[3]/div/ul/li['+str(infonum)+']/div[1]/a').click()

            info = driver.find_element_by_class_name("cd-info-list")
            detail = driver.find_element_by_class_name("comm-desc")
            """
            txtfile_info=open("C:/Users/user/Desktop/aven_info.txt", "a", encoding='UTF16')
            txtfile_detail=open("C:/Users/user/Desktop/aven_detail.txt", "a", encoding='UTF16')

            for q1 in info:
                infotext = q1.text
            txtfile_info.write(str(infotext))
            txtfile_info.write(",")

            for q2 in detail:
                detailtext = q2.text
            txtfile_detail.write(str(detailtext))
            txtfile_detail.write(",")
            """
            print("                      -------------   list   ------------- \n")
            print(info.text)
            print("                      -------------  article ------------- \n")
            print(detail.text)

            cnt = cnt+1
            infonum=infonum+1

            driver.back()

        except NoSuchElementException:
            print("----------NoSuchElementException----------")
            infonum=infonum+1
    infonum=2  #to reset num because we go next page
    pagenum=pagenum+1

print("total crawling num : "+str(cnt))
