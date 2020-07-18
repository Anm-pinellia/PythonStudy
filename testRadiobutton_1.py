from tkinter import *

root =Tk()

v = IntVar()
v.set(1)

Radiobutton(root,text='杨玉环', variable=v, value=1).pack(anchor=W)
Radiobutton(root,text='西施', variable=v, value=2).pack(anchor=W)
Radiobutton(root,text='貂蝉', variable=v, value=3).pack(anchor=W)
Radiobutton(root,text='王昭君', variable=v, value=4).pack(anchor=W)

mainloop()
