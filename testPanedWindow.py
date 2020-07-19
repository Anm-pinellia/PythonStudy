from tkinter import *

root = Tk()

m = PanedWindow(showhandle = True, sashrelief=SUNKEN)
m.pack(fill=BOTH, expand=1)


left = Label(m, text='左窗格')
m.add(left)

m2 = PanedWindow(orient=VERTICAL, showhandle = True, sashrelief=SUNKEN)
m.add(m2)

right1 = Label(m2, text='右窗格1')
m2.add(right1)

right2 = Label(m2, text='右窗格2')
m2.add(right2)




mainloop()
