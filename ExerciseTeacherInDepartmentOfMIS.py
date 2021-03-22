# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 16:54:31 2021

@author: user
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.mis.kuas.edu.tw/main.php?mod=teacher&site_id=0"
html = urlopen(url).read().decode('UTF-8')
bsObj3 = BeautifulSoup(html,"html.parser")

nameList = bsObj3.find_all("font",{"color":"blue"})
mailList = bsObj3.findAll("td",{"style":"text-align:center;width:"})
for i in range(len(nameList)):
    print(nameList[i].get_text(),end="")
    print(mailList[i].get_text())