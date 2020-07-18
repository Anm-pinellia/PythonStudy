import tkinter as tk

class App:
    def __init__(self,master):
        frame = tk.Frame(master)
        frame.pack(side = tk.LEFT ,  padx=10 ,pady=20)

        self.hi_here = tk.Button(frame, text='你好啊，小朋友', fg='black',command = self.say_hi)
        self.hi_here.pack()

    def say_hi(self):
        print('点击了按钮操作')






root = tk.Tk()
app = App(root)
root.mainloop()
