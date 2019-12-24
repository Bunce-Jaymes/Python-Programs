#This program will keep track of your usernames and passwords
#1.1v

from tkinter import *
import tkinter.scrolledtext as tkst
import uuid
import os, sys
import win32print
import time

def show(*args):
    accountfile= open("account.txt", "a+")
    passfile= open("pass.txt", "a+")
    accountData= accountfile.read().split(",")
    passData= passfile.read().split(",")

    accountfile= open("account.txt", "r+")
    passfile= open("pass.txt", "r+")
    accountData= accountfile.read().split(",")
    passData= passfile.read().split(",")

    printfile= open("print.txt", "a+")
    printData= printfile.read().split(",")
    printfile= open("print.txt", "r+")
    printData= printfile.read().split(",")
    
    win= Tk()
    win.wm_title("Info")
    win.config(bg="grey")
    win.iconbitmap("favicon.ico")

    main= Frame (win, width=450, height=400)
    main.grid (row=0, column=0, padx=10, pady=10)
    main.config(bg="#6889B2")

    output= tkst.ScrolledText (master= main, wrap= "word", width= 35, height= 20, bg= "white")
    output.grid (row=0, column=0, padx=10, pady=10)

    output.insert(0.0, "Account, Password\n__________________\n")

    for line in zip(accountData, passData):
        output.insert(END, "{} {:20}\n".format(*line))

    info= output.get("0.0", END)

    printfile= open("print.txt", "w")
    printfile.write(info)
    printfile.close()
    
    Button (main, text="Print", command= printstuff).grid(row=1, column=0, padx=10, pady=10)
    
    win.mainloop()   

def add():
    name= nameent.get()
    password= passent.get()

    if name and password != "":
        nameent.delete(0, END)
        passent.delete(0, END)
        
        accountfile= open("account.txt", "a+")
        accountfile.write(" , "+name)
        accountfile.read().split(",")
        accountfile.close()
                        
        passfile= open("pass.txt", "a+")    
        passfile.write(" , "+password)
        passfile.read().split(",")
        passfile.close()

        win= Tk()
        win.wm_title("Confirm")
        win.config(bg="grey")
        win.iconbitmap("favicon.ico")

        main= Frame (win, width=450, height=400)
        main.grid (row=0, column=0, padx=10, pady=10)
        main.config(bg="#6889B2")

        aboutinfo= Label (main, text="Password Added!")
        aboutinfo.grid (row=0, column=0, padx=10, pady=10)

        Button (main, text="Okay", command=win.destroy).grid (row=1, column=0, padx=10, pady=10)
        
        win.mainloop()

    if name or password == "":
        win= Tk()
        win.wm_title("Error")
        win.config(bg="grey")

        main= Frame (win, width=450, height=400)
        main.grid (row=0, column=0, padx=10, pady=10)
        main.config(bg="#6889B2")
        win.iconbitmap("favicon.ico")

        aboutinfo= Label (main, text="Make sure your boxes are correct,\nBoxes can not be blank!")
        aboutinfo.grid (row=0, column=0, padx=10, pady=10)

        Button (main, text="Okay", command=win.destroy).grid (row=1, column=0, padx=10, pady=10)
        
        win.mainloop()
        
    else:
        win= Tk()
        win.wm_title("Error")
        win.config(bg="grey")
    
        main= Frame (win, width=450, height=400)
        main.grid (row=0, column=0, padx=10, pady=10)
        main.config(bg="#6889B2")
        win.iconbitmap("favicon.ico")

        aboutinfo= Label (main, text="Make sure your boxes are correct,\nBoxes can not be blank!")
        aboutinfo.grid (row=0, column=0, padx=10, pady=10)

        Button (main, text="Okay", command=win.destroy).grid (row=1, column=0, padx=10, pady=10)
        
        win.mainloop()
 
def remove():
        name= nameent.get()
        password= passent.get()
        
        if name and password != "":
            nameent.delete(0, END)
            passent.delete(0, END)

            passfile= open("pass.txt", "r+")
            data= passfile.read()
            newdata= data.replace(password, "")
            passfile= open("pass.txt", "w")
            passfile.write(newdata)
            passfile.close()

            accountfile= open("account.txt", "r+")
            data= accountfile.read()
            newdata= data.replace(name, "")
            accountfile= open("account.txt", "w")
            accountfile.write(newdata)
            accountfile.close()

            win= Tk()
            win.wm_title("Confirm")
            win.config(bg="grey")

            main= Frame (win, width=450, height=400)
            main.grid (row=0, column=0, padx=10, pady=10)
            main.config(bg="#6889B2")
            win.iconbitmap("favicon.ico")

            aboutinfo= Label (main, text="Password Removed!")
            aboutinfo.grid (row=0, column=0, padx=10, pady=10)

            Button (main, text="Okay", command=win.destroy).grid (row=1, column=0, padx=10, pady=10)
            
            win.mainloop()
            
        if name or password == "":
            win= Tk()
            win.wm_title("Error")
            win.config(bg="grey")

            main= Frame (win, width=450, height=400)
            main.grid (row=0, column=0, padx=10, pady=10)
            main.config(bg="#6889B2")
            win.iconbitmap("favicon.ico")

            aboutinfo= Label (main, text="Make sure your boxes are correct,\nBoxes can not be blank!")
            aboutinfo.grid (row=0, column=0, padx=10, pady=10)

            Button (main, text="Okay", command=win.destroy).grid (row=1, column=0, padx=10, pady=10)
            
            win.mainloop()
            
        else:
            win= Tk()
            win.wm_title("Error")
            win.config(bg="grey")

            main= Frame (win, width=450, height=400)
            main.grid (row=0, column=0, padx=10, pady=10)
            main.config(bg="#6889B2")
            win.iconbitmap("favicon.ico")

            aboutinfo= Label (main, text="Make sure your boxes are correct,\nBoxes can not be blank!")
            aboutinfo.grid (row=0, column=0, padx=10, pady=10)

            Button (main, text="Okay", command=win.destroy).grid (row=1, column=0, padx=10, pady=10)
            
            win.mainloop()

def random():
    password=(uuid.uuid1())
    
    win= Tk()
    win.wm_title("Random Password")
    win.config(bg="grey")

    main= Frame (win, width=450, height=400)
    main.grid (row=0, column=0, padx=10, pady=10)
    main.config(bg="#6889B2")
    win.iconbitmap("favicon.ico")

    aboutinfo= Text (main, width=36, height=1)
    aboutinfo.grid (row=0, column=0, padx=10, pady=10)
    
    aboutinfo.insert (0.0, password)

    Button (win, text="Okay", command=win.destroy).grid (row=1, column=0, padx=10, pady=10)
    
    win.mainloop()

def helpme():
    win= Tk()
    win.wm_title("Help")
    win.config(bg="grey")

    main= Frame (win, width=450, height=400)
    main.grid (row=0, column=0, padx=10, pady=10)
    main.config(bg="#6889B2")
    win.iconbitmap("favicon.ico")

    aboutinfo= Label (main, text="If you want to add or remove a password,\nsimply fill out the information and\nclick Add Password or Remove Password\n\nShow Accounts will show you all\npasswords you have saved\n\nRandom Password will create a\nrandom password\n\nHelp brings you to this screen\n\nAbout tells you about the program")
    aboutinfo.grid (row=0, column=0, padx=10, pady=10)
    
    win.mainloop()

def about():
    win= Tk()
    win.wm_title("About")
    win.config(bg="grey")

    main= Frame (win, width=450, height=400)
    main.grid (row=0, column=0, padx=10, pady=10)
    main.config(bg="#6889B2")
    win.iconbitmap("favicon.ico")

    aboutinfo= Label (main, text="Created by: Jaymes Bunce\njaymesbunce@gmail.com\n\nThank You for using my program!\nYou are using version: 1.0\nMake sure to check for updates!")
    aboutinfo.grid (row=0, column=0, padx=10, pady=10)
    
    win.mainloop()

def printstuff():
    try:
        printer_name = win32print.GetDefaultPrinter ()

        if sys.version_info >= (3,):
          raw_data = bytes ("This is a test", "utf-8")
        else:
          raw_data = "printfile.txt"

        hPrinter = win32print.OpenPrinter (printer_name)

        try:
          hJob = win32print.StartDocPrinter (hPrinter, 1, ("printfile.txt", None, "RAW"))

          try:
            win32print.StartPagePrinter (hPrinter)
            win32print.WritePrinter (hPrinter, raw_data)
            win32print.EndPagePrinter (hPrinter)

          finally:
            win32print.EndDocPrinter (hPrinter)

        finally:
          win32print.ClosePrinter (hPrinter)

        win= Tk()
        win.wm_title("Printing")
        win.config(bg="grey")

        main= Frame (win, width=450, height=400)
        main.grid (row=0, column=0, padx=10, pady=10)
        main.config(bg="#6889B2")
        win.iconbitmap("favicon.ico")

        aboutinfo= Label (main,text="Okay now printing your passwords to your\ndefault printer")
        aboutinfo.grid (row=0, column=0, padx=10, pady=10)

        Button (win, text="Okay", command=win.destroy).grid (row=1, column=0, padx=10, pady=10)
        
        win.mainloop()
        
    except:
        win= Tk()
        win.wm_title("Printing Error")
        win.config(bg="grey")

        main= Frame (win, width=450, height=400)
        main.grid (row=0, column=0, padx=10, pady=10)
        main.config(bg="#6889B2")
        win.iconbitmap("favicon.ico")

        aboutinfo= Label (main,text="Sorry an error occured\nwhile printing, please check your printer")
        aboutinfo.grid (row=0, column=0, padx=10, pady=10)

        Button (win, text="Okay", command=win.destroy).grid (row=1, column=0, padx=10, pady=10)
        
        win.mainloop()
        
#Root
root= Tk()
root.wm_title("Password Manager")
root.config(bg="grey")
root.iconbitmap("favicon.ico")

#Topframe
topframe= Frame (root, width=450, height=400)
topframe.grid (row=0, column=0, padx=10, pady=10)
topframe.config(bg="#6889B2")

folder= Label (topframe, text="Make sure this program is in a folder!\nIt will make things easier!")
folder.grid (row=0, column=2, padx=10, pady=5)
folder.config(bg="#B20000")

#Topframe Buttons
showpass= Button (topframe, text="Show Accounts", command=show)
showpass.grid (row=1, column=2, padx=10, pady=5)

helpbtn= Button (topframe, text="Help", command=helpme)
helpbtn.grid (row=3, column=2, padx=10, pady=5)

about= Button (topframe, text="About", command=about)
about.grid (row=4, column=2, pady=10)

quitbtn= Button (topframe, text="Quit", command=root.destroy)
quitbtn.grid (row=5, column=2, pady=10)

#Add Password
addbtn= Button (topframe, text="Add Password", command=add)
addbtn.grid (row=0, column=1, padx=10, pady=5)

#Remove Pasword
remove= Button (topframe, text="Remove Password", command=remove)
remove.grid (row=1, column=1, padx=10, pady=5)

#Input
name= Label (topframe, text="Name:")
name.grid (row=2, column=1, padx=10, pady=5)

nameent= Entry (topframe, width="15")
nameent.grid (row=3, column=1, padx=10, pady=5)
nameent.focus()

password= Label (topframe, text="Password:")
password.grid (row=4, column=1, padx=10, pady=5)

passent= Entry (topframe, width="15")
passent.grid (row=5, column=1, padx=10, pady=5)

#Random Password
ranbtn= Button (topframe, text="Random Password:", command=random)
ranbtn.grid (row=2, column=2, padx=10, pady=5)

#Root Stuff
root.bind("<Escape>", exit)

root.bind("<Return>",show)

root.mainloop()







