#aa
#!/usr/bin/python3
import re
import urllib2
html = urllib2.urlopen("http://craftstud.io/builds").read()
re.search(r"Server \d+\.\d+\.\d+\.\d+", html).group()

