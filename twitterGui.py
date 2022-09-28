'''twitter bot gui version'''

#modules to use
from tkinter import *
import re
from bs4 import BeautifulSoup
import requests
import json
import os


class TwitterBot(Frame):
    def __init__(self, master):
        Frame.__init__(self, master) # a frame to contain everything in
        self.grid() # to say we are using grids
        self.speak() # to call the screen method


        

def helpbtn(self):
    self.messagebox.showinfo("Help", "Enter your login details to access the To Do List") # if the user clicks on help this messagebox will appear 



def speak(self):
    self.Entrybox = Entry(textvariable = name_input)
    button_quit =Button(root, text="Exit program", command=root.quit)
    button_quit.pack()
    help_btn = Button( text = '?',font = 'Times 20 ',width = 1, height = 1, command = self.helpbtn)
    help_btn.grid(row = 8, column = 9)#pack(side = RIGHT)
    self.help_btn = Button(self, text = '?',font = 'Times 20 ',width = 1, height = 1, command = self.helpbtn)
    self.help_btn.grid(row = 8, column = 9)#pack(side = RIGHT)

root = Tk()
name_input = StringVar()


root.title('Twitter Bot')
root.mainloop()
