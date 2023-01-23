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

canvas.pack()  
  


#img = ImageTk.PhotoImage(Image.open("dagile.png"))
#img = img.resize((50, 50), Image.ANTIALIAS)

# Resize the image using resize() method
#resized_image = img.resize((10, 10), Image.ANTIALIAS)
  
# arranging image parameters in the application
#canvas.create_image(0, 0, anchor = NW,image = resized_image) 

#load = ImageTk.PhotoImage(file="image/dagile.png") 

label = ttk.Label(text="Name")
entry = ttk.Entry()
btn = ttk.Button(text="Submit")
label.pack()
entry.pack()
btn.pack()

root.mainloop()