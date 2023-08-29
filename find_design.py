from bs4 import BeautifulSoup
import os
directory = "./"
for filename in os.listdir(directory):
	f = os.path.join(directory, filename)
	if os.path.isfile(f):
		with open(f, 'r') as file:
			html_doc = file.read()
			soup = BeautifulSoup(html_doc, 'html.parser')
			for des_row in soup.find_all('tr', valign="top"): 
				if  des_row.find('td', string="Overall design"):
					des = des_row.find('td',  style="text-align: justify")
					print(des.text)					
