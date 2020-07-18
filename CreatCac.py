from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack(padx=10, pady=10)

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()

def cac():
    result = int(v1.get())+int(v2.get())
    v3.set(str(result))

def test(content):
    return content.isdigit()

testcmd = root.register(test)

num1 = Entry(frame, width=10, textvariable=v1, validate='key', validatecommand=(testcmd,'%P')).grid(\
    row=0, column=0)

signal1 = Label(frame, text='+').grid(row=0, column=1)

num2 = Entry(frame, width=10, textvariable=v2, validate='key', validatecommand=(testcmd,'%P')).grid(\
    row=0, column=2)

signal2 = Label(frame, text='=').grid(row=0, column=3)

num3 = Entry(frame, width=10, textvariable=v3, state='readonly').grid(\
    row=0, column=4)

button = Button(frame, text='计算', command=cac).grid(row=1, column=2)

mainloop()
