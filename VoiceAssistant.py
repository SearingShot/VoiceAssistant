import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning!!!')
    
    elif hour>=12 and hour<18:
        speak('Good Afternoon!!!')
    
    else:
        speak('Good Evening!!!')

    speak('I am Friday!! Please tell me How may I Help you Sir?')


def takeCommand():
    # it takes microphone input from the user and returns string Output
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing.......')
        query = r.recognize(audio, language='en-in')
        print(f'User Said{query}\n')
    except Exception as e:
        print(e)
        print("Say That Again Please!!!!")
        return "None"
    return query


if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
    
    # Logic for Executing Tasks Based On Query

    if 'wikipedia' in query:
        speak('Searching Wikipedia......')
        query = query.replace('wikipedia','')
        results = wikipedia.summary(query,sentences=5)
        speak("According To Wikipedia, ")
        print(results)
        speak(results)

    elif "open youtube" in query:
        webbrowser.open('youtube.com')

    elif "open google" in query:
        webbrowser.open('google.com')

    elif "open stackoverflow" in query:
        webbrowser.open('stackoverflow.com')

    elif "play music" in query:
        music_dir= "D:\\something not that imp\\wow"
        songs= os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))