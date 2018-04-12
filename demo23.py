import urllib.request as rq
import urllib.parse as p
import re
from bs4 import BeautifulSoup as BS

def main():
    #keyword = input("请输入")
    keyword = "猪八戒"
    keyword = p.urlencode({"word":keyword})
    
    #访问网址,该网址直接返回当前公网出口ip
    url = 'http://members.3322.org/dyndns/getip'
    #这是代理IP,先telnet一下确定能不能通
    ip = '119.28.138.104:3128'
    proxy = {'http':ip}
    #创建ProxyHandler
    proxy_support = rq.ProxyHandler(proxy)
    #创建Opener
    opener = rq.build_opener(proxy_support)
    head = {}
    #添加User Angent
    #head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    opener.addheaders = [('User-Agent',head['User-Agent'])]
    #安装OPener
    rq.install_opener(opener)
    #使用自己安装好的Opener
    response = rq.urlopen("http://baike.baidu.com/search/word?%s" %keyword)
    html = response.read()
    #html = html.decode('utf-8')
    soup = BS(html,"html.parser")
    #print(soup)
    #print(type(soup.find_all(href = re.compile("view"))))
    for i in soup.find_all(href = re.compile("view")):
        content = ''.join([i.text])
        url2 = ''.join(["http://baike.baidu.com", i["href"]])
        response2 = rq.urlopen(url2)
        html2 = response2.read()
        soup2 = BS(html2,"html.parser")
        if soup2.h2:
            content = ''.join([content, soup2.h2.text])
        content = ''.join([content, "->", url2])
        print(content)

if __name__ == "__main__":
    main()
