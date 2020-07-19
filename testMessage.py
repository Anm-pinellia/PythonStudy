from tkinter import *

root = Tk()

w1 = Message(root, text='短短的消息', width=100)
w1.pack()

w2 = Message(root, text='非常非常非常非常非常非常非常非常非常非常非常非常非常非常非常长的消息', width=100)
w2.pack()

mainloop()
