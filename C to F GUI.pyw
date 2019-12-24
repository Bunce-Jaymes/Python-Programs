#C to F conveter GUI

from tkinter import *

#Defs
def CeltoFah():
    try:
        output.delete(0.0, "end") #Clears the output box
        cel= enterdegree.get()
        cel= int(cel)
        f= (9/5*cel+32)
        f= int(f)
        round (f,1)
        f= str(f)
        output.insert(0.0, f+" degrees Fahrenheit")
        enterdegree.delete(0, END)
    except:
        cel= enterdegree.get()
        if cel != int:
         output.insert(0.0, "Sorry please type a number")
        enterdegree.delete(0, END)

def FahtoCel():
    try:
        output.delete(0.0, "end") #Clears the output box
        fah= enterdegree.get()
        fah= int(fah)
        c= ((-32+fah)*5/9)
        c= int(c)
        round (c,1)
        c= str(c)
        output.insert(0.0, c+" degrees Celesius")
        enterdegree.delete(0, END)
    except:
        fah= enterdegree.get()
        if fah != int:
         output.insert(0.0, "Sorry please type a number")
        enterdegree.delete(0, END)

#Window
root= Tk()
root.wm_title("Celesius/Fahrenheit Conveter")
root.config (bg="#5CEBFF")

#Frames
mainframe= Frame (root, width=350, height=300)
inputlab= Label (mainframe, text="Number of Degrees:")
enterdegree= Entry (mainframe, width="5", takefocus=0)
output= Text (mainframe, width=30, height=1)

#Buttons
CtoF= Button (mainframe, text="Celesius to Fahrenheit", command=CeltoFah)
FtoC= Button (mainframe, text="Fahrenheit to Celesius", command=FahtoCel)

#Griding
mainframe.grid (row=0, column=0, padx=10, pady=10)
inputlab.grid (row=0, column=0, padx=5, pady=5)
enterdegree.grid (row=1, column=0, pady=5)
output.grid (row=4, column=0, padx=5, pady=5)
CtoF.grid (row=2, column=0, pady=5)
FtoC.grid (row=3, column=0, pady=5)

#Config
mainframe.config (bg="#B8FFCB")
CtoF.config (bg="#CBE8CD")
FtoC.config (bg="#CBE8CD")
inputlab.config (bg="#A7E8D0")
enterdegree.focus() #important!

root.mainloop()
