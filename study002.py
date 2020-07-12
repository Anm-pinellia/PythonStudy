print("================分数判别系统==============")
while True:
    temp=int(input("请输入一个分数\n"))
    if temp>100:
        print("输入的分数过于离谱")
        break;
    elif temp>=90:
        print("成绩为A")
    elif temp>=80:
        print("成绩为B")
    elif temp>=70:
        print("成绩为C")
    elif temp>=60:
        print("成绩为D")
    elif temp<60:
        print("成绩不合格")
print("判别系统结束")
