from msilib.schema import RadioButton
from tkinter import *
from tkinter.ttk import Labelframe
# import pillow for image

from PIL import ImageTk
from PIL import Image

root = Tk()
root.title('Radio Buttons')

# not using a loop

favour = IntVar()
favour.set('2')
# To get the variable favour.get()
ogboi = StringVar()
ogboi.set('get')
# update the var depending on the button clicked

def clicked(value):
    mylabel = Label(root,text = value)
    mylabel.pack()

radio1 = Radiobutton( root,text = "Option 1", variable = favour,value = 1, command = lambda: clicked(favour.get())).pack()
radio2 = Radiobutton( root,text = "Option 2", variable = ogboi ,value = 2)
radio2.pack()

mybutton = Button(root,text = "click me",command= lambda: clicked(favour.get()))
mybutton.pack()


# Using a loop

label = Label(root,text="Loop part").pack()

def clicked(value):
    mylabel = Label(root,text = value)
    mylabel.pack()

modes = [
    ('pepperoni','pepperoni'),
    ('cheese','cheese'),
    ('mushrooms','mushrooms'),
    ('onoions','onoions'),
    ]

pizz = StringVar()

for text, mode in modes:
    Radiobutton(root,text = text , variable=pizz,value = mode,anchor=W).pack()

mybutton = Button(root,text = "click me",command= lambda: clicked(pizz.get()))
mybutton.pack()


root.mainloop()
