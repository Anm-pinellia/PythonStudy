from tkinter import *
from tkinter import colorchooser


root = Tk()

def callback():
    colorName = colorchooser.askcolor()
    print(colorName)

Button(root, text='选择颜色', command=callback).pack()

mainloop()
