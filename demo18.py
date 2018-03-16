import urllib.request as rq
import urllib.parse as p

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://fanyi.youdao.com/"
data = {}
data['type'] = 'AUTO'
data['i'] = 'I have a cat'
data['doctype'] = 'json'
data['xmlVersion'] = '1.6'
data['keyfrom'] = 'fanyi.web'
data['ue'] = 'UTF-8'
data['typoResult'] = 'true'
data = p.urlencode(data).encode('utf-8')
response = rq.urlopen(url,data)
html = response.read().decode('utf-8')
print(html)
