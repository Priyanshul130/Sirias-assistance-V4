# importing speech recognition package from google api 
import speech_recognition as sr 
import playsound # to play saved mp3 file
from gtts import gTTS # google text to speech
import os

myAssistantName="sirias"   #change the assistant name here

def speak(output): 
	print(myAssistantName +": ", output) 
        #converts text to speech
	audioOutput = gTTS(text = output, lang ='en', slow = False) 
	# save as audio file	
	audioOutput.save("audioOutput.mp3")	
	# playsound package is used to play the same file. 
	playsound.playsound("audioOutput.mp3", True)
	os.remove("audioOutput.mp3")



def getAudio():
        #create a speech recognizer object
        rObject = sr.Recognizer()
        audio =""
        with sr.Microphone() as source:
                print("Start Speaking...")
                # recording the audio using speech recognition ,wait for 5 secs
                audio = rObject.listen(source,phrase_time_limit=5)
                print("Stop.") # limit 5 secs
        try:
                #convert speech to text
                text = rObject.recognize_google(audio, language ='en-US')
                print("You : ", text)
                return str(text)
        except:
                speak("Pardon me!!I couldn't understand you.Please repeat")
                return "bad input"
