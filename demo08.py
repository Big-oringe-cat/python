f=open("/tmp/test1.txt",'rb+')
#f.writelines(["hahaha\n","aiheihei\n","henghengheng\n"])
print(list(f))
f.seek(2,0)
print(f.tell())
f.seek(1,1)
print(f.tell())
f.read(2)
print(f.readline())
print(f.readline())
#for i in f.readlines():
#    #i=i.split('\n')[0]
#    print(i,)
print(f.tell())
f.close()