#This program will retrieve and interact with inputs (entry)

from tkinter import *

def welcome():
    name=entername.get()
    welcomewin.insert (0.0, "Welcome to my program: "+name+"\n")

root= Tk()
root.wm_title("Hello World")
root.config (bg= "black")

#Interface GUI ALL widgets

topframe= Frame (root, width=250, height=200)
topframe.grid  (row=0, column=0, pady=2)
bottomframe= Frame (root, width=250, height=100)
bottomframe.grid (row=2, column=0, pady=5)

name= Label (topframe, text="Hello what is your name?")

entername= Entry (topframe, width="15")
entername.config (bg="green")

wbtn= Button (topframe, text="Welcome Me!", command=welcome)
wbtn.config (bg="red")

welcomewin= Text (bottomframe, width=40, height=5)
welcomewin.config (bg="grey")

#Packing/Griding
name.grid (row=0, column=0, padx=5, pady=2)
entername.grid (row=1, column=0, padx=2)
wbtn.grid (row=2, column=0)
welcomewin.grid (row=0, column=0)

root.mainloop()
