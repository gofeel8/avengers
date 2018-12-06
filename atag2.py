import requests
import re

# [a 태그]
URL='https://www.wevity.com/?c=find&s=1&mode=ing&gp=1'
#headers = {'Content-Type': 'application/json; charset=utf-8'}
res=requests.get(URL)
html=res.text

#re_a = re.compile("<[Aa]\s+[^>]+>", re.MULTILINE)
re_a = re.compile("<a href=\"\?c=find&s=1&mode=ing&gbn=view&gp[^<]+<", re.MULTILINE)
#re_a = re.compile("<ul class=\"list\">[^(ul)]", re.MULTILINE)
#re_a = re.compile("<ul class=\"list\">"[], re.MULTILINE)



a_tag = re_a.findall(html)

print('\n'.join(a_tag))

#for name in a_tag:
#	re_b=re.compile("<[Ss]pan\s+[^>]+</span>",re.MULTILINE)
#	b_tag=re_b.findall(name)
#	print('\n'.join(b_tag))

