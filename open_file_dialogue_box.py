from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

root = Tk()
root.title('File opener')

def open():
    global img_label
    # file dialogue returns the location of files
    root.filename = filedialog.askopenfilename(initialdir= '/Users/Master/Desktop/thinker',title = "select a file", filetypes= (('py files'),('all files')))
    mylbl = Label(root,text = root.filename).pack()
    img = ImageTk.PhotoImage(Image.open(root.filename))
    img_label = Label(image = img).pack()

but = Button(root,text = 'open file',command = open).pack()

mainloop()
