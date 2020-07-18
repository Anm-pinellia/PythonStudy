from tkinter import *

root = Tk()

def showinfo():
    print('账号为: %s' % inputLabel1.get())
    print('密码为: %s' % inputLabel2.get())

v1 = StringVar()
v2 = StringVar()
    

#设置按钮
button1 = Button(root, text='提交信息', width=10, command=showinfo)
button2 = Button(root, text='退出界面', width=10, command=root.quit)
label1 = Label(root, text='账号')
label2 = Label(root, text='密码') 
inputLabel1 = Entry(root, textvariable=v1)
inputLabel2 = Entry(root, textvariable=v2, show='*')

#页面布局

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
inputLabel1.grid(row=0, column=1, padx=10, pady=5)
inputLabel2.grid(row=1, column=1, padx=10, pady=5)
button1.grid(row=2, column=0, sticky=W, padx=5, pady=10)
button2.grid(row=2, column=1, sticky=E, padx=5, pady=10)



mainloop()
