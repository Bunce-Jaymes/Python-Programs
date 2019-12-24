#This practice program will show us a few objects to use when creating a GUI

from time import *
from tkinter import *

def main():
    newtext.insert(0.0, "I clicked a button \n")
    #print (userInput.get(), "I just clicked a button")
    
root= Tk() #Makes the window
root.wm_title("Window Title") #Makes the title that will appear in the top left corner of the window
root.config (background= "#123456")#Color

leftframe= Frame (root, width= 200, height= 600) #Window in a window
leftframe.config (background= "#987654")
leftframe.grid (row=0, column=0, padx=10, pady=2)#Format settings

#logo= PhotoImage (file="image.jpg")
firstlabel= Label (leftframe, text="This is my first label")
firstlabel.grid (row=5, column=10, padx=10, pady=2)

secondlabel= Label (leftframe, text=":-)")
secondlabel.grid (row=13, column=4, padx=10, pady=2)

thirdlabel= Label (leftframe, text="Justin sucks!")
thirdlabel.grid (row=1, column=1, padx=10, pady=2)

userInput= Entry (leftframe, width=10)#Width refers to the number of charactors
userInput.grid (row=0, column=0, padx=10, pady=2)
userInput.get()#Stores the info they type in

newbutton= Button(leftframe, text="Okay", command=main)
newbutton.grid (row=1, column=0, padx=10, pady=2)

newcanvas= Canvas (leftframe, width=100, height=100, bg="red")
newcanvas.grid (row=3, column=3, padx=10, pady=2)

newtext= Text (leftframe, width=50, height=10, takefocus=0)#Take focus moves the cusor
newtext.grid (row=2, column=2, padx=10, pady=2)
newtext.insert (0.0, "Please type out the meaning of life here: ")

root.mainloop() #Start monitoring and updating the GUI
