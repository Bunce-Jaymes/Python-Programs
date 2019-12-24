import random
import time
HANGMANPICS = ['''

  000000
 0 |  | 0
 0      0
 0 \__/ 0
  000000

''', '''

  000000
 0 |  | 0
 0      0
 0 \___ 0
  000000
  
''', '''

  000000
 0 |  | 0
 0      0
 0 ____ 0
  000000

''', '''

  000000
 0 |  | 0
 0 ___  0
 0    \ 0
  000000

''', '''

  000000
 0 |  | 0
 0  __  0
 0 /  \ 0
  000000

''', '''

  000000
 0 |  | 0
 0  __ *0
 0 /  \ 0
  000000

''', '''

  000000
 0 x  x 0
 0  __  0
 0 /  \ 0
  000000

''']

animalsWords = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
statesWords= 'alabama alaska arizona arkansas california colorado connecticut delaware florida georgia hawaii idaho illinois indiana iowa kansas kentucky louisiana maine maryland massachusetts michigan minnesota mississippi missouri montana nebraska nevada ohio oklahoma oregon pennsylvania tennessee texas utah vermont virginia washington wisconsin wyoming'.split()
MKWords= 'scorpion raiden sonya kano reptile goro jax kitana baraka mileena kintaro jade smoke cyrax sektor nightwolf kabal sindel sheeva stryker motaro ermac rain'.split()
randomWords= 'scorpion raiden sonya kano reptile goro jax kitana baraka mileena kintaro jade smoke cyrax sektor nightwolf kabal sindel sheeva stryker motaro ermac rain alabama alaska arizona arkansas california colorado connecticut delaware florida georgia hawaii idaho illinois indiana iowa kansas kentucky louisiana maine maryland massachusetts michigan minnesota mississippi missouri montana nebraska nevada ohio oklahoma oregon pennsylvania tennessee texas utah vermont virginia washington wisconsin wyoming ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWord(wordList):
    # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        
        if len(guess) != 1:
            print('Please enter a single letter.')
        if guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')
    print ()

def main():
    time.sleep(1)
    print ("H")
    time.sleep(0.25)
    print (" A")
    time.sleep(0.25)
    print ("  N")
    time.sleep(0.25)
    print ("   G")
    time.sleep(0.25)
    print ("    M")
    time.sleep(0.25)
    print ("     A")
    time.sleep(0.25)
    print ("      N")
    time.sleep(0.25)
    print ("       !")
    time.sleep(0.25)
    print ()
    time.sleep(0.25)
    print ("*****************")
    print (" H A N G M A N ! ")
    print ("*****************")
    print ()


    missedLetters = ''
    correctLetters = ''
    gameIsDone = False

    choice= eval(input('Please select a catagory:\n Type (1) for Animals\n Type (2) for States \n Type (3) for Mortal Kombat charactors \n Type (4) for a random word from all of the categories \n '))
    if choice == 1:
        words= animalsWords
    if choice == 2:
        words= statesWords
    if choice == 3:
        words= MKWords
    if choice == 4:
        words= randomWords
       
    secretWord = getRandomWord(words)
    print ()
    print ("All letters are lower case")
    print ()

    while True:
        displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

        # Let the player type in a letter.
        guess = getGuess(missedLetters + correctLetters)

        if guess in secretWord:
            correctLetters = correctLetters + guess

            # Check if the player has won
            foundAllLetters = True
            for i in range(len(secretWord)):
                if secretWord[i] not in correctLetters:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print ()
                print('Yes! The secret word is "' + secretWord + '"! You have won!')
                gameIsDone = True
        else:
            missedLetters = missedLetters + guess

            # Check if player has guessed too many times and lost
            if len(missedLetters) == len(HANGMANPICS) - 1:
                displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
                print ()
                print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
                gameIsDone = True

        # Ask the player if they want to play again (but only if the game is done).
        if gameIsDone:
            if playAgain():
                main()
                #missedLetters = ''
                #correctLetters = ''
                #gameIsDone = False
                #secretWord = getRandomWord(words)
            else:
                break

main()
                  
