from tkinter import *

# Root widget

root = Tk()

# entry widget

entry = Entry(root,width=50,bg='black',fg='white',borderwidth=5,border=3)
entry.pack()

# Adding a default text in the text box

entry.insert(0,"Enter your name : ")

def click():
    what =  input("Enter what you love: ") +" "+ "I love food"
    labels = Label(root,text = "Hello" +" "+ entry.get() +" "+ what)
    labels.pack()

button = Button(root,text = "Click Me After Inputing Test",command=click)
button.pack()

# Creating a loop that will run until the game stops

root.mainloop()

