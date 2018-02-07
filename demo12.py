def showMaxFactor(num):
    count = num//2
    while count>1:
        if num%count==0:
            print('{0}的最大公约数是{1}'.format(num,count))
            break
        count -=1
    else:
        print('{0}是个素数'.format(num))
num=int(input('请输入一个整数'))
showMaxFactor(num)
