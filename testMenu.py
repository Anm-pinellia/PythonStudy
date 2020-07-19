from tkinter import *

root = Tk()



def sayhello():
    print('触发菜单栏选项')

def nothing():
    print('无事发生')

#初始化一个菜单
menu1 = Menu(root)

#初始化一个菜单的子选项菜单
filemenu = Menu(menu1, tearoff=False)
filemenu.add_command(label='打开', command=sayhello)
filemenu.add_command(label='保存', command=nothing)
filemenu.add_separator()
filemenu.add_command(label='退出', command=root.quit)
#完成初始化后，将其添加到父选项中
menu1.add_cascade(label='文件', menu=filemenu)




#初始化另一个菜单选项
editmenu = Menu(menu1, tearoff=False)
editmenu.add_command(label='剪切', command=nothing)
editmenu.add_command(label='拷贝', command=nothing)
#将子选项添加到父选项中
menu1.add_cascade(label='编辑', menu=editmenu)

#添加菜单
root.config(menu=menu1)

mainloop()
