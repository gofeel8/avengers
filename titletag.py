 # -*- coding: utf-8 -*- 

import urllib.request, re, requests


#web=urllib.request.urlopen('http://www.python.org')
#web=urllib.request.urlopen('https://www.wevity.com/?c=find&s=1&mode=ing')

#URL='http://www.python.org'
URL='https://www.wevity.com/?c=find&s=1&mode=ing'
res=requests.get(URL)
html=res.text
#html=web.read() #html 코드내용 저장

#web.close()

#print(html)

#code=str(html)
#print(html)
#.encode('utf-8').decode('cp949') #윈도우 형식의 문자열로 변경

#c=re.compile(r'.*?<title.*?>(.*)</title>') #두개의 플래그 설정
c=re.compile("<title>(.*)</title>",re.MULTILINE)
#c=re.compile("<div>(.*)</div>",re.MULTILINE)
#re.I\reS
print(c.findall(html))

