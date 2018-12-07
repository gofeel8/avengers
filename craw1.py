#!/usr/bin/python3
#!/usr/bin/python3
#wevity contest
from selenium import webdriver
import time
import requests
import re

#someone use this project you shoud change DRIVER_DIR  cuz your chromedriver.exe is not same point
DRIVER_DIR = "C:/Users/user/Desktop/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(DRIVER_DIR)
driver.implicitly_wait(1)

pagenum=1 #pagenumber
infonum=2 #cuz number start 2 not 1
cnt=1 #crawling number

while(pagenum<=16):
    driver.get('https://www.wevity.com/?c=find&s=1&mode=ing&gp='+str(pagenum)+'')
    time.sleep(2)

    while(infonum<=16):
        try:
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[1]/div[2]/div[3]/div/ul/li['+str(infonum)+']/div[1]/a').click()

            URL=(driver.current_url)
            res=requests.get(URL)
            html=res.text

            time.sleep(1)


            #time.sleep(1)
            print("----- "+str(pagenum)+" page, "+str(infonum-1)+" information -----")
            # (공모전이름)
            re_title = re.compile(">(.*)</h6>", re.MULTILINE)
            title_tag = re_title.findall(html)
            print("title:")
            print('\n'.join(title_tag))

            #(주관)
            re_com = re.compile("주관</span>\s*(.*)\s*</li>", re.MULTILINE)
            com_tag = re_com.findall(html)
            print("com:")
            print('\n'.join(com_tag))

            #(기간)
            re_day = re.compile("기간</span>\s*(.*)\s*<span", re.MULTILINE)
            day_tag = re_day.findall(html)
            print("when:")
            print('\n'.join(day_tag))

            #(내용)
            re_info = re.compile("viewContents\">\s*(.*)</div>", re.MULTILINE)
            info_tag = re_info.findall(html)
            print("info:")

            info='\n'.join(info_tag)
            info=info.replace("/upload","https://www.wevity.com/upload")
            print(info)

            #(이미지)
            img_info = re.compile("<img src=\"(/upload/contest.*)\"\s*alt=\"공", re.MULTILINE)
            img_tag = img_info.findall(html)
            print("img:")

            img='\n'.join(img_tag)
            img=img.replace("/upload","https://www.wevity.com/upload")
            print(img)


            #(홈페이지)
            re_page = re.compile("홈페이지</span>\s*<a href=\"(.*?)\"", re.MULTILINE)
            page_tag = re_page.findall(html)
            print("page:")
            print('\n'.join(page_tag))

            cnt = cnt+1
            infonum=infonum+1

            driver.back()

        except NoSuchElementException:
            print("----------NoSuchElementException----------")
            #infonum=infonum+1
    infonum=2  #to reset num because we go next page
    pagenum=pagenum+1

print("total crawling num : "+str(cnt-1))

