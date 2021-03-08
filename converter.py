import pyttsx3
from moviepy.editor import *

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

speak("give the file location including name of video file")
mp4 = str(input("file location: "))          
mp4_file = mp4
print(mp4_file)

speak("give the file location and name of audio to be saved")
mp3 = str(input("file location: ")) 
mp3_file ="mp3"
  
clip = VideoFileClip(mp4)

clip.audio.write_audiofile(mp3)

speak('sir video converted succesfully, it is saved to'+ mp3)


