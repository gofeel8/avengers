#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
response = requests.get('http://www.thinkcontest.com')

html = response.text

soup = BeautifulSoup(html, 'html.parser')
for tag in soup.select('div[class=title]'):
	print(tag.text.strip())
#for tag in soup.select('div[class=tit3]'):
#	print(tag.text.strip())

