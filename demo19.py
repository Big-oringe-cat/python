import urllib.request
import urllib.parse
import json
import re

#url = 'http://www.ip138.com/'
url = 'http://ip.cn/'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
proxy = urllib.request.ProxyHandler({'http':'59.48.148.226:61202'})
opener = urllib.request.build_opener(proxy)
urllib.request.install_opener(opener)
req = urllib.request.Request(url=url, headers=header,)
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')
print(html)
p = r'(?:(?:25[0-4]|2[0-4]\d|1\d\d|\d\d|\d)\.){3}(?:25[0-4]|2[0-4]\d|1\d\d|\d\d|\d)'
iplist = re.findall(p,html)
for i in iplist:
    print(i)
