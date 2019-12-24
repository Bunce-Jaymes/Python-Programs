#Coin Filpper 1.0| This program will simulate a coin toss

import random
import time

def main():
    while True:
        flip= random.randint(1,2)
        #heads= 1
        #tails= 2

        heads= ("""
 000
0 H 0
 000

""")

        tails= ("""

 000
0 T 0
 000

""")
        flat= ("""

 000
""")

        guess= input("Please choose heads or tails: ")

        amountFlip= random.randint(1,10)
        
        for coin in range(amountFlip):
            time.sleep (0.25)
            print (heads)
            time.sleep (0.25)
            print (flat)
            time.sleep (0.25)
            
            print (tails)
            time.sleep (0.25)
            print (flat)
            
        if flip == 1 and guess == "heads":
            print (heads)
            print ("It's heads you win!")

        elif flip == 2 and guess == "tails":
            print (tails)
            print ("It's tails you win!")

        elif flip == 2 and guess == "heads":
            print (tails)
            print ("It was tails! You lose!")

        elif flip == 1 and guess == "tails":
            print (heads)
            print ("It was heads! You lose!")

        print ()
        print ("---------------------------------------")

    
main()

