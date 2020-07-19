from tkinter import *
import webbrowser

root = Tk()

text = Text(root, width=50, height=30)
text.pack()

text.insert(INSERT, "测试Tags:Search.com")

text.tag_add('link', 1.8, 1.13, 1.16)

text.tag_config('link', background='blue', foreground='white')
text.tag_config('link', background='yellow', foreground='red',underline=True)

def show_hand_cursor(event):
    text.config(cursor='arrow')

def show_xterm_cursor(event):
    text.config(cursor='xterm')

def click(event):
    webbrowser.open('http://www.bilibili.com')
    


text.tag_bind('link', '<Enter>', show_hand_cursor)
text.tag_bind('link', '<Leave>', show_xterm_cursor)
text.tag_bind('link', '<Button-1>', click)




mainloop()
