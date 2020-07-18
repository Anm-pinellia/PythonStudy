from tkinter import *

root = Tk()

text = Text(root , width=200, height=100)
text.pack()

text.insert(INSERT, '开始你的想法:\n')

image1 = PhotoImage(file="E:/动漫.gif")

def viewidea():
    print(text.get('1.0', "1.8"))
    text.image_create(END, image=image1)

button = Button(text, text='打印内容进行输出', command=viewidea)


text.window_create(INSERT, window= button)


mainloop()
