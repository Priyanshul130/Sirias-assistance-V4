#**********riddles*********
import random
print("welcome to super coders riddles quiz")
print("-"*30)
#initialise score and dictonary
score=0
riddles={}
#read everything from file
with open("riddles.txt","r")as f:
    questions=f.readlines()
    #get each questions from the list
    #split on the basis of : as q and a
    for question in questions:
        q,a=question.strip().split(":")
        riddles[q]=a
#print the rules
print()
print("max questions asked 5")
print("correct ans +2 marks")
print("wrong ans -1 marks ")
print()
#initalise the question no
que=0
#get all keys from riddles and convert to list
questions=list(riddles.keys())
#shuffle list
random.shuffle(questions)
#read each questions from list
for q in questions:
    #print ques and get answer
    print(q)
    ans=input("Enter your answer")
    if ans.lower()==riddles[q].lower():#compare answer by converting to lower case
        print("correct answer")
        score=score+2#score update
    else:
        print("wrong answer try again")
        print("correct answer-",riddles[q])
        score=score-1
    print("score-",score)
    #increment que no and exit at 5
    que+=1
    if que==5:
        break
print()
print("end of quiz")
print("total score-",score)
        
    
    

        
        
    

