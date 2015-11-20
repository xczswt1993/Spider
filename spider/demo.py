#-*- coding:utf-8 -*-
import urllib2
import re
enable_proxy = True
ip = '218.200.66.200'
port = '80'
http_proxy = ip + ':'+ port
proxy_handler= urllib2.ProxyHandler({'http':http_proxy})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)
request = urllib2.Request('http://pachong.org/high.html')
try: 
    response = urllib2.urlopen(request)
    html = response.read().decode('utf-8')
    pattern  = '<h2>(.*?)</h2>'
except urllib2.URLError, e:
    print e.reason
result = re.search(pattern,html)
result_ip = result.group(1)
if ip == result_ip:
    print True
