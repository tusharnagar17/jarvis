import pyttsx3
import speech_recognition as sr
import datetime
import os
import random
import webbrowser
#import pywhatkit as kit
import sys
import time
# import wikipedia

from requests import get

chrome_path="C:\Program Files\Google\Chrome\Application\chrome.exe"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices',voices[0].id)

## text to speak 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

## To convert voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)

    try:
        print('Recognizing...')
        query= r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
    
    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query
## to greet
def wish():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else: 
        speak("good evening")
    speak("i am jarvis sir. please tell me how can i help you")

# def sendEmail(to, content):
    # server = smtplib.SMTP("smtp.gmail.com", 587)
    # find docs and complete it

## to send email kindly install secure-smtplib


if __name__ == '__main__':
    # takecommand()
    wish()
    while True:
    # if 1:
        query = takecommand().lower()

        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
        elif "open command prompt" in query:
            os.system("start cmd")
        elif "play music" in query:
            music_dir = "F:\\mp3"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
        
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")
            print(ip)
        
        # wikipedia  module not wokring
        # # use wikipeida
        # elif 'wikipedia' in query:
        #     speak("searching wikipedia...")
        #     query = query.replace("wikipedia", "")
        #     results = wikipedia.summary(query, sentences=2)
        #     speak("according to wikipedia")
        #     speak(results)

        # code is not working here

        # elif "open youtube" in query:
        #     speak("opening youtube")
        #     webbrowser.open("www.youtube.com")
        # elif "open google" in query:
        #     speak("Sir, what should i search on google")
        #     cm = takecommand().lower()
        #     webbrowser.get(f"{cm}")
        # elif "send message" in query:
        #     kit.sendwhatmsg("+919891555336", "this is testing messaging", 2, 25)

        # elif "play songs on youtube" in query:
        #     kit.playonyt("game sidhu moosewala")
        
        # use import smtp link as module
        # elif "send email" in query:
        #     try:
        #         speak("what should i say")
        #         content = takecommand.lower()
        #         to= "nagartushar771@gmail.com"
        #         sendEmail(to, content)
        #         speak("Email has been sent to you")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry, I'm not able to sent the email")
        
        elif "no thanks" in query:
            speak("thanks for using me have a nice day")
            # import sys 
            sys.exit()
            
        time.sleep(5)
        speak("sir, do you have any work for me")

