import requests
import csv
from bs4 import BeautifulSoup 


def get_string(item):
	item = item.string.replace("\n", '').replace('\t', '').replace(" ", '')
	item = item.encode('utf-8')
	return item


url = 'http://cbseresults.nic.in/jee_main_zxc/jee_cbse_2017.asp';

data = {
	'regno': '51603866',
	'dob': '26/12/1998',
	'B2': 'Submit'
}

headers = {
	'user-agent': 'my-app/0.0.1',
	#'Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	#'Accept-Encoding:gzip, deflate',
	'Accept-Language': 'en-US,en;q=0.8,hi;q=0.6',
	'Cache-Control': 'no-cache',
	'Connection': 'keep-alive',
	#'Content-Length': '43',
	'Content-Type' :'application/x-www-form-urlencoded',
	#'Host': 'cbseresults.nic.in',
	'Origin': 'http://cbseresults.nic.in',
	'Pragma': 'no-cache',
	'Referer' :'http://cbseresults.nic.in/jee_main_zxc/jee_cbse_2017.htm',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent' :'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
}

r = requests.post(url, data, headers=headers)
soup = BeautifulSoup(r.content,'html5lib')

table3 = soup.find_all("table")
result = {
	'Category': get_string(table3[4].find_all('td')[9]),
	'State': get_string(table3[4].find_all('td')[13]),
	'Paper-I': get_string(table3[6].find_all('td')[13]),
	'Paper-II': get_string(table3[6].find_all('td')[17]),
}
print result

