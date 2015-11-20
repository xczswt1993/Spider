#!/usr/bin/env python
#-*-coding:utf-8-*-
__author__ = 'stone'
import re 
import requests
import socket
import socks
import js2py
url = 'http://pachong.org/high.html'
socks.set_default_proxy(socks.SOCKS5,'127.0.0.1',1080)
socket.socket = socks.socksocket
r = requests.get(url)
html = r.text.encode('utf-8')
#匹配定义script脚本
reg_all = '<script type.*?>(.*?)</script>'
pattern_all = re.compile(reg_all,re.S)
result_all = re.findall(pattern_all,html)
print result_all[2]
#匹配端口
reg_sig = '<td><script>(.*?)</script>'
pattern_sig = re.compile(reg_sig,re.S)
result_sig = re.findall(pattern_sig,html)
#匹配ip地址
reg_ip = '<td>([0-9]+(?:\.[0-9]+){0,3})</td>'
pattern_ip = re.compile(reg_ip,re.S)
result_ip = re.findall(pattern_ip,html)
ip_port = {}
for i,item in enumerate(result_ip):
    find_result = result_all[2]+ result_sig[i]
    js = """ function add(){
    %s
    }
    add() """ % find_result.replace("document.write","return")
    result = js2py.eval_js(js)
    ip_port[item]= result

print ip_port



