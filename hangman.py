
import personal_assistant_api as ast
import random

def play():
   
    with open("words.txt","r") as f:
        words=f.readlines()

    index=random.randint(0,len(words)-1)
    theWord=words[index].strip().upper() 

    totalChance=7 
    currentChance=0
    hangman="HANGMAN"
    guessedWord='_'*len(theWord)
    ast.speak("WELCOME TO HANGMAN")
    while totalChance!=0:
        print(guessedWord)
        
        ast.speak("Guess the letter :")
        letter=ast.getAudio().upper() 
        if letter in theWord:
            for index in range(len(theWord)):
                if theWord[index]==letter: 
                    
                    guessedWord=guessedWord[:index]+letter+guessedWord[index+1:]
         
            if guessedWord==theWord:
                ast.speak("Congratulations!!!You Won with ",totalChance," chances to spare")
                break
        else: g
            totalChance-=1 
            currentChance+=1
            ast.speak("Wrong choice.")
            print("You are now -> ",hangman[:currentChance])
            ast.speak("Chances left "+str(totalChance))
   
    else:
        ast.speak("The word was "+theWord)
        ast.speak("You lost.All chances exhausted")
