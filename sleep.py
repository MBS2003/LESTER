import pyttsx3
import speech_recognition as sr
import os
import sys

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
        return 'None '
    return query

if __name__ == '__main__':

    while True:
        query = takeCommand().lower()

        if 'join' in query:
            os.startfile("D:\\lester AI\\lester.py")
            sys.exit()
