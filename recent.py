import pyttsx3
import speech_recognition as sr
import pyautogui
import key
import sys
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 494
        r.adjust_for_ambient_noise(source, duration=1.5)
        audio = r.listen(source)

    try:
        print('Recognizing..')
        query = r.recognize_google(audio, language='en-in')
        print(f'recognized: {query}\n')

    except Exception as e:
        # print(e)

        print('Say that again please...')
        return 'P'
    return query

if __name__ == '__main__':

    while True:
        query = takeCommand().lower()

        if 'ok done' in query:
            pyautogui.press("space")
            os.startfile('D:\\lester AI\lester.py')
            sys.exit()

        if 'close it' in query or 'quit' in query:
            pyautogui.press("del")

        elif 'right' in query:
            key.right()

        elif 'left' in query:
            key.left()

        elif 'down' in query:
            key.down()

        elif 'up' in query:
            key.up()

        elif 'open' in query:
            pyautogui.press("enter")

        
