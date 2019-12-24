#Duck Realm 1.0

import random
import time

def displayIntro():
    print ("You are on a planet full of ducks. In front of you,")
    print ("You see two caves. In one cave, the duck is friendly")
    print ("and will share his treasure with you. The other duck")
    print ("is greedy and hungry, and he will eat you on sight.")
    print ()

def chooseCave():
    cave= "" #<--- using a string to force a while loop
    while cave != "1" and cave != "2":
        print("Which cave will you go into. (1 or 2)")#This input is a string
        cave= input()
        print ()
        print ("--------------------------------------------------")
        
        return cave 
    

def checkCave(chosenCave):
    print ("You approach the cave...")
    time.sleep (2)
    print ("It is dark and spooky...")
    time.sleep (2)
    print ("A large duck jumps out in front of you! He opens his mouth and...")
    print ()
    time.sleep (2)

    friendlyCave= str(random.randint (1,2))

    if chosenCave == friendlyCave:
        print ("Gives you his treasure!")
        print ()
        print ("--------------------------------------------------")
        time.sleep (2)
        treasureChoice()

    else:
        print ("He begains to charge at you. He is going to trample you!")
        print ()
        print ("--------------------------------------------------")
        time.sleep (2)
        duckCharge()
        
def duckCharge():
    print ("You have to quickly grab something. Out of your")
    print ("eye you spot a knife and a ice pick. You can only")
    print ("pick one")
    print ()

    print ("Which do you choose? (1 or 2)")
    weapon= input()
    print ("--------------------------------------------------")

    print ("You reach for the weapon")
    time.sleep (2)
    print ()
    print ("You pick up the weapon")
    time.sleep (2)
    print ()
    print ("You prepare for the attack and...")
    print ()
    
    luckyweapon= str(random.randint (1,2))

    if weapon == luckyweapon:
        print ("You take the treasure with out any harm")
        print ()
        print ("--------------------------------------------------")
        anotherTreasure()

    else:
        print ("The money is cursed. When you touch it your face melts off,")
        print ("and die.")
        print ()
        print ("--------------------------------------------------")
    
def treasureChoice():
    print ("The duck leaves with two options.")
    time.sleep (2)
    print ("Take a million dollars in gold or, take")
    time.sleep (2)
    print ("a million dollars in silver.")
    print ()

    print ("Which do you choose? (1 or 2)")
    treasureOpt= input()
    print ("--------------------------------------------------")

    print ("You run towards the chest")
    time.sleep (2)
    print ()
    print ("You unlock the chest")
    time.sleep (2)
    print ()
    print ("You slowly opens the chest and...")
    print ()
    
    luckyChest= str(random.randint (1,2))

    if treasureOpt == luckyChest:
        print ("You take the treasure with out any harm")
        print ()
        print ("--------------------------------------------------")
        anotherTreasure()

    else:
        print ("The money is cursed. When you touch it your face melts off,")
        print ("and die.")
        print ()
        print ("--------------------------------------------------")

def anotherTreasure():
    print ("As you are walking away with the treasure you spot something.")
    print ("You see two piles of treasure! On top of one pile there is a big ruby")
    print ("that you could take, or you can take the diamond on the second pile.") 
    print ()
    print ("Which do you take? (1 or 2)")
    print ("--------------------------------------------------")

    rubyChoice= input()

    print ("--------------------------------------------------")

    print ("You reach for the gem")
    time.sleep (2)
    print ()
    print ("You see its amazing pattern")
    time.sleep (2)
    print ()
    print ("The tips of your finger touch the gem and...")
    print ()
    
    luckygem= str(random.randint (1,2))

    if rubyChoice == luckygem:
        print ("You take the gem without any harm")
        print ()
        print ("--------------------------------------------------")
        

    else:
        print ("The gem blows up when you touch it. Nothing remains")
        print ("of your body.")
        print ()
        print ("--------------------------------------------------")
        playAgain()

    
    
    
def playAgain():
    playAgain= "yes"
    while playAgain== "yes" or playAgain== "y":
        displayIntro()

displayIntro()
    
caveNumber = chooseCave()

checkCave(caveNumber)

