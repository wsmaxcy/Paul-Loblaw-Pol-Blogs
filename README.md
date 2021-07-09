
╭━━━━┳╮╱╱╱╱╱╭━━━╮╱╱╱╱╱╭╮╱╭╮╱╱╱╱╱╭╮╱╭╮
┃╭╮╭╮┃┃╱╱╱╱╱┃╭━╮┃╱╱╱╱╱┃┃╱┃┃╱╱╱╱╱┃┃╱┃┃
╰╯┃┃╰┫╰━┳━━╮┃╰━╯┣━━┳╮╭┫┃╱┃┃╱╱╭━━┫╰━┫┃╭━━┳╮╭╮╭╮
╱╱┃┃╱┃╭╮┃┃━┫┃╭━━┫╭╮┃┃┃┃┃╱┃┃╱╭┫╭╮┃╭╮┃┃┃╭╮┃╰╯╰╯┃
╱╱┃┃╱┃┃┃┃┃━┫┃┃╱╱┃╭╮┃╰╯┃╰╮┃╰━╯┃╰╯┃╰╯┃╰┫╭╮┣╮╭╮╭╯
╱╱╰╯╱╰╯╰┻━━╯╰╯╱╱╰╯╰┻━━┻━╯╰━━━┻━━┻━━┻━┻╯╰╯╰╯╰╯
╭━━━╮╱╱╭╮╱╭━━╮╭╮╱╱╱╱╱╱╱╭╮
┃╭━╮┃╱╱┃┃╱┃╭╮┃┃┃╱╱╱╱╱╱╱┃┃
┃╰━╯┣━━┫┃╱┃╰╯╰┫┃╭━━┳━━╮┃┃╱╱╭━━┳━━┳━━┳━━┳━╮
┃╭━━┫╭╮┃┃╱┃╭━╮┃┃┃╭╮┃╭╮┃┃┃╱╭┫╭╮┃╭╮┃╭╮┃┃━┫╭╯
┃┃╱╱┃╰╯┃╰╮┃╰━╯┃╰┫╰╯┃╰╯┃┃╰━╯┃╰╯┃╰╯┃╰╯┃┃━┫┃
╰╯╱╱╰━━┻━╯╰━━━┻━┻━━┻━╮┃╰━━━┻━━┻━╮┣━╮┣━━┻╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃╱╱╱╱╱╱╱╭━╯┣━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯╱╱╱╱╱╱╱╰━━┻━━╯

By: Will Maxcy

What is it?
--------------------------------------------------------------------------------
Ever wonder if an opinion piece has langauge that suggests political bias?

Ever read a blog so blatently one sided that it is almost funny?

Ever want to know if a robot could read a work of literature and be able to 
spot political bias?

THE PAUL LOBLAW POL BLOG LOGGER IS HERE for YOU!

The Paul Loblaw Pol Blog Logger scrapes blog posts from 6 different political
blog websites, saves them, compares them to a specific blog post entered in
by the user, then can predict if the user entered blog is 'conservative'
leaning or 'liberal' leaning.

This is done by comparing the sentiment in specific sentences from conservative
blogs against liberal blogs and finding

How do I install it?
--------------------------------------------------------------------------------
MUST have python installed to run

Install latest version of Python

Clone repository from github.com/wsmaxcy/paul-loblaw-pol-blog

---- Command: "git clone github.com/wsmaxcy/paul-loblaw-pol-blog.git"

From directory, use command "pip3 install -r requirements.txt"

Open python interpreter  and type command "import nltk"

Type command "nltk.download()"

Download all collections

It should be ready to run now

How do I use it?
--------------------------------------------------------------------------------
Open the "PLLPBL.pyw" file in the main directory

First, scrape blogs from the interent. The more blogs the better the
program can determine political bias. This can be done by pressing the 
"Scrape Blogs" button.

Once blogs are scraped, scan a URL that is intended to be predicted. Enter in 
the URL in the text box that says "Enter URL Here" then press the "Scrape URL"
button. 

Once the ticker at the bottom says the URL was successfully scraped, press the
"Find Affiliation" button. This process will take anywhere between 10-20 
minutes (Yes, this is a long time. I'm working on it [haha]). Once the blog
political affiliation can be predicted, the ticker will print out the 
prediction and the "LED" will light up blue or red based on political 
affiliation.
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------

Thank you for reading! Any questions or comments feel free to e-mail me at 
wsmaxcy@gmail.com