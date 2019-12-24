#This program allows you to enter a number and count it to 100

import time

print ("Hey there, what is your name?")
name= input()
time.sleep (1)

print ("Hey, "+name+" nice to meet you!")
time.sleep (1)

while True:
    print ("What number would you like me to count out by,to get to 100?")
    count= input ()
    count= int(count)
    time.sleep (1)

    print ("Okay, one moment please...")
    total=0

    while total < 100:
        total= (count+total)
        print (total)
    
    
    


