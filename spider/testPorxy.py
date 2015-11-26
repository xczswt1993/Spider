#!/usr/bin/env python
#-*- coding:utf-8 -*-
import requests
import urllib2
import socket
import socks
import requesocks
url = 'http://www.whatismyip.com.tw'
#
#使用sock代理时
#
socks.set_default_proxy(socks.SOCKS5,ip,port)
socket.socket = socks.socksocket
response = urllib2.urlopen(url)
print response.read()

#
#使用http代理时
#方法(1):
proxy_support = urllib2.ProxyHandler({'http','http://ip:port'})
opener = urllib2.build_opener(ProxyHandler)
urllib2.install_opener(opener)
html = urllib2.urlopen(url).read()

#方法(2):
proxy = 'ip:port'
proxis = {'http':'http://%s'% proxy}
headers = {'User-agent':'Mozilla/5.0'}
proxy_support = urllib2.ProxyHandler(proxis)
opener = urllib2.build_opener(proxy_support,urllib2.HTTPHandler(debuglevel=1))
urllib2.install_opener(opener)

req = urllib2.Request(url,None,headers)
html = urllib2.urlopen(req).read()

#
#使用requesocks库
#可以实现http,https,sock4,socks5代理


# SOCKS5 proxy for HTTP/HTTPS
proxiesDict = {
        'http' : "socks5://1.2.3.4:1080",
        'https' : "socks5://1.2.3.4:1080"
}

# SOCKS4 proxy for HTTP/HTTPS
proxiesDict = {
        'http' : "socks4://1.2.3.4:1080",
        'https' : "socks4://1.2.3.4:1080"
}

# HTTP proxy for HTTP/HTTPS
proxiesDict = {
        'http' : "1.2.3.4:1080",
        'https' : "1.2.3.4:1080"
}
#if need basic auth
#use proxies = {'http':'http://user:pass@ip:port',}
session = requesocks.session()
session.proxies(proxiesDict)
req = session.get(url)
print req.text
