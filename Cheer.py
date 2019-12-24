#This program will cheer for your local high school team.
#Practice a practical use of a For loop

import time

def main():
    team= input("What team would you like to cheer for?").upper()
    print ()

    for letter in team:
        cheer= "Give me an " + letter + "!"
        print (cheer)
        time.sleep (1)
        print(letter + "!")
        print ()
        

    print ("What does that spell!")
    time.sleep (1)
    print (team + "!")
    print ()

    main()    

main()
