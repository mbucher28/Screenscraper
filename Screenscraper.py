# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 11:47:02 2019

@author: mbucher
"""



import urllib
import urllib.request
from bs4 import BeautifulSoup
import os



# setup data source connection and processor
source = urllib.request.urlopen("https://www.baseball-reference.com/leagues/MLB/bat.shtml")
soup = (BeautifulSoup(source, "html.parser"))

filename = "SportsDataFinal1.csv"
f = open(os.path.expanduser(filename), "wb")
header = "Teams~#Bat~BatAge~R/G~G~PA~AB~R~H~2B~3B~HR~RBI~SB~CS~BB~SO~BA~OBP~SLG~OPS~TB~GDP~HBP~SH~SF~IBB"
f.write(bytes(header, encoding="ascii", errors='ignore'))
# process data
dataoutput=""
for td in soup.findAll('tr'):
    standdata=""
    for data in td.findAll('td'):
        standdata = standdata + "~" + data.text
    dataoutput = dataoutput + "\n" + standdata

f.write(bytes(dataoutput, encoding="ascii", errors='ignore'))


    

