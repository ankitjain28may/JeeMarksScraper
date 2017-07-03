import requests
import csv
import sys
from bs4 import BeautifulSoup 



def get_string(item):
	item = item.get_text().replace("\n", '').replace('\t', '').replace(" ", '')
	item = item.encode('utf-8')
	return item

def main(data):
	url = 'http://cbseresults.nic.in/jee_main_zxc/jee_cbse_2017.asp'

	headers = {
		'user-agent': 'my-app/0.0.1',
		'Accept-Language': 'en-US,en;q=0.8,hi;q=0.6',
		'Cache-Control': 'no-cache',
		'Connection': 'keep-alive',
		'Content-Type' :'application/x-www-form-urlencoded',
		'Origin': 'http://cbseresults.nic.in',
		'Pragma': 'no-cache',
		'Referer' :'http://cbseresults.nic.in/jee_main_zxc/jee_cbse_2017.htm',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent' :'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
	}

	r = requests.post(url, data, headers=headers)
	soup = BeautifulSoup(r.content,'html5lib')

	table = soup.find_all("table")

	result = [
		get_string(table[4].find_all('td')[9]),
		get_string(table[4].find_all('td')[13]),
		get_string(table[6].find_all('td')[13]),
		get_string(table[6].find_all('td')[17])
	]
	return result

i = 0
ex = [];
file_name = raw_input("Enter the filename\n")
output_file_name = raw_input("Enter the output filename\n")
with open(output_file_name, 'a+') as csvwrite:
	spamwriter = csv.writer(csvwrite, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
	readerdata =  csv.reader(csvwrite, delimiter=',', quotechar='|')
	index = ['cname', 'mname', 'fname', 'dob', 'roll', 'mob', 'state', 'category', 'state', 'paper-I', 'paper-II']
	if index not in readerdata:
		spamwriter.writerow(index)
	l = len(list(readerdata))
	with open(file_name) as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in spamreader:
			try:
				sys.stderr.write( "\r Reading " + str(i) + " Records" )
				i+=1
				if i < l-5:
					continue
				# dob = row[3]
				# dob = dob.split("/")
				# if int(dob[2]) <= 99 and int(dob[2]) >= 90:
				# 	dob[2] = "19"+dob[2]
				# else:
				# 	dob[2] = "20"+dob[2]
				# dob = "/".join(dob)
				data = {
					'regno': row[2],
					'dob': row[1],
					'B2': 'Submit'
				}
				result = main(data)
				row.extend(result)
				if row not in readerdata:
					spamwriter.writerow(row)
			except Exception as e:
				ex.append(row[4])
				print e
				pass
print ex


