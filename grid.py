from tkinter import *

# Root widget

root = Tk()

# Label widget

mylabel = Label(root, text = "World").grid(row=0,column=0)
mylabel1 = Label(root, text = "Hello").grid(row = 1,column = 0)
mylabel2 = Label(root, text = "World")
mylabel3 = Label(root, text = "Hello plus World")
# Shoving to the screen

mylabel2.grid(row = 1,column =2)
mylabel3.grid(row =1,column=5)

# Creating a loop that will run until the game stops

root.mainloop()


