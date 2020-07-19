from tkinter import *
import math as m

root = Tk()

w = Canvas(root, width=200, height=200)
w.pack()

centre_x = 100
centre_y = 100
r = 50

points = [
    #左上
    centre_x-int(r*m.sin(2*m.pi/5)), centre_y-int(r*m.cos(2*m.pi/5)),

    #右上
    centre_x+int(r*m.sin(2*m.pi/5)), centre_y-int(r*m.cos(2*m.pi/5)),

    #左下
    centre_x-int(r*m.sin(2*m.pi/5/2)), centre_y+int(r*m.cos(2*m.pi/5/2)),
    
    #正上
    centre_x, centre_y-r, 
    
    #右下
    centre_x+int(r*m.sin(2*m.pi/5/2)), centre_y+int(r*m.cos(2*m.pi/5/2)),
    ]

w.create_polygon(points, outline='black', fill='red')



Button(root, text='删除全部', command=(lambda x=ALL:w.delete(x))).pack()

mainloop()
