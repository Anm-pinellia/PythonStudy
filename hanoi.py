print('--------汉诺塔问题的递归算法应用--------------')

def hanoi(n,x,y,z):
    if n==1:
        print(x,'--->',z) #如果只有一个圆盘，则从x移动到z
    else:
        hanoi(n-1,x,z,y)    #将前n-1个圆盘从x移动到y上
        print(x,'--->',z)   #将x上的第n个圆盘移动到z上
        hanoi(n-1,y,x,z)    #将y上的最后一个圆盘移动到z上

n=int(input('请输入汉诺塔的圆盘数量:'))
x='X'
y='Y'
z='Z'
hanoi(n,x,y,z)
