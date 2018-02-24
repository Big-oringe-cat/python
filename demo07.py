#斐波拉切递归
def fab(n):
    if n<1:
        print('err number!')
        return -1
    if n==1 or n==2:
        return 1
    else:
        return fab(n-1) + fab(n-2)

result=fab(int(input('please insert a number:')))
if result != -1:
    print(result)
