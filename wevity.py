import requests
import re
import pymysql

conn=pymysql.connect(host="localhost",user='root',password='ffdsffds',db='test',charset='utf8')
curs=conn.cursor()


URL='https://www.wevity.com/?c=find&s=1&mode=ing&gbn=viewok&gp=1&ix=27700'
res=requests.get(URL)
html=res.text

# (공모전이름)
re_title = re.compile(">(.*)</h6>", re.MULTILINE)
title_tag = re_title.findall(html)
print("title:")
title='\n'.join(title_tag)
print(title)

#(주관)
re_com = re.compile("주관</span>\s*(.*)\s*</li>", re.MULTILINE)
com_tag = re_com.findall(html)
print("com:")
com='\n'.join(com_tag)
print(com)

#(기간)
re_day = re.compile("기간</span>\s*(.*)\s*<span", re.MULTILINE)
day_tag = re_day.findall(html)
print("when:")
when='\n'.join(day_tag)
print(when)

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
page='\n'.join(page_tag)
print(page)

#sql="INSERT INTO avengers_crawling VALUES(%s,%s,%S)"
try:
	curs.execute("INSERT INTO avengers_crawling VALUES(%s,%s,%s,%s,%s,%s)",(title,com,when,info,img,page))
	conn.commit()
except:
        conn.rollback()
        print("error")
conn.close()
