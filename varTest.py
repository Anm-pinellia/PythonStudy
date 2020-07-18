from tkinter import *

root = Tk()

v = IntVar()

c = Checkbutton(root, text='测试CheckButton', variable=v)
c.pack()

status = Label(root, textvariable=v)
status.pack()

mainloop()
