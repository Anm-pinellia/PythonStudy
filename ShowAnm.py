from tkinter import *
from PIL import Image,ImageTk


def callba():
    var.set('谢谢观看')


root = Tk()         #初始化一个窗口对象

var = StringVar()
var.set('我抓取的动漫图片')

frame1 = Frame(root)    #设置窗口中的框架
frame2 = Frame(root)

textLabel = Label(frame1, textvariable=var)        #设置框架1中的条目内容
textLabel.pack(side=LEFT)                               #设置条目的位置

im = Image.open('E:/动漫.jpg')
img = ImageTk.PhotoImage(im)

imgLabel = Label(frame1, image=img)
imgLabel.pack(side=RIGHT)

theButton = Button(frame2, text="阅", command=callba)    #设置button按下调用的方法
theButton.pack()        #设置Butoon的位置

frame1.pack()
frame2.pack()           #设置框架的位置


mainloop()
