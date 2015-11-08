from httplib2 import *
from HTMLParser import HTMLParser

import re

class MyParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		if tag == 'img':
			print tag, attrs

class UNIV20Parser:

	def __init__(self):
		url = "https://univ20.com/covermodel"
		self.source = self.getSource(url)

	def getSource(self, url):
		h = Http()
		header, body = h.request(url, headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9"})
		return body

	def getImage(self):
		codeList = re.findall(r'<a href=\"https://univ20.com/([0-9]+).tomorrow\"', self.source)
		for code in codeList:
			url = "https://univ20.com/%s.tomorrow" %code
			print url
			source = self.getSource(url)
			imagelist = re.findall(r'//univ20.com/wp-content/uploads/(.*?.jpg)', source)
			for img_url in imagelist:
				if "-" not in img_url:
					print "http://univ20.com/wp-content/uploads/" + img_url

u = UNIV20Parser()
u.getImage()
del u
