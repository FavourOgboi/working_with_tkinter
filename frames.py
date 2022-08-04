from tkinter import *
from tkinter.ttk import Labelframe
# import pillow for image

from PIL import ImageTk
from PIL import Image

root = Tk()
root.title('Frames')

frame = LabelFrame( root ,text = "This is a frame",padx = 50,pady = 50)
frame.pack(padx=100,pady=100)

b = Button(frame,text = "Don't click here",)
b2 = Button(frame,text = "Don't click here also",)
b.grid(row=0,column=0)
b2.grid(row=1,column=1)


root.mainloop()