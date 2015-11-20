#-*-coding:utf-8-*-
from ghost import Ghost
ghost = Ghost()
with ghost.start() as session:
    session.set_proxy('socks5','127.0.0.1',1080)
    page,extra_sources = session.open('http://pachong.org/socks.html',timeout=200)
    result,sources = session.evaluate('document.write((16223^cock)+204);')
    print sources
