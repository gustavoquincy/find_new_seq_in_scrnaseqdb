from bs4 import BeautifulSoup


html_doc = open("./scrnaseqdb_browse_page/page1.html", "r")
soup = BeautifulSoup(html_doc, "html.parser")
for link in soup.find_all('a'):
	if 'http' and 'acc' in link.get('href'):
		print(link.get('href'))
html_doc = open("./scrnaseqdb_browse_page/page2.html", "r")
soup = BeautifulSoup(html_doc, "html.parser")
for link in soup.find_all('a'):
	if 'http' and 'acc' in link.get('href'):
		print(link.get('href'))
html_doc = open("./scrnaseqdb_browse_page/page3.html", "r")
soup = BeautifulSoup(html_doc, "html.parser")
for link in soup.find_all('a'):
	if 'http' and 'acc' in link.get('href'):
		print(link.get('href'))
html_doc = open("./scrnaseqdb_browse_page/page4.html", "r")
soup = BeautifulSoup(html_doc, "html.parser")
for link in soup.find_all('a'):
	if 'http' and 'acc' in link.get('href'):
		print(link.get('href'))