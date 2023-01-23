'''application to fix the file 
part of https://github.com/fb0801/dagile created by Farhan Bhatti

Remove the square brackets and quotation marks from the ‘groups’ column
search for [ , replace all’. Repeat for ] and “:

'''

#application modules
import pandas as pd
import numpy as np
import os
import tkinter
from PIL import Image, ImageTk


from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Dagile Filter")
root.geometry('400x400') 

canvas = tkinter.Canvas(root, width = 400, height = 300)  

# loading the image
img = ImageTk.PhotoImage(file="image/dagile.png") 
Label(root,image=img).pack()


label = ttk.Label(text="Name")
entry = ttk.Entry()
btn = ttk.Button(text="Submit")
label.pack()
entry.pack()
btn.pack()
canvas.pack()



root.mainloop()