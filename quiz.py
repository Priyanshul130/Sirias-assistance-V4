#************riddles**************#
import random
import personal_assistant_api as ast

def play():
    #print the introductory message
    ast.speak("Welcome to Riddles Quiz!")
    print('_'*30)
    #initialize score and dictionary
    score=0
    riddles={}
    #read everything from file
    with open("riddles.txt","r") as f:
        questions=f.readlines()
    #get each question from the list
    #split on the basis of : as q and a
    for question in questions:
        q,a=question.strip().split(':')
        riddles[q]=a

    #print the rules.
    print()
    ast.speak("Max questions asked :5")
    ast.speak("Correct answer : 2 marks")
    ast.speak("Wrong answer :-1 mark")
    print()
    #initialize the questions asked count
    qCount=0
    #get keys all keys from riddles and convert to list
    questions=list(riddles.keys())
    #shuffle list
    random.shuffle(questions)
    #read each question from list
    for q in questions:
    #print question and get answer
        ast.speak(q)
        ans=ast.getAudio()
        #compare both answer by converting to lower case
        #update and  print score
        if ans.lower()==riddles[q].lower():
            ast.speak("Correct answer")
            score=score+2
        else:
            ast.speak("Correct answer is "+riddles[q])
            score=score-1
        ast.speak("Score is "+str(score))
        #increment question count and exit if 5
        qCount=qCount+1
        if qCount==5:
            break
    print()
    ast.speak("End of riddles quiz")
    ast.speak("Your total Score is "+str(score))

      
            
                  

