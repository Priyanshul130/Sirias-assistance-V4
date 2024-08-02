import personal_assistant_api as ast
import hangman as hman
import quiz
import datetime
import os
import wolframalpha
import wikipedia
import webbrowser
import playsound
import requests
from openai import OpenAi

#wolfram id
wolfram_appid="TG33P5-7XJGEG6PT5"
#wheater api key
weather_api_key="e7715ef3a95e2bba650cbd2f3a558809"



#name of user
user_name=""


def start_conversation():
    global user_name
    #get username till theare is no error
    ast.speak("what is your name HUMAN?")
    while True:
        user_name=ast.getAudio()
        if user_name!="bad input":
            break

    #find approtiation greeting
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        ast.speak("hello good morning "+user_name)
    elif hour>=12 and hour<18:
        ast.speak("hello good afternoon "+user_name)
    else:
        ast.speak("hello good eavening "+user_name)
    ast.speak("i am your assistant and my name is "+ast.myAssistantName)


#function personal assistant can do
def whatcanido():
    ast.speak("Hello "+user_name)
    ast.speak("My name is "+ast.myAssistantName)
    ast.speak("I can tell you current time and date")
    ast.speak("I can search the web for you. keyword : search")
    ast.speak("I will answer your query. keyword:query")
    ast.speak("I can give a weather report ")
    ast.speak("I can open an application")
    ast.speak("I can laugh and clap")
    ast.speak("I can sing birthday song")
    ast.speak("I can sing Birthday song in sanskrit")
    ast.speak("I can open some specific apps")
    ast.speak("I can open a website")
    ast.speak("I can also play hangman and quiz with you")
    ast.speak("I can shutdown your system for you")
    ast.speak("I hope i can be a great help to you")

def queryChatGpt(user_input):
    gpt=OpenAi(
        api='org-GFaLUibFwmZcFBTKNN8PMq1k'
        )
    r=gpt.chat.completions.create(
        model="gpt-4"
        messages=[{
            'role':'user',
            'content':user_input}]
        )
    ast.speak(r.choices[0].message.content)
    

def querywolfram(user_input):
    #use the same apiid that we have generated earlier
    client=wolframalpha.Client(wolfram_appid)
    res=client.query(user_input)
    try:
        ast.speak(next(res.results).text)
        
    except StopIteration:
        queryWikipedia(user_input)

def queryWikipedia(user_input):
    try:
        results=wikipedia.summary(user_input,sentences=2)
        ast.speak("according to wikipedia")
        ast.speak(results)
    except:
        ast.speak("sorry i dont have an information about this")
        ast.speak("i will do a google search for you")
        queryGoogle(user_input)

def queryGoogle(user_input):
    
    webbrowser.open_new_tab(user_input)
    
def getWeather():
    base_url="https://api.openweathermap.org/data/2.5/weather?"
    ast.speak("city name ?")
    city_name=ast.getAudio()
    complete_url=base_url+"appid="+weather_api_key+"&q="+city_name
    response = requests.get(complete_url)
    res=response.json()
    print(complete_url)
    print(res)
    print(res["cod"])
    if res["cod"]=='404': #success
        ast.speak("Sorry!I don't have information on that")
    else:
        value=res["main"]
        current_temperature = int(float(value["temp"])-273.15)
        current_humidiy = value["humidity"]
        ast.speak(" Temperature is " + str(current_temperature) +" degree celsius "+
                    "and humidity is " + str(current_humidiy) + " percentage.")

    
#start
start_conversation()

while True:
    '''repeat=input("do you have more")
    if repeat=="no":
        break'''
    ast.speak("what can i do for you")
    user_input=ast.getAudio().lower()
    if user_input=="bad input":#if error
        continue
    if "thank you" in user_input or "thanks" in user_input:
        ast.speak("you are welcome "+user_name+".")

    if "exit" in user_input or "bye" in user_input or "sleep" in user_input:
        ast.speak("bye "+user_name)
        break
    elif "who are you" in user_input or "how can you help" in user_input or "what can you do" in user_input:    
        whatcanido()

    elif "who made you" in user_input or "who created you" in user_input:
        ast.speak("Priyanshul made me")
    elif "time" in user_input:
        str_time=datetime.datetime.now().strftime("%H:%M:%S")
        ast.speak("Time is "+str_time)
    elif "date" in user_input:
        ast.speak("today is "+str(datetime.date.today()))

    elif "shutdown" in user_input or "shut down" in user_input:
        ast.speak("Your pc will shut down in 30 seconds make sure you save and exit all application")
        os.system('shutdown /s /t 1')
        break
    elif "search" in user_input or 'google' in user_input:
        
        queryGoogle(user_input)
    elif 'wikipedia' in user_input or "from wikipedia" in user_input:
        queryWikipedia(user_input)
        
    elif "query" in user_input:
        ast.speak("ask me ")
        user_input=ast.getAudio().lower()
        querywolfram(user_input)
    elif 'chatGPT ' in user_input or 'Ask AI' in user_input:
        queryChatGpt(user_input)
    elif "weather" in user_input:
        getWeather()

    elif "notepad" in user_input:
        os.system("notepad")
        ast.speak("notepad opened")

    elif "calculator" in user_input:
        ast.speak("opening")
        os.system("calc")

    elif "clap" in user_input:
        playsound.playsound("clapping.wav",True)

    elif "laugh" in user_input:
        playsound.playsound("laughing.wav",True)

    elif "happy birthday" in user_input:
        playsound.playsound("birthday.mp3",True)

    elif "happy birthday in sanskrit " in user_input:
        playsound.playsound("happybirthday.mp3" , True)

    elif "shopping" in user_input or " add to cart" in user_input:
        ast.speak("i have opened amazon for you happy shopping")
        webbrowser.open_new_tab("https://www.amazon.in/")

    elif "sing" in user_input or "song" in user_input:
        webbrowser.open_new_tab("https://www.gaana.com/")
        ast.speak("listen songs")

    elif "mail" in user_input or "gmail" in user_input or "email" in user_input:
        ast.speak("here you go")
        webbrowser.open_new_tab("https://www.gmail.com/")

    elif "youtube" in user_input or "you tube" in user_input:
        ast.speak("happy browsing")
        webbrowser.open_new_tab("https://www.youtube.com/")

    elif "play" in user_input or "hangman" in user_input:
        hman.play()
    elif "quiz" in user_input or "riddle" in user_input:
        quiz.play()
              
    elif "ways to exam stress management" in user_input or "stress management" in user_input or 'Exam Stress' in user_input: 
        with open("stress.txt","r")as f:
            ans=str(f.readlines())
            ast.speak(ans)
            
    elif 'kill negetive thoughts ' in user_input or 'negative thoughts' in user_input :
        with open('stress1.txt','r')as f:
            ans=str(f.readlines())
            ast.speak(ans)
            
               
    elif 'improve in exams' in user_input or "exam improvement" in user_input:
        with open('stress2.txt','r')as f:
            ans=str(f.readlines())
            ast.speak(ans)
    elif "study skills" in user_input or "improve study skills":
        with open('stress3.txt','r')as f:
            ans=str(f.readlines())
            ast.speak(ans)
        
    elif 'fight fears' in user_input or 'ways to fight fears' in user_input:
        with open('stress4.txt','r')as f:
            ans=str(f.readlines())
            ast.speak(ans)
    else:
        ast.speak("I dont know that")

        
        








        
        
