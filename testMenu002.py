from tkinter import *

root = Tk()

def sayhello():
    print('hello')


menu1 = Menu(root, tearoff=False)

menu1.add_command(label='删除', command=sayhello)
menu1.add_command(label='重命名', command=sayhello)

frame = Frame(root, width=512, height=512)
frame.pack()

def popup(event):
    menu1.post(event.x_root, event.y_root)


frame.bind('<Button-3>',popup)

