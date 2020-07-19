from tkinter import *

root = Tk()

w = Canvas(root, width=200, height=100)
w.pack()
'''
line1 = w.create_line(0,50,200,50,fill='yellow')
line2 = w.create_line(100,0,100,100,fill='red',dash=(4,4))
rect1 = w.create_rectangle(50,25,150,75,fill='blue')

w.coords(line1, 0, 25, 200, 25)
w.itemconfig(rect1,fill='red')
w.delete(line2)
'''
line1 = w.create_line(0,0,200,100,fill='red',width=3)
line2 = w.create_line(200,0,0,100,fill='red',width=3)
rect1 = w.create_rectangle(40,20,160,80,fill='green')
rect2 = w.create_rectangle(65,35,135,65,fill='blue')

w.create_text(100,50,text='测试')


Button(root, text='删除全部', command=(lambda x=ALL:w.delete(x))).pack()



mainloop()
