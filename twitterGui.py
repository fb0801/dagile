'''twitter bot gui version'''

#modules to use
from tkinter import *
import re
from bs4 import BeautifulSoup
import requests
import json
import os


root = Tk()
root.title('Twitter Bot')




Entrybox = Entry(textvariable = name_input)
button_quit =Button(root, text="Exit program", command=root.quit)
button_quit.pack()
help_btn = Button( text = '?',font = 'Times 20 ',width = 1, height = 1, command = helpbtn)
help_btn.grid(row = 8, column = 9)#pack(side = RIGHT)

def helpbtn():
    messagebox.showinfo("Help", "Enter your login details to access the To Do List") # if the user clicks on help this messagebox will appear 





root.mainloop()



