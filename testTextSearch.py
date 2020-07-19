from tkinter import *
import hashlib

root = Tk()

text = Text(root, width=50, height=30)
text.pack()

text.insert(INSERT, "测试Tags:Search.com")

start = '1.0'

def getIndex(text, index):
    return tuple(map(int, str.split(text.index(index),'.')))

while True:
    pos = text.search("o", start, stopindex=END)
    if not pos:
        break
    print('该字符的位置是：',getIndex(text,pos))
    start = pos + "+1c"


mainloop()
