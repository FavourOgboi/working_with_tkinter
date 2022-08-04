from tkinter import *
from urllib.request import urlretrieve
# import pillow for image

from PIL import ImageTk
from PIL import Image


root = Tk()
root.title("Code")

# Working with images
urlretrieve('https://i.imgur.com/SkPbq.jpg', 'chart.jpg');
img_label = Label(image = ImageTk.PhotoImage(Image.open('chart.jpg')))
img_label.pack()

# An exit button

button_quit = Button(root,text = "Exit Program", command = root.quit)

button_quit.pack()

root.mainloop()