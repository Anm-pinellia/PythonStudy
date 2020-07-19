from tkinter import *

root = Tk()

def create():
    top = Toplevel()
    top.title('你好啊')
    top.attributes('-alpha',0.5)

    msg = Message(top, text='hello world!')
    msg.pack()

Button(root, text='创建顶级窗口', command=create).pack(side=LEFT)

mainloop()
