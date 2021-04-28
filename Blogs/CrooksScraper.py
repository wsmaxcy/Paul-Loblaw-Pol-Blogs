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
	
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

	webpage = urlopen(req).read()

	soup = s(webpage, "lxml")	

	title = soup.find('title')
	date = soup.find('time')
	author = soup.find(class_='nh-footer')
	body = soup.find_all('p')
	
	# clean text for csv
	textTitle = title.get_text()[:-19].replace(',','')
	textDate = (date.get_text().split()[0]).replace('/','-')
	if(textDate[1]=='-'):
		textDate = '0'+textDate
	textAuthor = author.find('a').get_text()
	textBody = textTitle + ', '+ textAuthor + ", " + textDate + ", "

	for text in body:
		textBody = textBody + text.get_text().replace(',','')+' '
		textBody = textBody.replace('\n', '')
		

	textBody = 'L, ' + textBody + '\n'

	# blog title name
	blogTitle = 'L CrooksAndLiars '+textAuthor+' '+textTitle+'.csv'
	invalid = '<>:\"\\|?*\'/\n'
	for char in invalid:
		blogTitle = blogTitle.replace(char,'')
	
	print("CrooksAndLiars: "+textTitle)

	# write file
	file = open(sys.path[0]+"/SavedBlogs/"+blogTitle , "w+", encoding = 'utf-8')
	file.write(textBody)
	file.close()
	

	return()

def main():

	# range deals with how many blogs are scraped. change 
	for x in range(0,80):
		url = 'https://crooksandliars.com/politics?page=' + str(x)
		req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
		webpage = urlopen(req).read()
		soup = s(webpage, "html.parser")
		links = soup.find_all('h2')
		links = links[1:]
		linkList = []
		
		for link in links:
			linkList.append(link.find('a').get('href'))

		for link in linkList:
			scrape('https://crooksandliars.com/'+link)

	return()
main()