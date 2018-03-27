# _*_ coding:utf-8 _*_
import urllib.request as rq
import re
from bs4 import BeautifulSoup as BS

def main():
    url = "http://baike.baidu.com/view/284853.html"
    response = rq.urlopen(url)
    html = response.read()
    soup = BS(html,"html.parser")

    
    #for i in soup.find_all(href = re.compile("view")):
    #    print(i.text, "->", ''.join(["http://baike.baidu.com", \
#i["href"]]))
    print(soup.find_all(href = re.compile("view")))

if __name__ == "__main__":
    main()
