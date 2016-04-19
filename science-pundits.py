# this file does nothing at the moment


import urllib2
from bs4 import BeautifulSoup

import readability

# resp = urllib2.urlopen("http://www.vox.com/2016/4/6/11376948/babymetal-us-debut-colbert")
# soup = BeautifulSoup(resp, "lxml", from_encoding=resp.info().getparam('charset'))
#
#
#
# # print soup.body
# for tag in soup.findAll('p'):
#     print tag
#
#
#
# resp = urllib2.urlopen("http://www.politico.com/story/2016/03/rubio-wins-dc-caucuses-220681")
# soup = BeautifulSoup(resp, "lxml", from_encoding=resp.info().getparam('charset'))
#
#
# for tag in soup.findAll('p'):
#     print tag

import os
from readability import ParserClient


os.environ['READABILITY_PARSER_TOKEN'] = 'c4e591e3f00ed1512c8194ab6616cf826d155294'


# READABILITY_PARSER_TOKEN='c4e591e3f00ed1512c8194ab6616cf826d155294'
token = "c4e591e3f00ed1512c8194ab6616cf826d155294"

from readability import ParserClient
client = ParserClient(token=token)

parser_client = ParserClient(token)
parser_response = client.get_article('http://paulgraham.com/altair.html')
article = parser_response.json()

print(article['title'])
print(article['content'])


parser_response = client.get_article("http://www.politico.com/story/2016/03/rubio-wins-dc-caucuses-220681")
article = parser_response.json()
print(article['title'])
print(article['content'])



parser_response = client.get_article("http://www.vox.com/2016/4/6/11376948/babymetal-us-debut-colbert")
article = parser_response.json()
print(article['title'])
print(article['content'])
