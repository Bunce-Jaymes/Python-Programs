#My magic 8-ball-- This program will simulate a magic 8-ball
#Introduction: Welcome I am the awesome and powerfull magic 8-ball
#Question: Ask user to type their question
#Store question with a variable
#Simulate a shaking movment
#Choose a random response to display
#Provide answer
#Ask again option

import random
import time

ans1= "It is certain"
ans2= "It is decidedly so"
ans3= "Without a doubt"
ans4= "Yes definitley"
ans5= "You may rely on it"
ans6= "As I see it, yes"
ans7= "Most likely"
ans8= "Outlook good"
ans9= "Yes"
ans10= "Signs point to yes"
ans11= "Reply is hazy try again"
ans12= "Ask again later"
ans13= "Beter not tell you now"
ans14= "Are you sure you should rely on a ball for help?"
ans15= "What do you think that I am smart enought to know that!"
ans16= "Don't count on it"
ans17= "My reply is no"
ans19= "Outlook is not so good"
ans20= "Duh no"

print ("Hello there I am the awesome and powerull magic 8-ball!")
print ()
time.sleep (1)
print ("Bow before the power I hold!")
time.sleep (1)
print ()
while True:

    question= input("Ask me for advice, then press ENTER to shake me.")
    print()

    time.sleep (1)
    print ("*Shaking, duh*")
    time.sleep (3)
    print()
    print ("*Still shaking*")
    time.sleep (3)
    print ()
    print ("*You wonder if your silly question will be anwsered, still shaking*")
    time.sleep (3)
    print ()
    print ("*Shaking.............*"*4)
    print()

    choice= random.randint (1,20)

    if choice == 1:
        answer= ans1
    elif choice == 2:
        answer= ans2
    elif choice == 3:
        answer= ans3
    elif choice == 4:
        answer= ans4
    elif choice == 5:
        answer= ans5
    elif choice == 6:
        answer= ans6
    elif choice == 7:
        answer= ans7
    elif choice == 8:
        answer= ans8
    elif choice == 9:
        answer= ans9
    elif choice == 10:
        answer= ans10
    elif choice == 11:
        answer= ans11
    elif choice == 12:
        answer= ans12
    elif choice == 13:
        answer= ans13
    elif choice == 14:
        answer= ans14
    elif choice == 15:
        answer= ans15
    elif choice == 16:
        answer= ans16
    elif choice == 17:
        answer= ans17
    elif choice == 18:
        answer= ans18
    elif choice == 19:
        answer= ans19
    elif choice == 20:
        answer= ans20

    print (answer)
    print ()
    



