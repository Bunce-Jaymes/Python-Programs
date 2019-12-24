#Duck Realm 1.0

import random
import time

def displayIntro():
    print ("You are on a planet full of ducks. In front of you,")
    print ("You see two caves. In one cave, the duck is friendly")
    print ("and will share his treasure with you(1). The other duck")
    print ("is greedy and hungry, and he will eat you on sight(2).")
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
        print ("He begins to charge at you. He is going to trample you!")
        print ()
        print ("--------------------------------------------------")
        time.sleep (2)
        duckCharge()
        
def duckCharge():
    print ("You have to quickly grab something. Out of your")
    print ("eye you spot a knife(1) and a ice pick(2). You can only")
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
    time.sleep (2)
    
    luckyweapon= str(random.randint (1,2))

    if weapon == luckyweapon:
        print ("You manage to kill the duck before he can reach you")
        print ()
        print ("--------------------------------------------------")
        time.sleep (2)
        extraLoot()

    else:
        print ("Your attempt to stop the duck fails and you get trampled.")
        print ()
        print ("--------------------------------------------------")
        time.sleep (2)
        gunOrDuck()

def gunOrDuck():
    print ("You are bleeding very heavily. Your vision is blurring and")
    print ("life is fading. You spot a gun, you could use it finish your")
    print ("self(1). Or you could let the duck eat you(2).")
    print ()
    
    print ("Which do you choose? (1 or 2)")
    gun= input()
    print ("--------------------------------------------------")

    print ("You see a dark tunnel")
    time.sleep (2)
    print ()
    print ("You spot a light at the end of the tunnel")
    time.sleep (2)
    print ()
    print ("You look at the duck and...")
    print ()
    time.sleep (2)

    if gun == "1":
        print ("You kill your self. But the duck still eats you.")#Ending
        print ()
        print ("--------------------------------------------------")
        time.sleep (2)
        playAgain()
        

    else:
        print ("You are slowly eaten to death.")#Ending
        print ()
        print ("--------------------------------------------------")
        time.sleep (2)
        playAgain()
        
    
def extraLoot():
    print ("You see some armor in the body of the duck,")
    print ("you feel you should take it as a reward(1) or,")
    print ("you could leave it there(2).")
    print ()

    print ("Which do you take it? (1 or 2)")
    extraLoot= input()
    print ("--------------------------------------------------")

    print ("You weigh your options")
    time.sleep (2)
    print ()
    print ("You look deeply at the armour")
    time.sleep (2)
    print ()
    print ("You walk up to it and...")
    print ()
    time.sleep (2)
    
    luckyloot= str(random.randint (1,2))

    if extraLoot == luckyloot:
        print ("You do not regret your choice")#Ending
        print ()
        print ("--------------------------------------------------")
        time.sleep (2)
        ending()

    else:
        print ("Your regret your choice. You sadness consumes you")#Ending
        print ()
        print ("--------------------------------------------------")
        time.sleep (2)
        playAgain()
    

def treasureChoice():
    print ("The duck leaves with two options.")
    print ("Take a million pounds in gold(1) or, take")
    print ("a million pounds(2) in silver.")
    print ()

    print ("Which do you choose? (1 or 2)")
    chestOpt= input()
    print ("--------------------------------------------------")

    print ("You run towards the chest")
    time.sleep (2)
    print ()
    print ("You unlock the chest")
    time.sleep (2)
    print ()
    print ("You slowly opens the chest and...")
    print ()
    time.sleep (2)
    
    luckyChest= str(random.randint (1,2))

    if chestOpt == luckyChest:
        print ("You take the treasure with out any harm")
        print ()
        print ("--------------------------------------------------")
        time.sleep (2)
        anotherTreasure()

    else:
        print ("The money is cursed. When you touch it your hand melts off")
        print ()
        print ("--------------------------------------------------")
        time.sleep (2)
        helpOrDie()

def helpOrDie():
    print ("You are slowly bleeding out. One option it to try to")
    print ("find help(1). Another options is to try to escape(2).")
    print ()
    print ("Which do you do? (1 or 2)")
    lifeOpt= input()
    print ("--------------------------------------------------")

    print ("You think about the options")
    time.sleep (2)
    print ()
    print ("You wiegh the options")
    time.sleep (2)
    print ()
    print ("You begin to stand up and...")
    print ()
    
    luckylife= str(random.randint (1,2))

    if lifeOpt == luckylife:
        print ("You manage to survive!")#Ending
        print ()
        print ("--------------------------------------------------")
        time.sleep (2)
        ending()

    else:
        print ("You bled out before you could make it.")#Ending
        print ()
        print ("--------------------------------------------------")
        time.sleep (2)
        playAgain()
    

def anotherTreasure():
    print ("As you are walking away with the treasure you spot something.")
    print ("You see two piles of treasure! On top of one pile there is a big ruby")
    print ("that you could take(1), or you can take the diamond on the second pile(2).") 
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
    time.sleep (2)
    
    luckygem= str(random.randint (1,2))

    if rubyChoice == luckygem:
        print ("You take the gem without any harm")#Ending
        print ()
        print ("--------------------------------------------------")
        time.sleep (2)
        ending()
        

    else:
        print ("The gem blows up when you touch it. Nothing remains")
        print ("of your body.")#Ending
        print ()
        print ("--------------------------------------------------")
        time.sleep (2)
        playAgain()


def ending():
    print ("Great job you manged to escape duck realm with a story to tell!")
    print ()
    print ("--------------------------------------------------")
    time.sleep (2)
    playAgain()
    
def playAgain():
    playAgain= input("Would you like to play again? (yes or no)")
    print ()
    print ("--------------------------------------------------")
    time.sleep (2)

    if playAgain== "yes" or playAgain== "y":
        displayIntro()

displayIntro()
    
caveNumber = chooseCave()

checkCave(caveNumber)

