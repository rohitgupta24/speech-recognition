import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0],id)

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0  and hour <12 :
        speak("good morning")

    if hour>= 12  and hour <18 :
        speak("Good Afternoon")

    else:
        speak("Good Evening")
    speak("I am your personal assistant, how may I help you")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)


    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language ='en-in')
        print("user said:", query)

    except Exception as e:
        #print(e)

        print("say that again please")
        return('none')
    return query
if __name__ == "__main__":
    wishme()
    while True:
        query =take_command().lower()
#logic for executing task based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query =query.replace('wikipedia','')
            results = wikipedia.summary(query , sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query: 
            webbrowser.open('youtube.com')

        elif "open google" in query: 
            webbrowser.open('google.com')

        #elif "play music" in query:
            #music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            #songs = os.listdir(music_dir)
            #print(songs)    
            #os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        #elif 'open code' in query:
            #codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            #os.startfile(codePath)