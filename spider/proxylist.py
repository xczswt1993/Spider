#!/usr/bin/env python
#-*-coding:utf-8-*-
__author__= 'stone'
import urllib2
import re
import requests
import socket
import socks
import execjs
url = 'http://pachong.org/high.html'
#
#使用socks5代理
socks.set_default_proxy(socks.SOCKS5,'127.0.0.1',1080)
socket.socket = socks.socksocket
#先设置代理,再请求
#urllib2的使用方式
#request = urllib2.Request('http://www.whatismyip.com.tw/')
#request = urllib2.Request(url)
#response = urllib2.urlopen(request)
#html=response.read()
#requests库的使用方式
#r = requests.get('http://www.whatismyip.com.tw/')
###print r.text.encode('utf-8')
r = requests.get('http://pachong.org/high.html')
html = r.text.encode('utf-8')
#pattern = '<script type.*?>var(.*?)</script>'
#result = re.search(pattern,html)
#script=result.group()
#pattern = '<script type.*?>(.*?)</script>'
#result = re.search(pattern,script)
#print result.group(1)
pattern = re.compile('<td><script>(.*?)</script>',re.S)
items = re.findall(pattern,html)
for item in items:
    print item
