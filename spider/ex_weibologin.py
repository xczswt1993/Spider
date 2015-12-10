#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'stone'

import urllib
import urllib2
import cookielib

import lxml.html as HTML

class Weibo(object):

    def __init__(self,username,password):
        self.cookie = cookielib.LWPCookieJar()
        self.cookie_processor = urllib2.HTTPCookieProcessor(self.cookie)
        self.opener = urllib2.build_opener(self.cookie_processor)
        urllib2.install_opener(self.opener)

        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1',
                        'Referer':'','Content-Type':'application/x-www-form-urlencoded'}

        self.username = username
        self.password = password

    def get_rand(self, url):
        headers = {'User-Agent':'Mozilla/5.0 (Windows;U;Windows NT 5.1;zh-CN;rv:1.9.2.9)Gecko/20100824 Firefox/3.6.9',
                   'Referer':''}
        req = urllib2.Request(url ,urllib.urlencode({}), headers)
        resp = urllib2.urlopen(req)
        login_page = resp.read()
        rand = HTML.fromstring(login_page).xpath("//form/@action")[0]
        passwd = HTML.fromstring(login_page).xpath("//input[@type='password']/@name")[0]
        vk = HTML.fromstring(login_page).xpath("//input[@name='vk']/@value")[0]
        return rand, passwd, vk

    def login(self):

        login_url = 'http://login.weibo.cn/login/'
        rand,passwd,vk = self.get_rand(login_url)

        login_data = urllib.urlencode({
            'mobile': self.username,
            passwd: self.password,
            'remember': 'on',
            'backURL': 'http://weibo.cn/',
            'backTitle': '新浪微博',
            'vk': vk,
            'submit': '登录',
            'encoding': 'utf-8'
        })
        url = login_url + rand
        req = urllib2.Request(url,login_data,self.headers)
        result = urllib2.urlopen(req)
        print result.read()

username = ''
password = ''

test = Weibo(username,password)
test.login()