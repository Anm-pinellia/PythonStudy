from tkinter import *
import hashlib

root = Tk()

text = Text(root, width=50, height=30)
text.pack()

text.insert(INSERT, "测试Tags:Search.com")
contents = text.get(1.0, END)

def getSig(contents):
    m = hashlib.md5(contents.encode())
    return m.digest()

sig = getSig(contents)

def check():
    contents = text.get(1.0, END)
    print('原本MD5的值',sig)
    print('后来MD5的值',sig)
    if sig != getSig(contents):
        print('检测到的值发生变化')
    else:
        print('无事发生')


Button(root, text='检查是否变化', command=check).pack()




mainloop()
