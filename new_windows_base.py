from tkinter import *

root = Tk()
root.title('New windows')

def open():
    top = Toplevel()
    top.title('SECOND WINDOW')
    mylabel = Label(top, text = 'Hellow world').pack()

btn = Button(root,text = "Open second window",command = open).pack()
root.mainloop()
