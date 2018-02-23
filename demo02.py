import urllib
import urllib.request as rp
import re
import linecache
import os
import threading
#resp=rp.urlopen("http://www.92taotu.net/tag/wanimal")
path="/picture/ailili01"
zip_path="/workspace/zip/"
zip_name="ailili001.zip"
os.system("mkdir -p {0}".format(path))
def download(url,path):
    os.system("wget {0} -P {1}".format(url,path))
threading_list=[]
pic=[]
resp=rp.urlopen("http://www.zm123456.cn/taotu/10947.html")
html=resp.read()
html=html.decode("utf8")
#print(html)
p=r'<img src="[^"]*\.jpg" alt="艾栗栗无圣光">'
imglist=re.findall(p,html)
for i in imglist:
    i=i.split(sep="\"")[1]
    t=threading.Thread(target=download,args=(i,path,))
    t.start()
    threading_list.append(t)
    #pic.append(i)
for num in range(2,11):
    num=str(num)
    resp=rp.urlopen("http://www.zm123456.cn/taotu/10947_"+num+".html")
    html=resp.read()
    html=html.decode("utf8")
    #print(html)
    p=r'<img src="[^"]*\.jpg" alt="艾栗栗无圣光">'
    imglist=re.findall(p,html)
    for i in imglist:
        i=i.split(sep="\"")[1]
        t=threading.Thread(target=download,args=(i,path,))
        t.start()
        threading_list.append(t)
        #pic.append(i)
[t.join() for t in threading_list]
os.system("zip -r {0}{1} {2}".format(zip_path,zip_name,path))
#print(pic)
#print(len(pic))
