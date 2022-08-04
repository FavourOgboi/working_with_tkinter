from tkinter import *
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.title("Code")
root.geometry('600x100')

def graph():
    house_prices = np.random.normal(200000,2500,5000)
    plt.hist(house_prices, 50)
    plt.show()

but = Button(root,text='Graph',command=graph).pack()

root.mainloop()
