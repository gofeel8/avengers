import time
import csv
import pandas as pd
from konlpy.tag import Twitter
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
# csvFile = open("D:/Download/for_csv.csv", "w", encoding = 'UTF16')
# writer = csv.writer(csvFile
DRIVER_DIR = "C:/Users/user/Desktop/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(DRIVER_DIR)
driver.implicitly_wait(3)
driver.get('https://www.instagram.com/explore/tags/명동맛집/')
elem = driver.find_element_by_tag_name("body")
def for_pos(image):
    temp = tw.pos(image.get_attribute('alt'), norm=True)
    return temp 
def Go_page(a, b):
    txtFile = open("C:/Users/user/Desktop/연습용.txt", "a", encoding='UTF16')
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/article/div[1]/div/div/div['+str(a)+']/div['+str(b)+']/a/div/div[2]'
    ).click()
    time_to = driver.find_elements_by_css_selector('a.c-Yi7 > time')
    for q in time_to:
        print(q.get_attribute('datetime'))
        txtFile.write(str(q.get_attribute('datetime')))
        txtFile.write(',')
    Create_text()
    time.sleep(1)
    txtFile.close()
    driver.back()
 

def Go_page_2(a, b):
    driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]'
            #'//*[@id="react-root"]/section/main/article/div[2]/div/div[7]/div[1]/a/div/div[2]'
        ).click()
    c = 1
    while(c < 5):
        try:
            data = 1
            time.sleep(3)
            driver.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[1]/a'
            ).click()
            time.sleep(1)

            if data == 1:
                driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div/section/div/a/span').click()                
                print("lang값출력중")
                #lang = driver.find_element_by_xpath("//li[@class]=' LH36I'/a")
                lang = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').text
                #lang = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/h1').text // 아이디 출력
                print (lang)
                
            txtFile = open("C:/Users/user/Desktop/연습용.txt", "a", encoding='UTF16')
            time_to = driver.find_elements_by_css_selector('a.c-Yi7 > time')
            for q in time_to:
                date = q.get_attribute('datetime')
            #print (a)
            txtFile.write(str(q.get_attribute('datetime')))
            txtFile.write(",")
            #print (driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/div[2]/div[2]/a').text)
            driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div/a[2]').click()
            Create_text()
            time.sleep(1)
            print ("현재 ",c ,"번째 게시글을 크롤링중입니다")
            c = c + 1
            txtFile.close()
        except NoSuchElementException:
            driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div/a').click()
            time_to = driver.find_elements_by_css_selector('a.c-Yi7 > time')
            txtFile = open("C:/Users/user/Desktop/연습용.txt", "a", encoding='UTF16')
            for q in time_to:
                date = q.get_attribute('datetime')
            txtFile.write(str(q.get_attribute('datetime')))
            txtFile.write(",")
            print (driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/div[2]/div[2]/a').text)
            print("[예외 발생]")
            driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div/a[2]').click()    
            lang = driver.find_element_by_xpath("//div[@class = 'C4VMK']/span").text
            print(lang)
            Create_text()
            time.sleep(1)
            print ("현재 ",c ,"번째 게시글을 크롤링중입니다")
            c = c + 1
            txtFile.close()
        except StaleElementReferenceException:
            Go_page_2(a,b+1)
    return c

def Create_text():
    txtFile = open("C:/Users/user/Desktop/연습용.txt", "a", encoding='UTF16')
    #driver.find_elements_by_css_selector('div.KL4Bh > img')
    # 브라우저에 보이는 모든 img 태그를 css 선택자 문법으로 찾는다.
    lang = driver.find_element_by_xpath("//div[@class = 'C4VMK']/span").text
    #print(lang)   
    # 위에서 선언한 alt_list 리스트에 alt 속성의 값을 중복을 방지하며 할당한다.
    for data in lang:
        temp_Content = []
        #print (i.get_attribute('alt')
        if (data == "\ud83d"):
            continue
        elif (data == "\ud83e"):
            continue
        elif (data == "\ud83c"):
            continue
        elif (data == "\n"):
            continue
        elif (data == ","):
            continue
        else:
            temp_Content.append(data)
        a = "".join(temp_Content)
    #if lang.find('행복') != -1:
        txtFile.write(str(a))
    txtFile.write('\n')
    txtFile.close()

alt_list = []
tw = Twitter()
pagedowns = 1

for i in range(1, 3):
    elem.send_keys(Keys.PAGE_DOWN)

# 페이지 스크롤 타이밍을 맞추기 위해 sleep
time.sleep(2)
"""if pagedowns == 1:
    for i in range(3,4):
        for j in range(1,3):
            Go_page(i, j)"""

number = Go_page_2(1,1)
print ("게시물의 수는 : ", number , "입니다")
print("txt 파일 생성 완료")

driver.close()
 
