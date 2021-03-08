from sound import Sound
import sys
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def volume():
    speak('set sound to ')
    volume = int(input("Volume (0 - 100): "))
    Sound.volume_set(volume)
    sys.exit()

volume()
