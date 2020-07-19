from tkinter import *

root = Tk()

def sayhello():
    print('hello')

mb = Menubutton(root, text='Menubutton的测试项', relief=RAISED)
mb.pack()

menu1 = Menu(mb, tearoff=False)

menu1.add_command(label='删除', command=sayhello)
menu1.add_command(label='重命名', command=sayhello)

mb.config(menu=menu1)

mainloop()
 
