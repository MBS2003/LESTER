import pyttsx3
import wikipedia
import webbrowser
import speech_recognition as sr
import os
import sys
import wolframalpha

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

client = wolframalpha.Client('6TA82H-GUE994TRHY')

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
        return 'p'
    return query

def typer():
    query = str(input("type here:"))
    try:
        res = client.query(query)
        results = next(res.results).text
        speak("the answer for the question " + query + " is")
        speak(results)

    except:
        results = wikipedia.summary(query, sentences=2)
        speak("the answer for the question " + query + " is")
        speak(results)

speak('activated IQ mode')

if __name__ == '__main__':

    while True:
        query = takeCommand().lower()

        if 'type the' in query:
            speak('ok then type your question here')
            typer()

        if 'exit iq mode' in query:
            speak('deactivating IQ mode')
            os.startfile("D:\\lester AI\\lester.py")
            sys.exit()

        if 'p' in query:
            print("ask your doubt")

        else:
            query = query
            try:
                res = client.query(query)
                results = next(res.results).text
                speak("the answer for the question " + query + " is")
                speak(results)

            except:
                results = wikipedia.summary(query, sentences=2)
                speak("the answer for the question " + query + " is")
                speak(results)
