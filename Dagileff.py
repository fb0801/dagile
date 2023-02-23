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

def dFilter():
    name = entry.get()
    if len(name) == 0:
        tkinter.messagebox.showerror(title="Error", message="Error no name given")
    else:
        #function to filter the file
        work =pd.read_csv("Dagile Users.csv")
        newfile = work.drop(columns=['User Status', 'Tutor','Date imported','Notes'])
        newfile['groups'] =newfile['groups'].str.replace('[', '')
        newfile['groups'] =newfile['groups'].str.replace(']', '')
        newfile['groups'] =newfile['groups'].str.replace('"', '')
       
        nfn = name
        dagile = newfile.to_csv(f'{name}.csv')
        tkinter.messagebox.showinfo(title="Success", message="Task completed")
        entry.delete(0, END)




#gui widgets
label = ttk.Label(text="File Name")
entry = ttk.Entry()
btn = ttk.Button(text="Submit", command= dFilter)
entry.bind('<Return>',dFilter)


label.pack()
entry.pack()
btn.pack()
canvas.pack()



root.mainloop()