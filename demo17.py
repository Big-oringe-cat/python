import urllib.request

rp = urllib.request.urlopen("http://placekitten.com/g/1000/800")
cat_img = rp.read()
print(rp.getcode(),'\n',rp.info(),'\n',rp.geturl(),'\n',)
#with open('cat_001.jpg', 'wb') as f:
#    f.write(cat_img)
