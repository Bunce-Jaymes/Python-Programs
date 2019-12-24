#This program will ask the user their gender, prac with checkboxes

from tkinter import *

def var_states():
    female= var2.get()
    male= var1.get()
    if male == 1:
        print ("Hey man wanna go to prom?")
    elif female == 1:
        print ("Hey girl wanna go to prom?")
    if male != 1 and female != 1:
        print ("Sorry python encountered an error")

root=Tk()
root.wm_title("Checkboxes")
root.geometry ("200x200")
root.config (bg="blue")

Label (root, text="Gender: ").grid (row=0, sticky=W)

#Checkbutton #1
var1= IntVar()
Checkbutton (root, text="Male", variable= var1).grid (row=1, sticky=W)

#Checkbutton #2
var2= IntVar()
Checkbutton (root, text="Female", variable= var2).grid (row=2, sticky=W)

Button (root, text="Quit", command= root.destroy).grid (row=3, sticky=W)
Button (root, text="Show", command=var_states).grid (row=3, column=1)










root.mainloop()
