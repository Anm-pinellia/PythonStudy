from tkinter import *

root = Tk()

w = Canvas(root, width=960, height=720)
w.pack()

#python不支持绘制点，但是可以绘制一个很小的圆形并填充来代替绘制点

def paint(event):
    x1, y1 = (event.x-1), (event.y - 1)
    x2, y2 = (event.x+1), (event.y + 1)
    w.create_oval(x1,y1,x2,y2,fill='red')

#将鼠标左键与paint方法绑定

w.bind('<B1-Motion>', paint)

Label(root, text='按住鼠标左键开始绘图').pack(side=BOTTOM)

mainloop()  
              
