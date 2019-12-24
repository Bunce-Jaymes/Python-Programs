#This Program will show us how to use radio buttons

from tkinter import *

def selection():
    whatsel= "You selected the option "+str(var.get())
    label.config (text=whatsel)

root= Tk()
root.wm_title("Radio Buttons")
root.config (bg="blue")
root.geometry ("200x200")

#Radio Buttons
var= IntVar()
r1= Radiobutton (root, text="Option 1", variable= var, value=1, command=selection)
r1.grid (row=0, column=0, pady=5)

r2= Radiobutton (root, text="Option 2", variable= var, value=2, command= selection)
r2.grid (row=1, column=0, pady=5)

r3= Radiobutton (root, text="Option 3", variable= var, value=3, command= selection)
r3.grid (row=2, column=0, pady=5)

label= Label (root, text="You have nothing selected")
label.grid (row=3, column=0, pady=5)














root.mainloop()
