################################################################################
# Will Macxy
# Hot Air Blog Scraper
# Last Updated : 4/27/2021
################################################################################

from bs4 import BeautifulSoup as s
from urllib.request import Request, urlopen
import sys
import re
import time

def scrape(url):

    
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

	webpage = urlopen(req).read()

	soup = s(webpage, "lxml")

	title = soup.find('title')
	body = soup.find_all('p')
	
	textTitle = title.get_text().replace(',','')
	textBody = '' 
    
	for text in body:
		textBody = textBody + text.get_text().replace(',','')
		textBody = textBody.replace('\n', '')

	blog = [textTitle,textBody]
	
	
	return(blog)

def main(url):

	# range deals with how many pages get scraped. this would be 10 pages of 50
	
	#url = 'https://www.thepennyhoarder.com/retirement/do-you-get-more-social-security-married/?aff_sub2=homepage'
	
	blog = scrape(url)
	

	return(blog)
#main()