"""
Irvin Pelcaztre-Ortega and Henry Truong
Section 012
"""


import random
import turtle
#from turtle import*
# Introductory message:
print("\nWelcome to Hangman game. You will get a random generated word, and your goal is to try to figure out the unknown word by guessing only lower case letters before you lose all your limbs.")

def noose():#This will draw the noose which will begin the rest of the game
    t = turtle.Turtle() #initializes the turtle
    t.pu() #pen up
    t.goto(-250,80)
    t.pd() #pen down
    t.speed(50)
    t.fd(100)#forward
    t.rt(180)#right turn
    t.fd(50)
    t.rt(90)
    t.fd(170)
    t.rt(90)
    t.fd(100)
    t.rt(90)
    t.fd(50)
    t.ht() #hides the turtle to remove the arrow that is displayed on screen
    maingame(t)#This function calls a different function which will start the maingame function.
    playAgain = input("Do you wish to play again? (yes/no):")
    playAgain = playAgain.lower() #makes the input lowercase to account for the fact that the user may input a capital word
    if playAgain == "yes": #replays the game if the user wishes to play again
        t.clear()
        print ("") 
        print ("")
        noose() #restarts the game
    elif playAgain == "no":
        print("Thanks for playing!")
        return 0
    else:
        print("Invalid input, terminating game")
        return 0

f = open("lists.txt","w")#This will create a text file with the list of the words
f.write("sunny milk cow red blue green black yellow white pink red browm purple apple pig vitamin arson time word calculator computer math science snapchat instagram facebook vampire dog cat ruler calculus pencil cloudy pencil eraser python function money dance hangman duck rihanna florida canada chips italy france argentina fruite pear watermelon horse soccer football business monitor laptop google folder discord house grass flowers meth water trinidad dior gucci givenchy louis armani tiffany fish sponge violence mountain tree roses daisy rose fendi burberry balenciaga chanel hermes kors verace dolce gabbana bentley")

f.close()

def loadWords():#Returns a list of words that are split up from up above text file. Words are strings of only lowercase letters
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open("lists.txt", 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):#Uses the returned lists of split words from the file and then chooses a random word.

    return (random.choice(wordlist))#Returns a word from wordlist at random


def maingame(t):

    #The first top half is just instructions and selecting a random word and making it into asterisks.
    alphabet = ["a","b","c", "d", "e", "f", "g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] #Makes sure the user's input is a letter.
     
    secret = chooseWord(loadWords())#This will run the function to randomly return a word from the text file.

    guessedLetters = [] #list to keep track of the letters the user has guessed.

    word = [] #a list is initialized for the word that will be guessed
    for i in range(len(secret)):
        word.append(secret[i]) #each letter is appended to the list so that they can be individually changed later (into asterisks)

    secret_word = [] #list for the version of the word displayed to the user

    for i in range(0, len(word)):
        secret_word.append("*") #hiddenWord becomes asterisks for the length of the word

    totalCorrect = 0 #keeps track of correct guesses

    incorrect = 0 #keeps track of incorrect guesses
    print ("")
    print ("The game has started.")
    print ("Remember to click the other window to view the hangman drawing and to only input lowercase letters and never words.")
    print ("")
    print ("Can you guess my word?")
    print ("".join(secret_word)) #outputs the word which is currently being stored as a list, in a string format
    print ("")
    
    while True:
        correct = 0 #used to check if current guess is correct (not total)
        while True:
            newLetter = True #used to determine if the letter has already been guessed
            found = False #used to check if the guessed letter has been found in the unguessed letters
            outputStatement = False #avoids multiple error output statements
            print ("")
            guess = input("Enter a guess:")
            for i in guessedLetters: #checks if the letter has already been guessed
                if guess == i:
                    print ("You've already guessed this letter!")
                    print ("".join(secret_word)) #word is outputted as a string
                    outputStatement = True #prevents duplicate error statements
                    newLetter = False #letter has already been guessed
                    print ("You have already guessed the following:", ", ".join(guessedLetters))

            if newLetter == True: #the following code only functions if the guess is not a repeated letter
                for i in alphabet:
                    if guess == i: #checks that the letter is in the alphabet
                    #del alphabet[alphabet.index(i)]
                        guessedLetters.append(guess) #guessed letter is added to a list to keep track of the previous guesses
                        found = True #the letter has been found in the word
                    elif len(guess) > 1: #checks if the input is larger than 1 character
                        print ("Invalid input. Must be one letter!")
                        print ("".join()) #word is outputted as a string
                        outputStatement = True #prevents duplicate error statements
                        break #exits to allow a new user input
            if found == True: #if the letter has been found, the loop to allow the user to guess is broken
                break
            elif found == False: #if the letter is not a single unguessed letter, a corresponding statement is outputted and the loop continues
                if outputStatement == False: #prevents duplicate error statements
                    print ("Not a valid input!")
                    print ("".join(secret_word)) #word is outputted as a string
        for i in range(0, len(word)): 
            if guess == word[i]:
                correct = 1 #updated to identify that a letter has successfully been guessed
                totalCorrect += 1 #the number of correct letters is increased
                secret_word[i] = guess #the hidden word is updated to display the guessed letters to the user
                word[i] = "*" #the actual word is updated to hide to guessed letters with asterisks
                print ("You guessed a letter!")
                print ("".join(secret_word)) #word is outputted as a string
        
        if correct == 0: #checks if the user guessed zero letters right
            incorrect += 1 #tally for incorrect guesses is increased
            print ("That letter is not in the word!")
            print ("".join(secret_word)) #word is outputted as a string
            drawHangman(t,incorrect) #the function is called to draw a piece on the hangman
        stringWord = "".join(word) #word is joined as a string
       
        check = len(stringWord) * "*" #a string is created which is asterisks equal in length to the word
        
        if stringWord == check: #checks if word has been guessed by seeing if the word is now all asterisks (since each letter is replaced in the word with asterisks as they are guessed)
            print ("")
            print ("YOU WIN!")
            print ("")
            print ("Score:", incorrect,"(# of incorrect guesses - a lower score is better!)")
            break
        elif incorrect == 6: #ends the game if the user makes 6 incorrect guesses
            print ("")
            print ("You guessed 6 wrong! GAME OVER")
            print ("The word was", secret)
            break
    
def drawHangman(t,incorrect):
    '''
    This function is called each time the player makes an incorrect guess.
    The corresponding body part is drawn until the man is completed,
    signifying a GAME OVER. This function will draw a different piece
    for each of the six incorrect guesses. The main function ends the game after the sixth incorrect guess.
    '''
    if incorrect == 1:#Draws rthe head
        t.pu()
        t.goto(-120,180)
        t.pd()
        t.circle(20)
        t.ht() #hides the turtle to remove the arrow that is displayed on screen
    elif incorrect == 2:#Draws the body
        t.pu()
        t.goto(-100,160)
        t.pd()
        t.fd(50)
        t.ht() #hides the turtle to remove the arrow that is displayed on screen
    elif incorrect == 3:#Draws a leg
        t.rt(45)
        t.fd(30)
        t.ht() #hides the turtle to remove the arrow that is displayed on screen
    elif incorrect == 4:#Drawsw a different leg
        t.pu()
        t.rt(-90)
        t.goto(-100,110)
        t.pd()
        t.fd(30)
        t.ht() #hides the turtle to remove the arrow that is displayed on screen
    elif incorrect == 5:#Draws an arm
        t.pu()
        t.rt(-45)
        t.goto(-100,135)
        t.pd()
        t.fd(30)
        t.ht() #hides the turtle to remove the arrow that is displayed on screen
    elif incorrect == 6:#Draws a different arm.
        t.pu()
        t.rt(180)
        t.goto(-100,135)
        t.pd()
        t.fd(30)
        t.pu()
        t.ht() #hides the turtle to remove the arrow that is displayed on screen

#Mainline
noose()


