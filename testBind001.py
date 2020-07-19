from tkinter import *

root = Tk()

def callback(event):
    print(event.char)       #显示按键的字符串
    print(event.x,event.y)  #显示光标位置


frame = Frame(root, width=520, height=520)

frame.bind('<Motion>',callback)     #进入目标区域即触发

frame.focus_set()
frame.pack()

mainloop()
