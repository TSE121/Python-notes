import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from googletrans import Translator
import time

f = time.time()
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

firefox_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def birthdayWish():
    date = float(datetime.datetime.today().strftime("%d.%m"))
    hour = int(datetime.datetime.now().hour)
    if hour >= 13 and date == 06.12:
        speak("Happy birthday Sir!!")
        print("Happy birthday Sir!!")
    elif hour >= 13 and date == 08.10:
        speak("wish your sister a happy birthday")
        print("wish your sister a happy birthday")
    elif hour >= 13 and date == 12.11:
        speak("Wish your father happy birthday")
        print("Wish your father happy birthday")
    elif hour >= 13 and date == 0.11:
        speak("Wish your mother happy birthday")
        print("Wish your mother happy birthday")


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir!!!")
        speak("How may I help you Sir?")
    elif 12 <= hour < 18:
        speak("Good afternoon Sir!!!")
        speak("How may I help you, Sir?")
    else:
        speak("Good evening Sir!!")
        speak("How may I help you, Sir?")


def takeCommand():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 100
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Didn't get that.. Please repeat..")
        return "none"
    return query


if __name__ == '__main__':
    birthdayWish()
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak("According to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.get("firefox").open("youtube.com")
            speak("Opening Youtube")
            print("Opening Youtube")
        elif 'instagram Feed' in query:
            webbrowser.get("firefox").open("https://www.instagram.com/")
            speak("Opening instagram Feed")
            print("Opening instagram Feed")
        elif 'open Instagram dm' in query:
            webbrowser.get("firefox").open("https://www.instagram.com/direct/inbox/")
            speak("Opening instagram DM")
            print("Opening instagram DM")
        elif 'open email' in query:
            webbrowser.get("firefox").open("mail.google.com")
        elif 'what is ' in query:
            speak("Searching...")
            webbrowser.open("https://google.com/?q=%s" % query)
        elif 'open ERP' in query:
            webbrowser.open("https://corp6.myclassboard.com/Home_Student#")
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")
        elif "open Spotify" in query:
            spotify_path = "C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs"
            os.startfile(spotify_path)
        elif "open netflix" in query:
            print("Opening Netflix...")
            speak("Opening Netflix...")
            webbrowser.get('firefox').open('netflix.com')
        elif "open zee5" in query:
            print("Opening Zee5...")
            speak("Opening Zee5...")
            webbrowser.get("firefox").open('zee5.com')
        elif 'open wise cleaner' in query:
            wdc_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Wise Disk Cleaner"
            os.startfile(wdc_path)
        elif "thank you" in query:
            print("It's my pleasure helping you sir...")
            speak("It's my pleasure helping you sir...")
        elif "I love you" in query:
            print("I am not your cup of tea")
            speak("I am not your cup of tea")
        elif "in french" in query:
            query = query.replace("in french", "")
            k_f = Translator().translate(query, src="auto", dest="fr")
            translated_f = str(k_f.text)
            print(translated_f)
            speak(translated_f)
        elif "in spanish" in query:
            query = query.replace("in spanish", "")
            k_es = Translator().translate(query, src="auto", dest="es")
            translated_es = str(k_es.text)
            print(translated_es)
            speak(translated_es)
        elif "in russian" in query:
            query = query.replace("in russian", "")
            k_ru = Translator().translate(query, src="auto", dest="russian")
            translated_ru = str(k_ru.text)
            print(translated_ru)
            speak(translated_ru)
        elif "in chinese" in query:
            query = query.replace("in chinese", "")
            k_ch = Translator().translate(query, src="auto", dest="zh-cn")
            translated_ch = str(k_ch.text)
            print(translated_ch)
            speak(translated_ch)
        elif "in japanese" in query:
            query = query.replace("in japanese", "")
            k_ja = Translator().translate(query, src="auto", dest="japanese")
            translated_ja = str(k_ja.text)
            print(translated_ja)
            speak(translated_ja)
        elif "in german" in query:
            query = query.replace("in german", " ")
            k_ger = Translator().translate(query, src="auto", dest="german")
            translated_ger = str(k_ger.text)
            print(translated_ger)
            speak(translated_ger)
        elif "in bengali" in query:
            query = query.replace("in bengali", ' ')
            k_ben = Translator().translate(query, src="auto", dest="bengali")
            translated_ben = str(k_ben.text)
            print(translated_ben)
            speak(translated_ben)
        elif "in hindi" in query:
            query = query.replace("in hindi", " ")
            k_hin = Translator().translate(query, src="auto", dest="hindi")
            translated_hin = str(k_hin.text)
            print(translated_hin)
            speak(translated_hin)
        elif "in african" in query:
            query = query.replace("in african", "")
            k_af = Translator().translate(query, src="auto", dest="af")
            translated_af = str(k_af.text)
            speak(translated_af)
            print(translated_af)
        elif "open drive" in query:
            speak("Opening Google drive...")
            print("Opening Google drive...")
            webbrowser.get(using="firefox").open('https//:drive.google.com')
        elif "quit" in query:
            exit()
f2 = time.time()
