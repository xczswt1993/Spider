#!/usr/bin/env python
#-*-coding:utf-8 -*-
__author__ = 'stone'

import re
import requesocks
import socket
import socks
import js2py
import json
import threading
import MySQLdb
proxyUrl = 'http://pachong.org/high.html'
checkUrl = 'http://www.whatismyip.com.tw'

#ip_port 存放抓取到的ip地址和端口
ip_port = {}
#checkedProxy 存放验证过的ip地址和端口
checkedProxy = []

#抓取方法
def getProxy():
    #socks5访问pachong.org
    socks.set_default_proxy(socks.SOCKS5,'127.0.0.1',1080)
    socket.socket = socks.socksocket
    r = requesocks.get(proxyUrl)
    html = r.text.encode('utf-8')
    #匹配 网页定义的js声明
    reg_script_head = '<script type.*?>(.*?)</script>'
    pattern_script_head = re.compile(reg_script_head,re.S)
    result_of_script_head = re.findall(pattern_script_head,html)

    #匹配ip端口
    reg_port = '<td><script>(.*?)</script>'
    pattern_port = re.compile(reg_port,re.S)
    result_of_port = re.findall(pattern_port,html)

    #匹配ip地址
    reg_ip = '<td>([0-9]+(?:\.[0-9]+){0,3})</td>'
    pattern_ip = re.compile(reg_ip,re.S)
    result_of_ip = re.findall(pattern_ip,html)

    for i,item in enumerate(result_of_ip):
        jsevalPort = result_of_script_head[2] + result_of_port[i]
        js = ''' function add(){
        %s
        }
        add()''' % jsevalPort.replace('document.write','return')
        result = js2py.eval_js(js)
        ip_port[item] = result

#多线程验证代理的可用性
class checkProxy(threading.Thread):
    def __init__(self,ip,port):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port

    def checkproxy(self):

        session = requesocks.session()
        reg = '<h2>(.*?)</h2>'
        proxiesDict = {'http':'%s:%s'%(self.ip,self.port),
                        'https':'%s:%s'%(self.ip,self.port)}
        session.proxies = proxiesDict
        try:
            req = session.get(checkUrl)
            html = req.text
            pattern = re.compile(reg,re.S)
            result = re.search(pattern,html)
            if result is not None:
                print result.group(1)
                checkedProxy.append({self.ip:self.port})
            else:
                print  threading.current_thread().name,u':不可用'
        except Exception,e:
            print self.ip,u'连接超时'

    def run(self):
        self.checkproxy()

#线程列表
checkThreads = []

if __name__ =='__main__':
    getProxy()

for ip,port in ip_port.iteritems():
    t = checkProxy(ip,port)
    checkThreads.append(t)

#启动线程
for i in range(len(checkThreads)):
    checkThreads[i].start()

for i in range(len(checkThreads)):
    checkThreads[i].join()

jsonFile = 'ip_port.json'

#写入json
with open(jsonFile,'w') as f:
    f.write(json.dumps(checkedProxy))

jsonDict = {}
#从json中读取
with open(jsonFile,'r') as f:
    jsonDict = json.load(f)
#数据库写入
def db_insert(ip,port):
    try:
        conn = MySQLdb.connect(host='localhost',user='root',passwd='qaz10',db='test')
        cursor = conn.cursor()
        cursor.excute("insert into proxy (ip,port,type) values (%s,%s,'http')" %(ip,port))
        cursor.commit()
        cursor.close()
    except MySQLdb.Error,e:
        print e.message

for ip,port in jsonDict.iteritems():
    db_insert(ip,port)