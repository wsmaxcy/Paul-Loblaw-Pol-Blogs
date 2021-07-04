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


def scrape(url,status,root):

	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

	webpage = urlopen(req).read()

	soup = s(webpage, "lxml")

	title = soup.find('title')
	date = re.findall(r'story\/[0-9][0-9][0-9][0-9]\/*[0-9]*[0-9]\/*[0-9]*[0-9]',url)
	author = soup.find(class_='author-name')
	body = soup.find_all('p')
	
	textTitle = title.get_text().replace(',','')
	textDate = date[0][6:].replace('/','-')
	
	if(textDate[6]=='-'):
		textDate = textDate[:5]+'0'+textDate[5:]

	if(len(textDate)==9):
		textDate = textDate[:8]+'0'+textDate[8:]

	textAuthor = author.get_text().replace('\n','')

	textBody = textTitle + ', '+ textAuthor + ", " + textDate + ", "

	for text in body:
		textBody = textBody + text.get_text().replace(',','')+' '
		textBody = textBody.replace('\n', '')

	textBody = 'L, ' +  textBody + '\n'
	
	blogTitle = 'L DailyKos '+textAuthor+' '+textTitle+'.csv'
	invalid = '<>:\"\\|?*\'/\n'
	for char in invalid:
		blogTitle = blogTitle.replace(char,'')
	
	step = "[+] DK: "+textTitle
	status['text'] = "{}".format(step)
	root.update()

	file = open(sys.path[0]+"/Blogs/SavedBlogs/"+blogTitle , "w+", encoding = 'utf-8')
	file.write(textBody)
	file.close()

	return("DailyKos: "+textTitle)

def main(status, root):

	# range deals with how many pages get scraped. this would be 10 pages of 50
	for x in range(1,2):	
		url = 'https://www.dailykos.com/part/story/table/by_current?page='+str(x)
		req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
		webpage = urlopen(req).read()
		soup = s(webpage, "html.parser")
		links = soup.find(class_='styled storiesAsGrid').find_all(class_='title')
		linkList = []
		#print(links)


		for link in links:
			linkList.append(link.get('href'))

		for link in linkList:
			scrape('https://www.dailykos.com'+link,status,root)
			time.sleep(.5)

	
			

	return()
