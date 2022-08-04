from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Message box")

def popup():
    messagebox.showinfo('This is my pop up','Hello World')
    messagebox.showwarning("danger")
    messagebox.showerror("error")
    messagebox.askquestion("Question")
    messagebox.askokcancel("okcancel")
    messagebox.askyesno("yesno")
Button( root ,text = "pop up", command = popup  ).pack()

# How to work with this message boxes

# this can work for okcancel
    #prints 1 or o
def pop():
    response = messagebox.askyesno('This is my pop up','Hello World')
    label = Label(root,text = response ).pack()
    if response == 1:
        Label(root , text = "you clickked yes").pack()
    else:
        Label(root , text = "you clicked no").pack()

# for askquestion
    #prints yes or no
# for show error
# for showwarning 
# for showinfo
    # prints ok if ok is picked

Button( root ,text = "pop response up", command = pop).pack()
root.mainloop()