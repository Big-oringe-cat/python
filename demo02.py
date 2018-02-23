import urllib
import urllib.request as rp
import re
import linecache
import os
import threading
path="/picture/ailili001" #存图路径
zip_path="/workspace/zip01/" #压缩文件存放路径
zip_name="ailili001.zip" #压缩文件名
#若不存在目录先创建目录
if not os.path.exists(path):
    os.system("mkdir -p {0}".format(path))
if not os.path.exists(zip_path):
    os.system("mkdir -p {0}".format(zip_path))
#定义下载函数，调shell命令wget下载图片，需提供参数：url，路径
def download(url,path):
    os.system("wget {0} -P {1}".format(url,path))
threading_list=[] #线程列表
#爬第一页图片
resp=rp.urlopen("http://www.zm123456.cn/taotu/10947.html") #打开url
html=resp.read() #获取html内容
html=html.decode("utf8") #utf8解码网页
p=r'<img src="[^"]*\.jpg" alt="艾栗栗无圣光">' #设置匹配图片的正则
imglist=re.findall(p,html) #按照正则匹配网页
for i in imglist:
    i=i.split(sep="\"")[1] #截取图片静态地址（url部分）
    t=threading.Thread(target=download,args=(i,path,)) #告诉线程去调用download函数，参数需要在args中添加
    t.start() #开启线程
    threading_list.append(t) #加入线程列表
#爬后面页的图片
for num in range(2,11):
    num=str(num)
    resp=rp.urlopen("http://www.zm123456.cn/taotu/10947_"+num+".html")
    html=resp.read()
    html=html.decode("utf8")
    p=r'<img src="[^"]*\.jpg" alt="艾栗栗无圣光">'
    imglist=re.findall(p,html)
    for i in imglist:
        i=i.split(sep="\"")[1]
        t=threading.Thread(target=download,args=(i,path,))
        t.start()
        threading_list.append(t)

[t.join() for t in threading_list] #主线程等待所有子线程结束,即下载完所有图片再进行打包
os.system("zip -r {0}{1} {2}".format(zip_path,zip_name,path)) #打包
