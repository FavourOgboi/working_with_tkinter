"""1 for checked and 0 for not checked, for value returned"""

from logging import root
from tkinter import *

root = Tk()

root.title("Check box")

# for the size of the windows to be specified 
root.geometry("400x400")

# To show selection if checked or not by clicking on the button
def slide():
    mylab = Label(root , text = var.get()).pack()

var = StringVar()
c = Checkbutton(root,text = "Check this box, i dare you", variable = var, onvalue= "Clicked",offvalue="Unclicked")
c.deselect()
c.pack()

but = Button(root,text="Show Selection",command = slide).pack()

root.mainloop()