with open('/tmp/test1.txt','r+') as f:
    print(f.seek(0,0))
    print(f.tell())
    for i in f:
        print(i,end='')
    print(f.tell())
    f.write('乖乖站好\n')
    print(f.tell())
    print(f.seek(0,0))
    for i in f:
        print(i,end='')
    print(f.tell())
