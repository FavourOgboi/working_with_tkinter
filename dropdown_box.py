"""1 for checked and 0 for not checked, for value returned"""

from logging import root
from tkinter import *

root = Tk()

root.title("dropdown box")

# for the size of the windows to be specified 
root.geometry("400x400")

def show():
    mylab = Label(root,text = clicked.get() ).pack()

clicked = StringVar()
# Default
clicked.set("Monday")

drop = OptionMenu(root , clicked , "Monday","Tuesday","Wednesday","Thursday","Friday")
drop.pack()

but = Button(root,text="Show Selection",command = show).pack()

# Using a list
def showing():
    mylab = Label(root,text = click.get() ).pack()

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
    ]

click = StringVar()
# Default
click.set(options[0])

drop = OptionMenu(root , click , *options)
drop.pack()

but = Button(root,text="Show Selection",command = showing).pack()


root.mainloop()