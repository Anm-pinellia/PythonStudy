from tkinter import *

root = Tk()

s1 = Scale(root, from_=0, tickinterval=5, resolution=5, to=420, length=600)
s2 = Scale(root, from_=0, to=200, tickinterval=10, length=600, orient=HORIZONTAL)
s1.pack()
s2.pack()

def getxy():
    x = s1.get()
    y = s2.get()
    print(x, ' ', y)

Button(root, text='获取位置', command=getxy).pack(pady=20)

mainloop()
