#斐波拉切
def fab(n):
    a1=1
    a2=1
    a3=1
    if n<1:
        print('insert err!')
        return -1
    while (n-2)>0:
        a3=a1+a2
        a1=a2
        a2=a3
        n -=1
    return a3

result=fab(int(input('几个月?')))
if result !=-1:
    print(result)
