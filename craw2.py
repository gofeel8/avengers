#!/usr/bin/python3
#wevity contest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import requests
import re

#someone use this project you shoud change DRIVER_DIR  cuz your chromedriver.exe is not same point
DRIVER_DIR = "C:/Users/user/Desktop/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(DRIVER_DIR)
driver.implicitly_wait(1)
endcheck = True#if information number is done it change False
pagenum=1 #pagenumber
infonum=2 #cuz number start 2 not 1
cnt1=0 #wevity crawling number
cnt2=0 #thinkgood crawling number

#-------------------------------------------------------------------------------------
#------------------wevity server receipt crawling ----------------------------------------------------
while(endcheck):    
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
                    
            print("----- receipt page "+str(pagenum)+" page, "+str(infonum-1)+" information -----")
            # (공모전이름)
            re_title = re.compile(">(.*)</h6>", re.MULTILINE)
            title_tag = re_title.findall(html)
            print("title:")
            print('\n'.join(title_tag))

            #(organization)
            re_com = re.compile("주관</span>\s*(.*)\s*</li>", re.MULTILINE)
            com_tag = re_com.findall(html)
            print("com:")
            print('\n'.join(com_tag))

            #(term)
            re_day = re.compile("기간</span>\s*(.*)\s*<span", re.MULTILINE)
            day_tag = re_day.findall(html)
            print("when:")
            print('\n'.join(day_tag))

            #(information)
            re_info = re.compile("viewContents\">\s*(.*)</div>", re.MULTILINE)
            info_tag = re_info.findall(html)
            print("info:")

            info='\n'.join(info_tag)
            info=info.replace("/upload","https://www.wevity.com/upload")
            print(info)

            #(image)
            img_info = re.compile("<img src=\"(/upload/contest.*)\"\s*alt=\"공", re.MULTILINE)
            img_tag = img_info.findall(html)
            print("img:")

            img='\n'.join(img_tag)
            img=img.replace("/upload","https://www.wevity.com/upload")
            print(img)


            #(homepage)
            re_page = re.compile("홈페이지</span>\s*<a href=\"(.*?)\"", re.MULTILINE)
            page_tag = re_page.findall(html)
            print("page:")
            print('\n'.join(page_tag))

            cnt = cnt+1
            
            
            infonum=infonum+1

            driver.back()
            
        except NoSuchElementException:# if pagenum == None 
            endcheck = False
            break
    infonum=2  #to reset num because we go next page
    pagenum=pagenum+1
    
    if endcheck == False:
        print("receipt crawling is finish ")
        break
#-------------------------------------------------------------------------------------
#------------------wevity server to be receipt crawling ----------------------------------------------------

endcheck = True

pagenum2=1
infonum2=2
while(endcheck):
    driver.get('https://www.wevity.com/?c=find&s=1&mode=future&gp='+str(pagenum2)+'')
    time.sleep(2)

    while(infonum2 <=16):
        try:
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[1]/div[2]/div[3]/div/ul/li['+str(infonum2)+']/div[1]/a').click()
            URL=(driver.current_url)
            res=requests.get(URL)
            html=res.text
            
            time.sleep(1)
                    
            print("-----to be receipt "+str(pagenum2)+" page, "+str(infonum2-1)+" information -----")
            # (공모전이름)
            re_title = re.compile(">(.*)</h6>", re.MULTILINE)
            title_tag = re_title.findall(html)
            print("title:")
            print('\n'.join(title_tag))

            #(organization)
            re_com = re.compile("주관</span>\s*(.*)\s*</li>", re.MULTILINE)
            com_tag = re_com.findall(html)
            print("com:")
            print('\n'.join(com_tag))

            #(term)
            re_day = re.compile("기간</span>\s*(.*)\s*<span", re.MULTILINE)
            day_tag = re_day.findall(html)
            print("when:")
            print('\n'.join(day_tag))

            #(information)
            re_info = re.compile("viewContents\">\s*(.*)</div>", re.MULTILINE)
            info_tag = re_info.findall(html)
            print("info:")

            info='\n'.join(info_tag)
            info=info.replace("/upload","https://www.wevity.com/upload")
            print(info)

            #(image)
            img_info = re.compile("<img src=\"(/upload/contest.*)\"\s*alt=\"공", re.MULTILINE)
            img_tag = img_info.findall(html)
            print("img:")

            img='\n'.join(img_tag)
            img=img.replace("/upload","https://www.wevity.com/upload")
            print(img)


            #(homepage)
            re_page = re.compile("홈페이지</span>\s*<a href=\"(.*?)\"", re.MULTILINE)
            page_tag = re_page.findall(html)
            print("page:")
            print('\n'.join(page_tag))

            cnt2 = cnt1+1
            infonum2=infonum2+1

            driver.back()
            
        except NoSuchElementException:# if pagenum == None 
            endcheck = False
            break
    pagenum2=pagenum2+1        
    infonum2=2  #to reset num because we go next page
    
    
    if endcheck == False:
        print("to be receipt crawling is finish ")
        print("wevity server crawling num : "+str(cnt1))
        break


        
#-------------------------------------------------------------------------------------
#------------------thinkgood server receipt crawling ----------------------------------------------------
        
        
        
        
        
endcheck = True

pagenum3=1
infonum3=1
while(endcheck):

    driver.get('https://www.thinkcontest.com/Contest/CateField.html?page='+str(pagenum3)+'&s=ing')
    time.sleep(2)

    while(infonum3 <=10):
        try:
        
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/table/tbody/tr['+str(infonum3)+']/td[1]/div[1]/a').click()
            URL=(driver.current_url)
            res=requests.get(URL)
            html=res.text
            
            time.sleep(1)
                    
            print("-----to be receipt "+str(pagenum3)+" page, "+str(infonum3)+" information -----")
            # (공모전이름)
            

            #(organization)
            

            #(term)
            

            #(information)
            

            #(image)
            

            


            #(homepage)
            

            cnt2 = cnt2+1
            infonum3=infonum3+1

            driver.back()
            
        except NoSuchElementException:# if pagenum == None 
            endcheck = False
            break
    pagenum3=pagenum3+1        
    infonum3=1  #to reset num because we go next page
    
    
    if endcheck == False:
        print("to be receipt crawling is finish ")
        print("thinkgood server crawling num : "+str(cnt2))
        break
        
        
#-------------------------------------------------------------------------------------
#------------------thinkgood server to be receipt crawling ----------------------------------------------------
        
        
        
        
        
endcheck = True

pagenum4=1
infonum4=1
while(endcheck):

    driver.get('https://www.thinkcontest.com/Contest/CateField.html?page='+str(pagenum4)+'&s=ing')
    time.sleep(2)

    while(infonum4 <=10):
        try:
        
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/table/tbody/tr['+str(infonum4)+']/td[1]/div[1]/a').click()
            URL=(driver.current_url)
            res=requests.get(URL)
            html=res.text
            
            time.sleep(1)
                    
            print("-----to be receipt "+str(pagenum4)+" page, "+str(infonum4)+" information -----")
            # (공모전이름)
            

            #(organization)
            

            #(term)
            

            #(information)
            

            #(image)
            

            


            #(homepage)
            

            cnt2 = cnt2+1
            infonum4=infonum4+1

            driver.back()
            
        except NoSuchElementException:# if pagenum == None 
            endcheck = False
            break
    pagenum4=pagenum4+1        
    infonum4=2  #to reset num because we go next page
    
    
    if endcheck == False:
        print("to be receipt crawling is finish ")
        print("thinkgood server crawling num : "+str(cnt2))
        break        
        
        
print("total crawling num : "+str(cnt1)+str(cnt2))
driver.close()
