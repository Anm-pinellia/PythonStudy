from tkinter import *
import hashlib

root = Tk()

text = Text(root, width=50, height=30, undo=True, autoseparators=False)
text.pack()

text.insert(INSERT, "测试Tags:Search.com")

def callback(event):
    text.edit_separator()


text.bind('<Key>', callback)

def show():
    text.edit_undo()

Button(root, text='撤销', command=show).pack()


mainloop()
