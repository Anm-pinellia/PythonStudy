from tkinter import *

root = Tk()

group = LabelFrame(root, text='你喜欢哪种脚本语言?', padx=5,pady=5)
group.pack(padx=10,pady=10)

LANGS = {
        ('Python',1),
        ('Perl',2),
        ('Ruby',3),
        ('Lua',4)}

v = IntVar()
v.set(1)

for lang,num in LANGS:
    b = Radiobutton(group, text=lang, variable=v, value=num,indicatoron=False)
    b.pack(fill=X)

mainloop()
