from tkinter import *

root = Tk()

theLB = Listbox(root, selectmode=BROWSE)
theLB.pack()

for item in ['1', '2', '3', '4']:
    theLB.insert(END, item)

theButton = Button(root, text='删除', \
                   command=lambda x=theLB:x.delete(ACTIVE))
theButton.pack()

mainloop()
