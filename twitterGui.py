'''twitter bot gui version'''

#modules to use
#from tkinter import messagebox
from tkinter import *
import tkinter as tk
import re
from bs4 import BeautifulSoup
import requests
import json
import os


class TwitterBot:
    def __init__(self, master):
        self.master = master
        self.Frame =Frame(self.master) # a frame to contain everything in
        
        master.title('Twitter Bot')
        

        user_input = Entry(textvariable = name_input)
        user_input.pack()
        button_quit =Button(self, text="Exit program", command=root.destroy)
        button_quit.pack()
        help_btn = Button(self, text = '?',font = 'Times 20 ',width = 1, height = 1, command = self.bothelp)
        help_btn.grid(row = 8, column = 9)#pack(side = RIGHT)



    def bothelp(self):
        self.messagebox.showinfo("Help", "Enter your login details to access the To Do List") # if the user clicks on help this messagebox will appear 

    def botSearch(self):
        pass




root = Tk()
name_input = StringVar()


Terry = TwitterBot(root)
root.mainloop()


#if __name__ == "__main__":
    #takes user to the main menu using magic method/dunders
    #main()