#/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'stone'

import requests
import urllib
import urllib2
import lxml.html as HTML

#
# 通过用户名和密码登录微博
# use requests
#
class Weibo(object):

    def __init__(self,username,password):
        # headers
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1',
                        'Referer':'','Content-Type':'application/x-www-form-urlencoded'}
        # session保存cookies
        self.session = requests.session()
        self.session.headers = self.headers
        self.username = username
        self.password = password

    # 获取form表单中post action必不可少的元素
    # rand,passwd,vk 随机产生
    #return rand,passwd,vk
    def get_rand(self,url):
        headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:42.0) Gecko/20100101 Firefox/42.0',
                        'Referer':''}

        req = urllib2.Request(url,urllib.urlencode({}),headers)
        resp = urllib2.urlopen(req)
        login_page = resp.read()
        rand = HTML.fromstring(login_page).xpath('//form/@action')[0]
        passwd = HTML.fromstring(login_page).xpath("//input[@type='password']/@name")[0]
        vk = HTML.fromstring(login_page).xpath("//input[@name='vk']/@value")[0]
        return rand,passwd,vk
    # 实现登录
    def login(self):
        login_url = 'http://login.weibo.cn/login/'
        rand,passwd,vk = self.get_rand(login_url)
        login_data = {'mobile':self.username,
                  'backTitle':'微博',
                  'backURL':'http://weibo.cn',
                  passwd:self.password,
                  'remember':'on',
                  'submit':'登录',
                  'vk':vk,
                      }
        #  session 保存了登录信息
        self.session.post(login_url+rand,data=login_data)

    def sock(self):
        # 方法一:
        # sock_url = 'http://weibo.cn/search/?pos=search&vt=4'
        # sock_data = dict(
        #     keyword = '股票',
        #     smblog = '搜微博'
        # )
        # req = self.session.post(sock_url,data=sock_data)

        #方法二:
        sock_url = 'http://weibo.cn/search/mblog?hideSearchFrame=&keyword=股票&page=1s&vt=4'
        req = self.session.get(sock_url)
        print req.content

username = ''
password = ''

test = Weibo(username,password)
test.login()
test.sock()




