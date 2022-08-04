from logging import root
from tkinter import *

root = Tk()

root.title("Slider")

# for the size of the windows to be specified 
root.geometry("400x400")

# To return the number of where user slided to on the slides

def slide():
    label = Label(root,text=horizontal.get())
    label.pack()
    label = Label(root,text=vertical.get())
    label.pack()
    # To affect the root length
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))


vertical = Scale(root , from_ = 0 , to = 400)
vertical.pack()

horizontal = Scale(root , from_ = 0 , to = 400, orient= HORIZONTAL)
horizontal.pack()

btn = Button(root,text = 'Click Me',command = slide).pack()

root.mainloop()