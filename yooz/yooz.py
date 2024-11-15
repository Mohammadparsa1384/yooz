import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import pyautogui
import wolframalpha
from pprint import pprint
engine = pyttsx3.init()
engine.setProperty('rate',150)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def get_command():
    read = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = read.listen(source)

        try:
            cm = read.recognize_google(audio, language='en-US')
            print(f'You said: {cm}\n')
            
        except:
            print("I didn't understand ")
            speak("I didn't understand ")
            return "None"
    return cm

NAME = ""
def welcome():
    hour = datetime.datetime.now().hour
    if 0<= hour<= 12:
        print('Hello Good morning')
        speak('Hello Good morning')
    
    elif 12< hour <=18:
        print('Hello Good evening')
        speak('Hello Good evening')
    
    else:
        print('Hello Good evening')
        speak('Hello Good evening')
    
    print("what is your name\n")
    speak("what is your name")
    global NAME
    while True:
        NAME = get_command().lower()
        if NAME != "none":
            break
    print(f'Welcome {NAME}, let start\n')
    speak(f'Welcome {NAME}, let start')


welcome()

while True:
    print('How can I help you?')
    speak('How can I help you?')
    command = get_command().lower()
    
    if "bye" in command or "stop" in command:
        print(f"Good Bye {NAME}\n")
        speak(f"Good Bye {NAME}\n")
        break
    
    if 'wikipedia' in command:
        print('Searching Wikipedia...\n')
        speak('Searching Wikipedia...')
        command = command.replace('wikipedia','')
        print("How many sentences would you like to read?\n")
        speak("How many sentences would you like to read?")
        try:
            count_sentence = int(get_command())
        except:
            count_sentence = 3
        res = wikipedia.summary(command, sentences=count_sentence)
        print(f"{count_sentence} sentences of your search result in wikipedia:\n")
        speak(f"{count_sentence} sentences of your search result in wikipedia:\n")
        pprint(res+"\n")
        speak(res)
    
    elif "youtube" in command:
        webbrowser.open_new_tab('https://youtube.com')
        print('opening youtube\n')
        speak('opening youtube')
        time.sleep(5)
        
    elif "google" in command:
        webbrowser.open_new_tab('https://google.com')
        print('Opening Google\n')
        speak('Opening Google')
        time.sleep(5)
    
    elif "time" in command:
        str_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(str_time+"\n")
        speak(str_time)
    
    elif "screenshot" in  command:
        my_screen = pyautogui.screenshot()
        my_screen.save("screen.png")
        print('Screen was taken\n')
        speak('Screen was taken')
    
    elif "question" in command:
        print("Now I can answer your calculation and geography questions\n")
        speak("Now I can answer your calculation and geography questions")
        question = get_command()
        app_id = "L8UVR7-GTGLTH9LWR"
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        ans = next(res.results).text
        print(ans+"\n")
        speak(ans)
    
    elif "who" in command:
        print("Hello, I am Voice assistant programmed by Parsa\n")
        speak("Hello, I am an Voice assistant programmed by Parsa")
    
    elif "write note" in command:
        print(f"What should I write {NAME}\n")
        speak(f"What should I write {NAME}")
        note = get_command()
        with open('note.txt','w') as file:
            now = datetime.datetime.now().strftime("%H : %M : %S")
            file.write(now+"\n")
            file.write(note.capitalize())
    
    elif "show note" in command:
        print("Show note\n")
        speak("Show note")
        
        with open('note.txt','r')  as file:
            save_file = file.read()
            print(f"{save_file}\n")
            speak(save_file)
    
    elif "telegram" in command:
        print("opening telegram\n")
        speak("opening telegram")
        os.startfile(r"C:\Users\javid\AppData\Roaming\Telegram Desktop\Telegram.exe")
        time.sleep(5)

  