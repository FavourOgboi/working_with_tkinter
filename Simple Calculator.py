"""Building a simple calculator with thinker"""

from ast import Lambda
from inspect import EndOfBlock
import math
from re import M
from tkinter import *

root = Tk()

root.title("SIMPLE CALCULATOR")

entry =  Entry(root , width = 40 , borderwidth = 5,bg="black",fg='white')

entry.grid(row = 0,column = 0,columnspan = 3,padx = 10,pady = 10)

def button_click(number):
    current = entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current) + str(number))

def button_add():
    first_num = entry.get()
    global f_num # Global variable
    global maths
    maths = "addition"
    f_num = int(first_num)
    entry.delete(0,END)

def button_sub():
    first_num = entry.get()
    global f_num # Global variable
    global maths
    maths = "substract"
    f_num = int(first_num)
    entry.delete(0,END)

def button_div():
    first_num = entry.get()
    global f_num # Global variable
    global maths
    maths = "divide"
    f_num = int(first_num)
    entry.delete(0,END)

def button_mul():
    first_num = entry.get()
    global f_num # Global variable
    global maths
    maths = "multiply"
    f_num = int(first_num)
    entry.delete(0,END)

def button_equals():
    second_num = entry.get()
    entry.delete(0,END)

    if maths == "addition":
        entry.insert(0, f_num + int(second_num))
    elif maths == "substract":
        entry.insert(0, f_num - int(second_num))
    elif maths == "multiply":
        entry.insert(0, f_num * int(second_num))
    else:
        entry.insert(0, f_num / int(second_num))

def button_clear():
    entry.delete(0,END)
# Define buttons

button_1 = Button(root,text = "1", padx = 40,pady = 20,command =  lambda: button_click(1))
button_2 = Button(root,text = "2", padx = 40,pady = 20,command =  lambda: button_click(2))
button_3 = Button(root,text = "3", padx = 40,pady = 20,command =  lambda: button_click(3))
button_4 = Button(root,text = "4", padx = 40,pady = 20,command =  lambda: button_click(4))
button_5 = Button(root,text = "5", padx = 40,pady = 20,command =  lambda: button_click(5))
button_6 = Button(root,text = "6", padx = 40,pady = 20,command =  lambda: button_click(6))
button_7 = Button(root,text = "7", padx = 40,pady = 20,command =  lambda: button_click(7))
button_8 = Button(root,text = "8", padx = 40,pady = 20,command =  lambda: button_click(8))
button_9 = Button(root,text = "9", padx = 40,pady = 20,command =  lambda: button_click(9))
button_0 = Button(root,text = "0", padx = 40,pady = 20,command =  lambda: button_click(0))
button_addition = Button(root,text = "+", padx = 39,pady = 20,command = button_add)
button_substraction = Button(root,text = "-", padx = 40,pady = 20,command = button_sub)
button_multiplication = Button(root,text = "X", padx = 39,pady = 20,command = button_mul)
button_division = Button(root,text = "/", padx = 39,pady = 20,command = button_div)
button_clear= Button(root,text = "Clear", padx =79,pady = 20,command = button_clear)
button_equals = Button(root,text = "=", padx = 91,pady = 20,command = button_equals)

# Display buttons on screen

button_1.grid(row =3, column =0)
button_2.grid(row =3, column =1)
button_3.grid(row =3, column =2)

button_4.grid(row =2, column =0)
button_5.grid(row =2, column =1)
button_6.grid(row =2, column =2)

button_7.grid(row =1, column =0)
button_8.grid(row =1, column =1)
button_9.grid(row =1, column =2)

button_0.grid(row =4, column =0)
button_clear.grid(row =4, column =1,columnspan=2)

button_addition.grid(row =5, column =0)
button_substraction.grid(row =6, column =0)
button_multiplication.grid(row =6, column =1)
button_division.grid(row =6, column =2)


button_equals.grid(row=5,column=1,columnspan=2)

root.mainloop()

