# This is a guess the number game
# Introduce the person to the game, ask for name
# Ask if they want to play
# Random a number between 1 and 10
# Print I am thinking of a number between 1-10
# User Guesses
# Process the guess and decide if it's low, high, or just right
# Print results

#Due to a bug, it is required to start the game with main(), otherwise nothing will happen

import time
import random

myname= input ("Hello, What is your name?")
time.sleep (1)
print ()
print ("Welcome to the Guess the Number Game 1.0, "+myname)
time.sleep (1)
print ()
print ("------------------------------------------------------------------")

def main():
    print()
    levelselect= input("Would you like to select your starting level? Type yes or no.")
    print ()
    print ("------------------------------------------------------------------")

    if levelselect == "yes":
        levels()
    
    if levelselect != "yes":
        level1()

def levels():
    print ("Type easy, to play guessing numbers 1-10")
    print ()
    print ("Type medium, to play guessing numbers 1-50")
    print ()
    print ("Type hard, to play guessing numbers 1-100")
    print ()
    print ("Type extreme, to play guessing numbers 1-1000")
    print ()

    levelselect2= input("Which level would you like to start at?")
    print ()
    print ("------------------------------------------------------------------")

    if levelselect2 == "easy":
        level1()
    if levelselect2 == "medium":
        level2()
    if levelselect2 == "hard":
        level3()
    if levelselect2 == "extreme":
        level4()

def level1():
    print ("------------------------------------------------------------------")
    number= random.randint (1, 10)
    print ("I am thinking of a number between 1-10")
    print ()

    guesstaken= 0
    guessremaining= 5
    while guesstaken < 5:  
        print ("Take a guess")
        print ()
        print ("You have, ",guessremaining," guesses remaining.")
        print ()
        guess= input()
        guess= int(guess)
        guesstaken= guesstaken + 1
        guessremaining= guessremaining-1
        print ("------------------------------------------------------------------")

        if guess < number:
            print ("Your guess is too low")
            print()
            
            

        if guess > number:
            print ("Your guess is too high")
            print ()
            

        if guess == number:
            print ("------------------------------------------------------------------")
            break

    if guess == number:
        guesstaken= str(guesstaken)
        print ("Good job, "+myname+" ,you guessed the number in "+guesstaken+" guesses!")
        print ()

        time.sleep (1)
        playnext= input("Would you like to play the next level?")
        print ()
        if playnext == "yes" or playnext== "y" or playnext== "Yes":
            level2()
            
    if guess != number:
        number= str(number)
        print ("Nope! The number I was thinking of was, "+number)
        print ()
        playagain= input ("Would you like to play again?")
        print ()
        if playagain == "yes" or playagain== "y" or playagin== "Yes":
            print ("------------------------------------------------------------------")
            main()

def level2():
    print ("------------------------------------------------------------------")
    number= random.randint (1, 50)
    print ("I am thinking of a number between 1-50")
    print ()

    guesstaken= 0
    guessremaining= 6
    while guesstaken < 6:
        print ("Take a guess")
        print ()
        print ("You have, ",guessremaining," guesses remaining.")
        print ()
        guess= input()
        guess= int(guess)
        guesstaken= guesstaken + 1
        guessremaining= guessremaining-1
        print ("------------------------------------------------------------------")

        if guess < number:
            print ("Your guess is too low")
            print()
            
        if guess > number:
            print ("Your guess is too high")
            print ()
            
        if guess == number:
            print ("------------------------------------------------------------------")
            break

    if guess == number:
        guesstaken= str(guesstaken)
        print ("Good job, "+myname+" ,you guessed the number in "+guesstaken+" guesses!")
        print ()

        playnext= input("Would you like to play the next level?")
        print ()
        if playnext == "yes" or playnext== "y" or playnext== "Yes":
            level3()
            
    if guess != number:
        number= str(number)
        print ("Nope! The number I was thinking of was, "+number)
        print ()
        playagain= input ("Would you like to play again?")
        print ()
        if playagain == "yes" or playagain== "y" or playagain== "Yes":
            print ("------------------------------------------------------------------")
            main()

def level3():
    print ("------------------------------------------------------------------")
    number= random.randint (1, 100)
    print ("I am thinking of a number between 1-100")
    print ()

    guesstaken= 0
    guessremaining= 7
    while guesstaken < 7:
        print ("Take a guess")
        print ()
        print ("You have, ",guessremaining," guesses remaining.")
        print ()
        guess= input()
        guess= int(guess)
        guesstaken= guesstaken + 1
        guessremaining= guessremaining-1
        print ("------------------------------------------------------------------")

        if guess < number:
            print ("Your guess is too low")
            print()
            

        if guess > number:
            print ("Your guess is too high")
            print ()
            
        if guess == number:
            print ("------------------------------------------------------------------")
            break

    if guess == number:
        guesstaken= str(guesstaken)
        print ("Good job, "+myname+" ,you guessed the number in "+guesstaken+" guesses!")
        print ()
        playnext= input ("Would you like to play the next level? Warning it is super hard!")
        time.sleep (3)
        print ()
        if playnext == "yes" or playnext== "y" or playnext== "Yes":
            level4()
        
        
            
    if guess != number:
        number= str(number)
        print ("Nope! The number I was thinking of was, "+number)
        print ()
        playagain= input ("Would you like to play again?")
        print ()
        if playagain == "yes" or playagain== "y" or playagain== "Yes":
            print ("------------------------------------------------------------------")
            main()
        
def level4():
    print ("------------------------------------------------------------------")
    number= random.randint (1, 1000)
    print ("I am thinking of a number between 1-1000")
    print ()
    guesstaken= 0
    guessremaining= 9
    while guesstaken < 9:
        print ("Take a guess")
        print ()
        print ("You have, ",guessremaining," guesses remaining.")
        print ()
        guess= input()
        guess= int(guess)
        guesstaken= guesstaken + 1
        guessremaining= guessremaining-1
        print ("------------------------------------------------------------------")

        if guess < number:
            print ("Your guess is too low")
            print()
            

        if guess > number:
            print ("Your guess is too high")
            print ()
            

        if guess == number:
            print ("------------------------------------------------------------------")
            break

    if guess == number:
        guesstaken= str(guesstaken)
        print ("Good job, "+myname+" ,you guessed the number in "+guesstaken+" guesses!")
        print ()
        print ("Thanks for playing, "+myname+" you passed all the levels!")
        time.sleep (3)
        quit ()
            
    if guess != number:
        number= str(number)
        print ("Nope! The number I was thinking of was, "+number)
        print ()
        playagain= input ("Would you like to play again?")
        print ()
        if playagain == "yes" or playagain== "y" or playagain== "Yes":
            print ("------------------------------------------------------------------")
            main()
            

main()
    
