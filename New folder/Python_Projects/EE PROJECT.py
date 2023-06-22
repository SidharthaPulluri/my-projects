import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import psutil
import ctypes
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
def wishme():
    hour = int(datetime.datetime.now().hour)
    speak(hour)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("recognising...")
        query = r.recognize_google(audio,language = 'en-in')
        print("user said",query)
    except Exception as e:
        print(e)
        print("say that again please...")
        return "none"
    return query
if __name__ == "__main__":
    #speak("youtube")
    #wishme()
    if 1:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com")
        elif 'time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {time}")
        elif 'open epic games' in query:
            path = "C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32"
            os.startfile(path)
        elif 'battery percentage' in query:
            battery_data = psutil.sensors_battery()
            speak(battery_data.percent)
        elif 'lock screen' in query:
            ctypes.windll.user32.LockWorkStation()