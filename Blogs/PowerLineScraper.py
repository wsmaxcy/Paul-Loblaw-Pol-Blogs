################################################################################
# Will Macxy
# Hot Air Blog Scraper
# Last Updated : 4/28/2021
################################################################################

from bs4 import BeautifulSoup as s
from urllib.request import Request, urlopen
import sys
import re

def scrape(url):
	
	# scrap of individual pages
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

	webpage = urlopen(req).read()

	soup = s(webpage, "lxml")	

	title = soup.find('title')
	date = soup.find('meta',property='article:published_time')
	author = soup.find(class_='url fn n')
	body = soup.find_all('p')
	
	
	# variable cleaner
	textTitle = title.get_text()[:-13].replace(',','')
	textDate = re.findall(r'[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]',(str(date)))[0]
	textAuthor=author.get_text()
	
	textBody = textTitle + ', '+ textAuthor + ", " + textDate + ", "

	# text body cleaner
	for text in body:
		textBody = textBody + text.get_text().replace(',','')+' '

	textBody = 'C, ' +textBody + '\n'

	# file name
	blogTitle = 'C PowerLine '+textAuthor+' '+textTitle+'.csv'
	invalid = '<>:\"\\|?*\'/'
	for char in invalid:
		blogTitle = blogTitle.replace(char,'')
	
	print("PowerLine: "+textTitle)

	# write operation
	file = open(sys.path[0]+"/SavedBlogs/"+blogTitle , "w+", encoding = 'utf-8')
	file.write(textBody)
	file.close()
	

	return()

def main():

	# scraper for 50 pages
	for x in range(0,5):
		url = 'https://www.powerlineblog.com/page/' + str(x)
		req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
		webpage = urlopen(req).read()
		soup = s(webpage, "html.parser")
		links = soup.find_all(class_='entry-title')
		
		linkList = []
		
		for link in links:
			linkList.append(link.find('a').get('href'))

		for link in linkList:
			scrape(link)

	return()
main()