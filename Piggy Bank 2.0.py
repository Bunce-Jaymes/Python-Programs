#This program will count your change
#Piggy Bank 2.0

from tkinter import *

def total(*args):
    
    output.delete(0.0, "end")
    try:
        pen= entpen.get()
        nic= entnic.get()
        dim= entdim.get()
        qua= entqua.get()
        dol= entdol.get()
        one= entone.get()
        
        pen= int(pen)
        nic= int(nic)
        dim= int(dim)
        qua= int(qua)
        dol= int(dol)
        one= int(one)

        pen= pen*0.01
        nic= nic*0.05
        dim= dim*0.1
        qua= qua*0.25
        dol= dol*0.5
        one= one*1

        total= pen + nic + dim + qua + dol + one

        output.insert(0.0, "You have, ${0:0.2f}".format(total))

        entpen.delete(0, END)
        entnic.delete(0, END)
        entdim.delete(0, END)
        entqua.delete(0, END)
        entdol.delete(0, END)
        entone.delete(0, END)

        entpen.insert(0, 0)
        entnic.insert(0, 0)
        entdim.insert(0, 0)
        entqua.insert(0, 0)
        entdol.insert(0, 0)
        entone.insert(0, 0)
        
    except:
        output.insert(0.0, "Sorry ALL boxes must have numbers")

#Root    
root= Tk()
root.wm_title("Piggy Bank")
root.config(bg="#5CEBFF")

#Top Frame
topframe= Frame (root, width=450, height=400)
intro= Label (topframe, text="Enter number of coins:")
output= Text (topframe, width=35, heigh=1)
#Labels for coins
textone= Label (topframe, text="One Dollars")
textdol= Label (topframe, text="Half Dollars")
textqua= Label (topframe, text="Quaters")
textdim= Label (topframe, text="Dimes")
textnic= Label (topframe, text="Nickles")
textpen= Label (topframe, text="Pennies")
#Input for coins
entone= Entry (topframe, width=5)
entdol= Entry (topframe, width=5)
entqua= Entry (topframe, width=5)
entdim= Entry (topframe, width=5)
entnic= Entry (topframe, width=5)
entpen= Entry (topframe, width=5)
#Button
show= Button (topframe, text="Show", command=total)

#Grid
topframe.grid (row=0, column=0, padx=10, pady=10)
intro.grid (row=0, column=1, pady=5)
output.grid (row=6, column=1, pady=10)
show.grid (row=5, column=1, pady=10)
#Grids for coins
textone.grid (row=3, column=2, pady=5)
textdol.grid (row=3, column=1, pady=5)
textqua.grid (row=3, column=0, pady=5)
textdim.grid (row=1, column=2, pady=5)
textnic.grid (row=1, column=1, pady=5)
textpen.grid (row=1, column=0, pady=5)

#Input Grid
entone.grid (row=4, column=2, pady=5)
entdol.grid (row=4, column=1, pady=5)
entqua.grid (row=4, column=0, pady=5)
entdim.grid (row=2, column=2, pady=5)
entnic.grid (row=2, column=1, pady=5)
entpen.grid (row=2, column=0, pady=5)

#Zeros
entpen.insert(0, 0)
entnic.insert(0, 0)
entdim.insert(0, 0)
entqua.insert(0, 0)
entdol.insert(0, 0)
entone.insert(0, 0)

#Config
topframe.config (bg="grey")
entpen.focus()
root.bind("<Return>", total)

try:
    image= PhotoImage (file="coin.gif")
    Label (topframe, image= image).grid (row=7, column=1)

except:
    print ()

root.mainloop()
