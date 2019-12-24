#Piggy Bank 1.0

import time

print ("Hello welcome to Piggy Bank 1.0!")
print()
name= input("Hello what is your name?")
print ()


def main():
    print ("Hi,"+name+" nice to meet you!")
    print ()
    
    pennies= eval(input("How many pennies do you have: "))
    print ()
    pennies= pennies*.01
    #round (pennies,2)

    nickles= eval(input ("How many nickles do you have: "))
    print ()
    nickles= nickles*.05
    #round (nickles,2)

    dimes= eval(input("How many dimes do you have: "))
    print ()
    dimes= dimes*.1
    #round (dimes,2)

    quarters= eval(input("How many quarters do you have: "))
    print ()
    quarters= quarters*.25
    #round (quarters,2)

    oneDollar= eval(input("How many one dollar bills do you have: "))
    print ()
    oneDollar= oneDollar*1
    #round (oneDollar,2)

    fiveDollar= eval(input("How many five dollar bills do you have: "))
    print ()
    fiveDollar= fiveDollar*5
    #round (fiveDollar,2)

    tenDollar= eval(input("How many ten dollar bills do you have: "))
    print ()
    tenDollar= tenDollar*10
    #round (tenDollar,2)

    twentyDollar= eval(input("How many twenty dollar bills do you have: "))
    print ()
    twentyDollar= twentyDollar*20
    #round (twentyDollar,2)

    fiftyDollar= eval(input("How many fifty dollar bills do you have: "))
    print ()
    fiftyDollar= fiftyDollar*50
    #round (fiftyDollar,2)

    hundredDollar= eval(input("How many hundred dollar bills do you have: "))
    print ()
    hundredDollar= hundredDollar*100
    #round (hundredDollar,2)

    total=(pennies + nickles + dimes + quarters + oneDollar + fiveDollar + tenDollar + twentyDollar + fiftyDollar +hundredDollar)    

    print ("You have,${0:0.2f} {1}".format(total,name))
    print ()
    print ("--------------------------------------------------")
    again()

def again():
    again= input("Would you like to count again? (yes or no)")
    print ()
    print ("--------------------------------------------------")
    time.sleep (2)

    if again== "yes" or again== "y":
        main()

main()
