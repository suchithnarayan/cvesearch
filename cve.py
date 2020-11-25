#!/usr/bin/ python3
#https://github.com/suchithnarayan

import requests
import sys
from bs4 import BeautifulSoup

vuln = sys.argv[1]

url = "https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword="+vuln
res = requests.get(url)
soup = BeautifulSoup(res.content,'html.parser')
td = soup.find_all('td', valign="top", nowrap="nowrap")

for i in td:
	soup1 = BeautifulSoup(str(i),'html.parser')
	try:
		cves= soup1.find('a').get_text()
	except:
		pass
	print(cves)
