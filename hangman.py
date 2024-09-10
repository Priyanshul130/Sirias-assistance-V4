
import personal_assistant_api as ast


import random

def play():
   
    with open("words.txt","r") as f:
        words=f.readlines()
    #select a random word from list and covert to upper case
    index=random.randint(0,len(words)-1)
    theWord=words[index].strip().upper() #word to be guessed

    totalChance=7 #total chance
    currentChance=0
    hangman="HANGMAN"
    guessedWord='_'*len(theWord) #word to be guessed
    ast.speak("WELCOME TO HANGMAN")
    while totalChance!=0: #repeat till all the chances are exhausted
        print(guessedWord)
        #get the input from user and convert to upper case since our word is in capitals
        ast.speak("Guess the letter :")
        letter=ast.getAudio().upper() 
        if letter in theWord: #check if letter is present in word
            for index in range(len(theWord)): #get all the index of word
                if theWord[index]==letter: #if letter at index is the letter
                    #replace the blank line at that index with letter
                    guessedWord=guessedWord[:index]+letter+guessedWord[index+1:]
            #check if user has guessed correct
            if guessedWord==theWord:
                ast.speak("Congratulations!!!You Won with ",totalChance," chances to spare")
                break
        else: #if the letter guessed by user was wrong
            totalChance-=1 #totalChance=totalChance-1
            currentChance+=1
            ast.speak("Wrong choice.")
            print("You are now -> ",hangman[:currentChance])
            ast.speak("Chances left "+str(totalChance))
    #when out of while since chances are exhausted
    else:
        ast.speak("The word was "+theWord)
        ast.speak("You lost.All chances exhausted")
