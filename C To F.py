#This program converts C to F

import time
Again= "yes"

def main():

    print ("What would you like me to convert to?")
    time.sleep (1)
    print ("Type 1 to convert from Celesis to Fahrenheit.")
    time.sleep (1)
    time.sleep (1)
    print ("Type 2 to convert from Fahrenheit to Celsius.")
    print ()
    convert= eval(input())


    if convert == 1:
            C2F()
    if convert == 2:
            F2C()

def C2F():
    time.sleep (1)
    cel= input("Okay, how many degrees Celsius?")
    cel= int(cel)
    time.sleep (1)
    print ("Okay one second...")
    f= (9/5*cel+32)
    round (f,1)
    print ("It's ",f," degrees Fahrenheit.")
    print ()
    time.sleep (1)
    again= input ("Would you like to convert again? Type yes.")
    print ()

    if again == "yes":
        main()

    if again != "yes":
        quit()

    
    

def F2C():
    time.sleep (1)
    fah= input("Okay, how many degrees Fahrenheit?")
    fah= int(fah)
    time.sleep (1)
    print ("Okay, one second...")
    c= ((-32+fah)*5/9)
    c= int(c)
    round (c,1)
    time.sleep (1)
    print ("It's ",c," degrees Celsius.")
    print ()
    again= input ("Would you like to convert again? Type yes.")
    print ()

    if again == "yes":
        main()

    if again != "yes":
        quit()

    
