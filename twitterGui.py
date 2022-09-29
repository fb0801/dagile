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

options ={}


class TwitterBot:
    def __init__(self, master):
        self.master = master
        self.Frame =tk.Frame(self.master) # a frame to contain everything in
        
        master.title('Twitter Bot')
        

        self.user_input = tk.Entry(textvariable = name_input)
        self.user_input.pack()
        self.button_quit =tk.Button(self, text="Exit program", command=master.destroy)
        self.button_quit.pack()
        self.help_btn = tk.Button(self, text = '?',font = 'Times 20 ',width = 1, height = 1, command = self.bothelp)
        self.help_btn.grid(row = 8, column = 9)#pack(side = RIGHT)



    def bothelp(self):
        self.messagebox.showinfo("Help", "Enter the duration") # if the user clicks on help this messagebox will appear 

    def botSearch(self):
        pass




root = tk.Tk()
name_input = StringVar()


Terry = TwitterBot(root)
root.mainloop()


#if __name__ == "__main__":
    #takes user to the main menu using magic method/dunders
    #main()