import urllib
from bs4 import BeautifulSoup
import praw
import re

#Objective
#Get the ten newest articles from CNN
#For each article
#If the article has not already been replied to
#Post the link to the article on reddit with the same title

politics = 'http://www.cnn.com/'
page = urllib.request.urlopen(politics)
soup = BeautifulSoup(page, 'html.parser')
#The regex below definitely works for the links in mind
#TODO: Use bs to get the title of the article we are currently looking at
#TODO: Use praw to post the article to reddit with the link and title of the article we are currently looking at
raw = soup.prettify('utf-8')
p = re.compile('\/2017\/10\/31\/politics\/[A-Za-z0-9\-\_]+\/[A-Za-z0-9\-\_\.]+')
latestpolitics = p.findall(raw.decode('utf-8'))
p = re.compile('\/2017\/10\/31\/us\/[A-Za-z0-9\-\_]+\/[A-Za-z0-9\-\_\.]+')
latestusnews = p.findall(raw.decode('utf'))
