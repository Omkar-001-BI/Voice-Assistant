import pyttsx3
import datetime 
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib
import random
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate',170)
# print(voices[1].id)
# engine.setProperty('voices',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    speak("Hello Sir...!")
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning..!")
    elif hour >= 12 and hour <18:
        speak("Good Afternoon...!")
    else:
        speak("Good Evening..!")
    
    speak("Please tell me How may I help you?")


def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('Your Email','vuizekikhkzhclkn')
    server.sendmail('sender Email',to,content)
    server.close()



def takeCommand():
    #This function takes microphone input from the user and returns the string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        r.energy_threshold=400 
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        print("Say that again plz")
        return "None"
    return query

def set_alarm(alarm_time):
   
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == alarm_time:
            music_dir=music_dir = "C:\\Users\\Omkar Dhakane\\OneDrive\\Desktop\\Dance"
            songs=os.listdir(music_dir)
            song_number=random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir,songs[song_number]))
            break
        time.sleep(60)

def jarvisTask():
    while True:
        query = takeCommand().lower()
        #logic to execute task
        if 'wikipedia' in query:
            speak("Ok Sir...!")
            speak("Searching for Wikipedia...!")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to wikipedia")
            print(results)
            speak(results)


        elif 'open youtube' in query:
            speak("Ok Sir...!")
            speak("Opening Youtube for you")
            webbrowser.open("youtube.com")


        elif 'open google' in query:
            speak("Ok Sir...!")
            speak("Opening google")
            webbrowser.open("google.com")


        elif 'open stackoverflow' in query:
            speak("Ok Sir...!")
            speak("Opening stackoverflow")
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            speak("Ok Sir...!")
            speak("Playing music for you sir...")
            music_dir = "C:\\Users\\Omkar Dhakane\\OneDrive\\Desktop\\Dance"
            songs=os.listdir(music_dir)
            song_number=random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir,songs[song_number]))

        elif 'time' in query:
            speak("Ok Sir...!")
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the Time is {strTime}")
            print(strTime)


        elif 'code' in query:
            speak("Ok Sir...!")
            speak("Opening Code... ")
            path = "C:\\Users\\PRATHAMESH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
            speak("Enjoy Your coding")


        elif 'chat gpt' in query:
            speak("Ok Sir...!")
            speak("Opening Chat gpt")
            speak("Ask Your question...")
            webbrowser.open("https://beta.openai.com/docs/")
        
        elif 'email to pratham' in query:
            try:
                speak("What should I say.?")
                content = takeCommand()
                to="howzatcompany@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry, Sir I am not able to send email. Please try again later.")

        elif 'set alarm' in query:
            user_time = input("What time would you like to set the alarm for? (Please use 24-hour format, e.g., 13:30): ")
            set_alarm(user_time)

        elif 'read file' in query:
            file_path= "C:\\Users\\PRATHAMESH\\Downloads\\EDE\\new.txt"
            try:
                os.startfile(file_path)
                with open(file_path,'r') as file:
                    file_contents=file.read()
                    speak(file_contents)
            except Exception as e:
                print(e)


        elif 'quit' in query:
            speak("Thank You for your time sir....! If you need plz let me know I am here to Help You any time..!")
            speak("Good bye sir..!")
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                speak("Have a Nice Day Sir..!")
            elif hour >= 12 and hour <18:
                speak("Have a Great day sir..!")
            else:
                speak("Good Night Sir..!")
            exit()


if __name__ == '__main__':
    wishMe()
    jarvisTask()