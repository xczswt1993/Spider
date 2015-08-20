# -*- coding:utf-8 -*-
__author__ = 'stone'

# douban movie chart spider
# how it do ?
# 1.we just find the movie title
# we analysis the webpage
# we just find the below
#
# <div class="hd">
# <a class="" href="http://movie.douban.com/subject/3442220/">
# <span class="title">海豚湾</span>
# <span class="title"> / The Cove</span>
# <span class="other"> / 血色海湾(台) / 海湾</span>
# </a>
# now we just use BeautifulSoup find <div class="hd">
# and then we can find the children easily
# what to find the next page?
# the url of every page is  http:// movie.douban.com/top250?start={page}&filter=&type='
# so we just change page's  value
# the below is  whole source code

import urllib
import urllib2
from bs4 import  BeautifulSoup

class DBS(object):
	"""docstring for DBS"""
	def __init__(self):
		self.page = 1		#movie chart first page
		self.cur_url = 'http://movie.douban.com/top250?start={page}&filter=&type='	#the url of every page

	def get_page(self,cur_page): 		#function of get page source 
		url = self.cur_url
		try:
			request = urllib2.Request(url.format(page=(cur_page -1)*25))
			response = urllib2.urlopen(request)
			result = response.read()
			unicodeResult = result.decode('utf-8')		#this step is no essential  .BeautifulSoup can aotu do it 
		except urllib2.URLError,e:
			if hasattr(e,'reason'):
				print e.reason
		return BeautifulSoup(unicodeResult)		#return a item of BeautifulSoup class

	def get_title(self,html):
		soup = html.select('[class~="hd"]')		# find  the parents
		for tag in soup:
			print  tag.a.contents[1].get_text()	#find the children

	def start_Spider(self):		
		while  self.page <=10:
			html = self.get_page(self.page)
			self.get_title(html)
			self.page += 1

sipder = DBS()
sipder.start_Spider()

