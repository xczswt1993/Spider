#-*- coding:utf-8 -*-
__author__ = 'stone'

# this is the second douban sipder 
# and this program will use thread 

import urllib
import urllib2
from bs4 import BeautifulSoup
import threading,Queue,time

FILE_LOCK = threading.Lock()
SHARE_Q = Queue.Queue()
_WORKER_THREAD_NUM =3

class MyThread(threading.Thread):
	def __init__(self,func):
		super(MyThread,self).__init__()
		self.func = func

	def run(self):
		self.func()

def worker():
	global SHARE_Q
	while  not SHARE_Q.empty():
		url = SHARE_Q.get()
		html = get_page(url)
		get_title(html)
		time.sleep(1)
		SHARE_Q.task_done()

def get_page(cur_page):
	try:
		request = urllib2.Request(cur_page)
		response = urllib2.urlopen(request)
		result = response.read()
		unicodeResult = result.decode('utf-8')		
	except urllib2.URLError,e:
		if hasattr(e,'reason'):
			print e.reason
	return BeautifulSoup(unicodeResult)

def get_title(html):
	
	soup = html.select('[class~="hd"]')
	for tag in soup:
		print tag.a.contents[1].string
	

def main():
	global SHARE_Q
	threads = []
	cur_url = 'http://movie.douban.com/top250?start={page}&filter=&type='
	for index in xrange(10):
		SHARE_Q.put(cur_url.format(page=index * 25))
	for i in xrange(_WORKER_THREAD_NUM):
		thread = MyThread(worker)
		thread.start()
		threads.append(thread)
	for thread in threads:
		thread.join()
	SHARE_Q.join()


	print 'spider wirte successfully!'

if __name__ == '__main__':
	main()