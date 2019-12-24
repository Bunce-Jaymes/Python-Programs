# This program is two truths and one lie game. Made by Jaymes Bunce
#String: Text that can be placed in a variable
#Function: A repeatable code/task (print, and input. Built in functions)
#Operator: +,-,*,/. Symbols that connect strings

import time

def main():
    print("Hey, my name is Jaymes, what is your name?")
    name= input ()
    print ("Hello, " + name + " nice to meet you")

    while True:
        print ("Here are my statements:")
        time.sleep (1)
        print ("1. I broke my big toe in a pillow fight.")
        time.sleep (1)
        print ("2. I have a dog that has white feet.")
        time.sleep (1)
        print ("3. Some of my favorite games include Halo, COD, BF4, and Robocraft.")
        time.sleep (1)

        print ("Which do you think is the lie? Type 1, 2, or 3.")
        guess= input ()
        guess= int(guess)
        
        if guess == 1:
            time.sleep (1)
            print ("That is correct, I have never broken my toe before! Thanks for playing!")
            break

        if guess == 2:
            time.sleep (1)
            print ("That is incorrect, My dog has white feet.")
            print ("Try again")
            
        if guess == 3:
            time.sleep (1)
            print (" That is incorrect, I love to play all of those games!")
            print ("Try again")
                   


    
