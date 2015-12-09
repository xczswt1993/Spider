#/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'stone'
import urllib
import requests
from bs4 import BeautifulSoup
import threading
import  json
# url = 'http://movie.douban.com/chart'
#
# req = requests.get(url)
# html = req.text.encode('utf-8')
# # with open('movie.html','w') as f:
# #     f.write(html)
#
# # soup = BeautifulSoup(open('movie.html'),'lxml')
# soup = BeautifulSoup(html,'lxml')
# for link in soup.find_all('a'):
#     if link.get('class') is not None:
#          class_str = link.get('class')
#          if class_str[0] == 'nbg':
#              s = BeautifulSoup(str(link),'lxml')
#              print s.a.get('title'),'  ',s.img.get('src')

#
#下载线程
#
class Download(threading.Thread):
    def __init__(self,name,imgUrl):
        threading.Thread.__init__(self)
        self.name = name
        self.imgUrl = imgUrl

    def downloadImg(self):
        print threading.current_thread().name
        path = r'/home/stone/图片/%s.jpg'% self.name
        data = urllib.urlopen(self.imgUrl).read()
        f = file(path,'wb')
        f.write(data)
        f.close()

    def run(self):
        self.downloadImg()

#url = 'http://movie.douban.com/top250?start=0&filter='

# req = requests.get(url)
# html = req.text.encode('utf-8')
# # with open('top.html','w') as f :
# #     f.write(html)
#
# soup = BeautifulSoup(html,'lxml')
# ol = soup.find('ol')
info = []
getThreads = []
downThreads = []


#
#解析网页
#提取name和imgUrl
#
class GetInfo(threading.Thread):
    def __init__(self,url):
        threading.Thread.__init__(self)
        self.url = url

    def getInfo(self):
        req = requests.get(self.url)
        html = req.text.encode('utf-8')
        soup = BeautifulSoup(html,'lxml')
        ol = soup.find('ol')
        for li in ol.find_all('li'):
            name = li.img.get('alt')
            name = name.encode('utf-8')
            imgUrl = li.img.get('src')
            info.append({name:imgUrl})

    def run(self):
        self.getInfo()

targets = []

for i in range(10):
    target = 'http://movie.douban.com/top250?start=%d&filter=' % (i*25)
    targets.append(target)

for i in range(len(targets)):
    t = GetInfo(targets[i])
    getThreads.append(t)

for i in range(len(getThreads)):
    getThreads[i].start()

for i in range(len(getThreads)):
    getThreads[i].join()

# for item in info:
#     for name,img in item.iteritems():
#         print name,img
# with open('movie.json','w') as f:
#     f.write(json.dumps(info))
#
# jsonDict = {}
#
# with open('movie.json','r') as f:
#     jsonDict = json.load(f)

for i,item in enumerate(info):
    for name,imgUrl in item.iteritems():
        t = Download(str(i+1)+'_'+name,imgUrl)
        downThreads.append(t)

for i in range(len(downThreads)):
    downThreads[i].start()

for i in range(len(downThreads)):
    downThreads[i].join()


