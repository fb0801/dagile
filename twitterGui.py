'''twitter bot gui version'''

#modules to use
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import re
from bs4 import BeautifulSoup
import requests
import json
import os
import random
import time

OPTIONS = [
"Jan",
"Feb",
"Mar"
] 



class TwitterBot:
    def __init__(self, master):
        self = master
        tk.Frame(self.master) # a frame to contain everything in
        
        master.title('Twitter Bot')
        
        self.help_btn = tk.Button(self, text = '?',font = 'Times 20 ',width = 1, height = 1, command = TwitterBot.bothelp)
        self.help_btn.pack(side = RIGHT )#grid(row = 1, column = 9)

        self.user_input = tk.Entry(textvariable = name_input)
        self.user_input.pack()

        variable = StringVar(master)
        variable.set(OPTIONS[0]) # default value

        w = OptionMenu(master, variable, *OPTIONS)
        w.pack()

        self.button_quit =tk.Button(self, text="Exit", command=master.destroy)
        self.button_quit.pack()
        
        

        self.submit_btn =tk.Button(self, text="Submit", command = TwitterBot.botSearch)
        self.submit_btn.pack()

    def bothelp():
        messagebox.showinfo("Help", "Enter the duration") # if the user clicks on help this messagebox will appear 

    def botSearch():
        dur = name_input.get()
        measure = Variable.get()
        if isinstance(dur, int) == True:
            print (dur)
            print(measure)
            
            while dur:
                mins, secs = divmod(dur, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(timer, end="\r")
                time.sleep(1)
                dur -= 1
            print('Fire in the hole!!')
        elif isinstance(dur, int) == False:
            print("Error")
        else: 
            print("Unknown")
        
        #while dur:
        #    mins, secs = divmod(dur, 60)
        #    timer = '{:02d}:{:02d}'.format(mins, secs)
        #    print(timer, end="\r")
        #    time.sleep(1)
        #    dur -= 1
        #print('Fire in the hole!!')




root = tk.Tk()
name_input = IntVar()


Terry = TwitterBot(root)
root.geometry("300x300")
root.mainloop()