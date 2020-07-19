from tkinter import *
from tkinter import filedialog

root = Tk()

def callback():
    print('开始运行')
    fileName = filedialog.askopenfilename()     #以filedialog对话框返回文件名
    print(fileName)

Button(root, text='打开文件', command=callback).pack()

mainloop()
