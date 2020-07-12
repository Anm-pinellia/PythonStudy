try:
    a=1+'1'
    print(a)
except TypeError as reason:
    print('错误输出的字符类型是',str(reason))
