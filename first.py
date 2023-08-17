from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Task 1 : Digital Clock")

def time():
    string = strftime('%H:%M:%S %p')
    Label.config(text=string)
    Label.after(1000,time)

Label = Label(root, font=("DS-DIGII",80), background = "black", foreground = "white")
Label.pack(anchor='center')
time()

mainloop()  




