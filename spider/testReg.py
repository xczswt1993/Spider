#!/usr/bin/env python
#-*-coding:utf-8-*-
import re
import requests
import socket
import socks

url = 'http://pachong.org/high.html'
socks.set_default_proxy(socks.SOCKS5,'127.0.0.1',1080)
socket.socket = socks.socksocket
r = requests.get(url)
html = r.text.encode('utf-8')

#匹配开头script
#reg_head = '<script tpye.*?>(.*?)</script>'

#匹配端口script
#reg_port = '<td><script>(.*?)</script>'
reg_all = '<td>.*?</td>'
test_script = '<td>([0-9]+(?:\.[0-9]+){0,3})</td>'
pattern = re.compile(reg_all,re.S)
result = re.findall(pattern,html)
print result
