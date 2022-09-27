'''twitter bot gui version'''

#modules to use
from tkinter import *

root = Tk()
root.title('Twitter Bot')


button_quit =Button(root, text="Exit program", command=root.quit)
button_quit.pack()

root.mainloop()