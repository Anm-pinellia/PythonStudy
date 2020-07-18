from tkinter import *

Girls = ['杨玉环','貂蝉','西施','王昭君']
Var = []

root = Tk()

def chStatus(var):
    if var==1:
        status='已选择该人物'
    else:
        status='未选择该人物'
    return status
    

for girl in Girls:
    var = IntVar()
    Var.append(var)
    status = StringVar()
    b = Checkbutton(root, text=girl ,variable=var)
    status = var.set(chStatus(var))
    st = Label(root, textvariable=var)
    b.pack()
    st.pack()

mainloop()
