#This program will help John with his math test
#The user will type two numbers to be +,-,*,/

#We will learn and apply the skill of combining variables.

import time

def main():
    print ("This program will calculate 2 numbers depending on the operator.")
    print ()
    print ("---------------------------------------------------------------")
    print ("Type 1, for addition.")
    print ()
    print ("Type 2, for subtraction.")
    print ()
    print ("Type 3, for multiplication.")
    print ()
    print ("Type 4, for divison.")
    print ()
    print ("Type 5, for slope intercept.")
    print ()

    operator= input("Please type whichever operator you would like to use:")
    operator= int(operator)
    print ()
    print ("---------------------------------------------------------------")

    if operator == 1:
        add()
    if operator == 2:
        sub()
    if operator == 3:
        mul()
    if operator == 4:
        div()
    if operator == 5:
        slope()
    

def add():
    add1, add2=  eval(input("Enter two numbers to be calculated, sperate the numbers with a comma:"))
    addanswer= add1 + add2
    print ("Your answer to this test question is: ",addanswer)
    print ()
    print ("---------------------------------------------------------------")
    startagain= input("Would you like to add again? Type y or n.")
    print ()
    print ("---------------------------------------------------------------")

    if startagain== "y":
        add()
    elif startagain== "n":
        main()
    elif startagain != "y" or startagain != "no":
        print ("Sorry people who don't follow directions, don't succeed in life.")

    

def sub():
    sub1, sub2=  eval(input("Enter two numbers to be calculated, sperate the numbers with a comma:"))
    subanswer= sub1 - sub2
    print ("Your answer to this test question is: ",subanswer)
    print ()
    print ("---------------------------------------------------------------")
    startagain= input("Would you like to add again? Type y or n.")
    print ()
    print ("---------------------------------------------------------------")

    if startagain== "y":
        add()
    if startagain== "n":
        main()
    if startagain != "y" or startagain != "no":
        print ("Sorry people who don't follow directions, don't succeed in life.")
    

def mul():
    mul1, mul2=  eval(input("Enter two numbers to be calculated, sperate the numbers with a comma:"))
    mulanswer= mul1 * mul2
    print ("Your answer to this test question is: ",mulanswer)
    print ()
    print ("---------------------------------------------------------------")
    startagain= input("Would you like to add again? Type y or n.")
    print ()
    print ("---------------------------------------------------------------")

    if startagain== "y":
        add()
    if startagain== "n":
        main()
    if startagain != "y" or startagain != "no":
        print ("Sorry people who don't follow directions, don't succeed in life.")

def div():
    div1, div2=  eval(input("Enter two numbers to be calculated, sperate the numbers with a comma:"))
    divanswer= div1 / div2
    print ("Your answer to this test question is: ",divanswer)
    print ()
    print ("---------------------------------------------------------------")
    startagain= input("Would you like to add again? Type y or n.")
    print ()
    print ("---------------------------------------------------------------")

    if startagain== "y":
        add()
    if startagain== "n":
        main()
    if startagain != "y" or startagain != "no":
        print ("Sorry people who don't follow directions, don't succeed in life.")


def slope():
    slope, slopeint= eval(input("Enter the slope and slope intercept as positive numbers and, seprate the numbers with a comma:"))
    print ()
    
    slope= str(slope)
    slopeint= str(slopeint)
    negative=  eval(input("Is your slope intercept a negative number? Type y or n."))

    if negative == "y":
        slopeform= "y="+slope+"x-"+slopeint
        slopeform= str(slopeform)

        print ("The slope form with these numbers is, "+slopeform)
        print ()

        print ("---------------------------------------------------------------")
        startagain= input("Would you like to add again? Type y or n.")
        print ()
        print ("---------------------------------------------------------------")

        if startagain== "y":
            add()
        if startagain== "n":
            main()
        if startagain != "y" or startagain != "no":
            print ("Sorry people who don't follow directions, don't succeed in life.")

    if negative != "y":
        slopeform= "y="+slope+"x+"+slopeint
        slopeform= str(slopeform)

        print ("The slope form with these numbers is, "+slopeform)
        print ()

        print ("---------------------------------------------------------------")
        startagain= input("Would you like to add again? Type y or n.")
        print ()
        print ("---------------------------------------------------------------")

        if startagain== "y":
            add()
        if startagain== "n":
            main()
        if startagain != "y" or startagain != "no":
            print ("Sorry people who don't follow directions, don't succeed in life.")


main()

