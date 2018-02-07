try:
    sum=1+1
    raise ZeroDivisionError('除数不能为0')
    #with open(input('请输入文件名：'),'r') as f:
    #    print(f.readlines())
except (OSError,TypeError,ZeroDivisionError) as reason:
    print(str(reason))
finally:
    print('over!')
