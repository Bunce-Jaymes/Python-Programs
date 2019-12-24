#This program will help out little boys and girls learn how to count
#The little kids will input what they want to count up to.

import time
count= 0

print ("Hi, I am the counting computer, what is your name?")
name= input()
time.sleep (1)

print ("Hello, "+name+" nice to meet you!")

time.sleep (1)

print ("What number would you like me to count out?")
number= input()
number= int(number)

if number == 0:
    print ("Sorry, please type a number that is greater than 1")

    print ("What number would you like me to count out?")
    number= input()
    number= int(number)

time.sleep (1)

print ("Okay give me one second...")
while count < number:
    count= count + 1
    print (count)
    



