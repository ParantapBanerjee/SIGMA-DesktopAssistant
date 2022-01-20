import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sys
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0)&(hour<12):
        speak("Good Morning")
    elif(hour>=12)&(hour<18):
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hello sir")
    speak("I am Sigma,a desktop assistant")
    speak("developed by Mister Parantap Banerjee")
    speak("How may I help you?")
def takeCommand():
    #it takes microphone input from user
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User Said:{query}\n")
    except Exception as e:
        print("Say that again please....")
        return "None"
    return query
if __name__=="__main__":
    dict1={"how are you":"i am fine,sir","who are you":"i am Sigma","what do you do":"I assist tasks on desktop","where are you from":"i am from india","how old are you":"i am a few days old"}
    chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    wishMe()
    while(1):
        query=takeCommand().lower()
        #logic for executing tasks based on commands
        if 'wikipedia' in query:
            speak("searching wikipedia.....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.get(chrome_path).open("youtube.com")
        elif 'open google' in query:
            webbrowser.get(chrome_path).open("google.com")
        elif 'play music' in query:
            webbrowser.get(chrome_path).open("https://www.youtube.com/watch?v=3S1NmtWDVYk&list=PLvpJuQwm0QUxu2S1_qa273S7xGVPHF0O4")
        elif 'time' in query:
            l=datetime.datetime.now().strftime("%H:%M:%S")
            print(l)
            speak(f"Sir,the time is {l}")
        elif 'open code' in query:
            code_path="C:\\Users\\Asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
        elif 'go to sleep' in query:
            speak("Goodbye Sir,Call me if you need anything")
            sys.exit()
        elif 'how are you' in query:
            speak(dict1["how are you"])     
        elif 'who are you' in query:
            speak(dict1["who are you"])
        elif 'what do you do' in query:
            speak(dict1["what do you do"])
        elif 'where are you from' in query:
            speak(dict1["where are you from"])
        elif 'how old are you' in query:
            speak(dict1["how old are you"])
