'''application to fix the file 
part of https://github.com/fb0801/dagile created by Farhan Bhatti

report filter

'''

#application modules
import pandas as pd
import numpy as np
import os
import tkinter
from tkinter.messagebox import showerror, showwarning, showinfo
from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk
from pynput.keyboard import Key, Listener
#import keyboard


root = Tk()
root.title("Dagile Filter")
root.geometry('510x300') 

canvas = tkinter.Canvas(root, width = 100, height = 100)  

# loading the image
img = ImageTk.PhotoImage(file="image/dagile.png") 
Label(root,image=img).pack()

def RFilter():
    pass


#gui widgets
label = ttk.Label(text="File Name")
entry = ttk.Entry()
btn = ttk.Button(text="Submit", command= RFilter)


label.pack()
entry.pack()
btn.pack()
canvas.pack()



root.mainloop()