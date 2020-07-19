from tkinter import *

root = Tk()

w = Spinbox(root, from_=0, to=99)
w.pack()

w1 = Spinbox(root, values=('hello','你好','世界'))
w1.pack()

mainloop()
