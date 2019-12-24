#This program will read data from a file and print it out in python

import time

def main():
    """This function will retreive a file depending on name and print the data"""

    filename= input("Please enter name of file: ")
    print ()

#if filename!= "laundry.txt" or filename != "chores.txt":
    #print ("Sorry there are no files with that name")
    #print ()
        
#else:
    filein= open (filename, "r+")
    data= filein.read()
    print (data)
    print ()

    while True:
        choice= input("Type (1) to Add \n Type (2) to Delete \n Type (3) to Exit")

        if choice == "1":
            addChores= input("Type the chore you would like to add: ")
            print ()
            filein.write(", "+addChores)
                
            filein= open (filename, "r+")
            data= filein.read()
            print (data)
            print ()
                    
        elif choice == "2":
            delChores=input("Chore to delete: ")
            newdata = data.replace(delChores,"")
            filein = open(filename,'w')
            filein.write(newdata)
            filein = open(filename, "r+")
            data = filein.read()
            print(data)

        elif choice != "1" and choice != "2" and choice != "3":
            print ("Why u no listen!!!!!")
            print ()

        else:
            print ("Thanks for using the program")
            print ()
            filein.close()
            break
                       

    
while True:
    main()
