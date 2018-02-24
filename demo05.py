#recursion递归
#输入1返回1，输入其他整数会进行阶乘（递归调用自己）
def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)
number=int(input('please insert a number:'))
result=factorial(number)
print("%d 的阶乘是 : %d" % (number,result))
