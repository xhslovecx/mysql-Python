# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 17:35:01 2017

@author: xhs
"""

import urllib.request
from bs4 import BeautifulSoup as bs

url = "http://love.163.com/home"

headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')

opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read()
soup=bs(data,'html.parser')
print(soup)
