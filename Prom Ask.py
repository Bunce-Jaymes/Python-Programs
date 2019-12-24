#This program will ask the user their gender, prac with checkboxes

from tkinter import *

def var_states():
    sex= var.get()
    if sex == 1:
        whatsex= "Hey man wanna go to prom with me?"
        label.config (text=whatsex)
    if sex == 2:
        whatsex= "Hey girl wanna go to prom with me?"
        label.config (text=whatsex)

root=Tk()
root.wm_title("Checkboxes")
root.geometry ("300x300")
root.config (bg="blue")

Label (root, text="Gender: ").grid (row=0, sticky=W)

#Checkbutton #1
var= IntVar()
Radiobutton (root, text="Male", variable= var, value=1).grid (row=1, sticky=W)

#Checkbutton #2
Radiobutton (root, text="Female", variable= var, value=2).grid (row=2, sticky=W)

Button (root, text="Quit", command= root.destroy).grid (row=3, sticky=W)
Button (root, text="Show", command= var_states).grid (row=3, column=1)

label= Label (root, text="You have nothing selected")
label.grid (row=4, column=0, pady=5)








root.mainloop()
