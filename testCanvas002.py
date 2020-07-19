from tkinter import *

root = Tk()

w = Canvas(root, width=200, height=100)
w.pack()


w.create_rectangle(40, 20, 160, 80, dash=(4,4), fill='black')
w.create_oval(40, 20, 160, 80, fill='red')


w.create_text(100,50,text='测试')


Button(root, text='删除全部', command=(lambda x=ALL:w.delete(x))).pack()



mainloop()
