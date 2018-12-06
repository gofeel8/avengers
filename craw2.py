#!/usr/bin/python3
#thinkgood contest
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
infonum=1 #cuz number start 2 not 1
cnt=1 #crawling number
print("1")
while(pagenum<3):
    driver.get('https://www.thinkcontest.com/Contest/CateField.html?page='+str(pagenum)+'&s=ing')
    time.sleep(2)
    print("2")
    while(infonum<=10):
        try:
            print("----- "+str(pagenum)+" page, "+str(infonum)+" information -----")
            time.sleep(1)

            driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/table/tbody/tr['+str(infonum)+']/td[1]/div[1]/a').click()

            info = driver.find_element_by_class_name("type-5")
            detail = driver.find_element_by_class_name("info-cont")

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
    infonum=1  #to reset num because we go next page
    pagenum=pagenum+1

print("total crawling num : "+str(cnt-1))

#여기서 접수기간 2018-12-05 ~ 2018-12-30 D-24 에서 정규표현식 써서 D뒤에 -이면 ㅇㅋ 아니면 무시




