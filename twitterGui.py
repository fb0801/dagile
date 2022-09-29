'''twitter bot gui version'''

#modules to use
from tkinter import messagebox
from tkinter import *
import re
from bs4 import BeautifulSoup
import requests
import json
import os


class TwitterBot:
    def __init__(self, master):
        #Frame.__init__(self, root) # a frame to contain everything in
        self.master = master
        master.title('Twitter Bot')
        #self.grid() # to say we are using grids
        #speak() # to call the screen method

        user_input = Entry(textvariable = name_input)
        user_input.pack()
        button_quit =Button(root, text="Exit program", command=root.quit)
        button_quit.pack()
        help_btn = Button(self, text = '?',font = 'Times 20 ',width = 1, height = 1, command = TwitterBot.bothelp)
        help_btn.grid(row = 8, column = 9)#pack(side = RIGHT)


    
        #self.help_btn = Button(self, text = '?',font = 'Times 20 ',width = 1, height = 1, command = self.helpbtn)
        #self.help_btn.grid(row = 8, column = 9)#pack(side = RIGHT)

    def bothelp(self):
        self.messagebox.showinfo("Help", "Enter your login details to access the To Do List") # if the user clicks on help this messagebox will appear 

    def botSearch(self):
        pass


root = Tk()
name_input = StringVar()


Terry = TwitterBot(root)
root.mainloop()
