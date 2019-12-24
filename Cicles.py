#This Program will better at GUI and have a interactive window

from tkinter import *
from time import *

def redCircle():
    circlecanvas.create_oval(20,20,80,80, width=0, fill="red")
    colorLog.insert(0.0, "Red Circle\n")

def blueCircle():
    circlecanvas.create_oval(20,20,80,80, width=0, fill="blue")
    colorLog.insert(0.0, "Blue Circle\n")

def orangeCircle():
    circlecanvas.create_rectangle(20,20,80,80, width=0, fill="orange")
    colorLog.insert(0.0, "Orange Rectangle\n")

def greenCircle():
    circlecanvas.create_rectangle(20,20,80,80, width=0, fill="green")
    colorLog.insert(0.0, "Green Rectangle\n")

def yellowCircle():
    circlecanvas.create_polygon(50,70,55,55,70,50,55,45,50,30,45,45,30,50,45,55, width=0, fill="yellow")
    colorLog.insert(0.0, "Yellow Star\n")

def purpleCircle():
    circlecanvas.create_polygon(50,70,55,55,70,50,55,45,50,30,45,45,30,50,45,55, width=0, fill="purple")
    colorLog.insert(0.0, "Purple Star\n")

#Left Frame Content

root= Tk() #Creates the window
root.wm_title ("Circles")
root.config (background= "black")

leftFrame= Frame (root, width= 200, height= 600)
leftFrame.config (background= "blue") 
leftFrame.grid (row=0, column=0, padx=10, pady=2)

instructions= Label (leftFrame, text="Instructions").grid (row=0, column=0, padx=10, pady=2)

instructionSteps= Label (leftFrame, text="1\n2\n3\n4\n5\n6\n7\n8\n9\n")
instructionSteps.grid (row=1, column=0, padx=10, pady=2)

try:
    GIFimage= PhotoImage (file= "link.gif")
    Label (leftFrame, image=GIFimage).grid (row=2, column=0)

except:
    print ("Sorry there is an error, ducks are taking over")

#Right Frame Content

rightframe= Frame (root, width= 200, height= 600)
rightframe.config (background= "red")
rightframe.grid(row=0, column=1, padx=10, pady=2)

circlecanvas= Canvas (rightframe, width=100, height=100, bg="white")
circlecanvas.grid (row=0, column=0, padx=10, pady=2)

#Button Frame

btnframe= Frame (rightframe, width=200, height=200)
btnframe.config (bg= "grey")
btnframe.grid (row=1, column=0, padx=10, pady=2)

#Color Log
colorLog= Text (rightframe,width=30, height=10,takefocus=0)
colorLog.grid (row=2, column=0, padx=10, pady=2)

#Color Buttons
redbtn= Button (btnframe, text="Red", command=redCircle)
redbtn.grid (row=3, column=0, padx=10, pady=2)

bluebtn= Button (btnframe, text="Blue", command=blueCircle)
bluebtn.grid (row=3, column=1, padx=10, pady=2)

orangebtn= Button (btnframe, text="Orange", command=orangeCircle)
orangebtn.grid (row=3, column=2, padx=10, pady=2)

greenbtn= Button (btnframe, text="Green", command=greenCircle)
greenbtn.grid (row=4, column=0, padx=10, pady=2)

yellowbtn= Button (btnframe, text="Yellow", command=yellowCircle)
yellowbtn.grid (row=4, column=1, padx=10, pady=2)

purplebtn= Button (btnframe, text="Purple", command=purpleCircle)
purplebtn.grid (row=4, column=2, padx=10, pady=2)

#Loop for the window
root.mainloop()
