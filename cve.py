#!/usr/bin/ python3
#https://github.com/suchithnarayan

import requests
import sys
from bs4 import BeautifulSoup
import re

vuln = sys.argv[1]
url = "https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword="+vuln
res = requests.get(url)
soup = BeautifulSoup(res.content,'html.parser')
td = soup.find_all('td', valign="top")
#0,2,4 = cve | 1,3,5 = Description

for i in td:
	index = td.index(i)
	if index % 2 == 0:
		pass
	else:
		soup1 = BeautifulSoup(str(i),'html.parser')
		try:
			desc = soup1.find('td').get_text()
			reg = re.search(vuln.split()[0],desc,re.IGNORECASE)
			if reg:
				soup2 = BeautifulSoup(str(td[index-1]),'html.parser')
				cves= soup2.find('a').get_text()
				print(cves)
		except:
			pass
