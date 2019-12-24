#Chores Program

import time

def main():
    print ("Hi would you like to view your chores that")
    print ("you need to complete today? (yes or no)")
    print ()
    viewList= input()
    print ()
    print ("---------------------------------------------------")

    if viewList == "y" or viewList == "yes":
        choreList()
    if viewList == "n" or viewList == "no":
        time.sleep(2)
        quit()
    else:
        print ("Good job smart ass...")
        time.sleep(5)
        quit()


def choreList():
    choreList= []

    while True:
        print ("Here are the chores you need to do:")
        print (*choreList, sep=", ")
        print ()

        print ("Would you like to add or remove to the list? (add or remove)")
        print ()
        addList= input()
        print ("---------------------------------------------------")
    
        if addList== "add":
            print ("Please type the chore you would like to add:")
            newChore= input()

            choreList.append(newChore)

            print ("Okay I will add, "+newChore+" ,to the list.")
            print ()
            print ("---------------------------------------------------")

        if addList == "remove":
            print ("Here are the chores you need to do:")
            print (*choreList, sep=", ")
            print ()
            print ("Which chore would you like to remove?")
            print ()
            removeList= input()
            print ("---------------------------------------------------")

            choreList.remove(removeList)
    
main()
#print (*choreList, sep=" , ")
