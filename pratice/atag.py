import requests
import re

URL='https://www.wevity.com/?c=find&s=1&mode=ing&gbn=viewok&gp=1&ix=27922'
res=requests.get(URL)
html=res.text

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

#(내용)
img_info = re.compile("<img src=\"(/upload/contest.*)\s*alt=\"공", re.MULTILINE)
img_tag = img_info.findall(html)
print("img:")

img='\n'.join(img_tag)
img=img.replace("/upload","https://www.wevity.com/upload")
print(img)


