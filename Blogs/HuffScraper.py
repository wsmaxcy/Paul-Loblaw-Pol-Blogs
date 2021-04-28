################################################################################
# Will Macxy
# Hot Air Blog Scraper
# Last Updated : 4/28/2021
################################################################################

from bs4 import BeautifulSoup as s
from urllib.request import Request, urlopen
import time
import re
import sys


def scrape(url):

	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

	webpage = urlopen(req).read()

	soup = s(webpage, "lxml")

	title = soup.find_all('title')
	date = soup.find_all(class_="timestamp__date--published")
	author = soup.find_all(class_="author-card__link yr-author-name")
	body = soup.find_all('p')
	body = body[:-1]
	
	
	textAuthor = ''
	# saves title, date, author to text
	textTitle = title[0].get_text()[:-11].replace(',','')
	
	
	textDate = date[0].get_text()[:-12]
		
	if len(author) ==0:
		textAuthor = 'Associated Press'			
	else:	
		textAuthor = author[0].get_text()

	# formats date with YYYY-MM-DD
	textDate = textDate[7:11]+"-"+textDate[1:3]+"-"+textDate[4:6]

	textBody = textTitle + ', '+ textAuthor + ", " + textDate + ", "

	# cleans text body
	for i in body:
		textBody = textBody + i.get_text().replace(',','') + " "

	textBody = 'L, ' +  textBody + '\n'
	
	blogTitle = 'L HuffPost '+str(textAuthor)+ " " + str(textTitle) + ".csv"
	invalid = '<>:\"\\|?*\'/'
	for char in invalid:
		blogTitle = blogTitle.replace(char,'')

	print('HuffPost: '+textTitle)

	# writes file
	file = open(sys.path[0]+"/SavedBlogs/"+blogTitle , "w+", encoding = 'utf-8')
	file.write(textBody)
	file.close()

	return()

def main():

	# range of how many blogs get scraped. This numbe can change depending on 503 errors if a lot of activity
	# happens over the network
	for i in range(1,2):
		page = i

		numEntries = 500

		url = 'https://www.huffpost.com/api/section/politics/cards?page='+str(page)+'&limit='+str(numEntries)

		req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

		webpage = urlopen(req).read()

		links = re.findall(r'https:\/\/www.huffpost.com\/entry\/[a-zA-Z-_\d]*',str(webpage))

		

		for link in links:
			scrape(link)
		return()

main()