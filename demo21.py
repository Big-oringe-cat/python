# _*_ coding: utf-8 _*_
from urllib import request

if __name__ == "__main__":
    #访问网址,该网址直接返回当前公网出口ip
    url = 'http://members.3322.org/dyndns/getip'
    #这是代理IP,先telnet一下确定能不能通
    ip = '119.28.138.104:3128'
    proxy = {'http':ip}
    #创建ProxyHandler
    proxy_support = request.ProxyHandler(proxy)
    #创建Opener
    opener = request.build_opener(proxy_support)
    head = {}
    #添加User Angent
    #head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    opener.addheaders = [('User-Agent',head['User-Agent'])]
    #安装OPener
    #request.install_opener(opener)
    #使用自己安装好的Opener
    #response = request.urlopen(url)
    
    response = opener.open(url)

    html = response.read().decode('utf-8')
    print(html)
