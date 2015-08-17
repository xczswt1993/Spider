#-*- coding:utf-8 -*-

import base64
class   ProxyMiddleware(object):
	"""docstring for   ProxyMiddleware"""
	def process_reqeust(self,request,spider):
		request.meta['proxy'] = 'http://220.176.130.79 :9000'
		
		