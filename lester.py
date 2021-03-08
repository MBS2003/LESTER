import pyttsx3
import wikipedia
import speech_recognition as sr
import webbrowser
import datetime
import os
import sys
import smtplib
import psutil
import pyjokes
import pyautogui
from news import speak_news, getNewsUrl 
from loc import weather
from youtube import youtube
import psutil
import pyjokes
from sys import platform
import getpass
import wolframalpha
import key
import keyboard
from sound import Sound

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# print(voices[0].id)

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
        print("recognized:"+ query)

    except Exception as e:
        # print(e)

        print('Say that again please...')
        return 'P'
    return query


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning SIR")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon SIR")

    else:
        speak('Good Evening SIR')

wishMe()
speak('i am back')
    
def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage)

def battery():
    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)

def joke():
    for i in range(5):
        speak(pyjokes.get_jokes()[i])

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:/Users/mbscr/OneDrive/Pictures/lester/screenshot.png")

def time():
    strTime = datetime.datetime.now().strftime("%I:%M:%S")
    speak(strTime)


if __name__ == '__main__':

    if platform == "linux" or platform == "linux2":
        chrome_path = '/usr/bin/google-chrome'

    elif platform == "darwin":
        chrome_path = 'open -a /Applications/Google\ Chrome.app'

    elif platform == "win32":
        chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    else:
        print('Unsupported OS')
        exit(1)

    webbrowser.register(
        'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    
    while True:
        query = takeCommand().lower()

        
            

#functions==========================================================
        
        if 'according to wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif 'search wikipedia' in query:
            speak('what do you want to search')
            query = takeCommand()
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif 'activate iq mode' in query:
            speak('activating iq mode')
            os.startfile("D:\\lester AI\\IQ MODE.py")
            sys.exit()

        elif 'play music' in query:
            os.startfile("D:\\RoiNa.mp3")

        elif 'on spotify' in query:
            query = query.replace('on spotify', '')
            query = query.replace('search', '')
            url = "https://open.spotify.com/search/" + query
            webbrowser.open(url)

        elif 'search youtube' in query:
            speak('What you want to search on Youtube?')
            search = takeCommand()
            url = 'https://www.youtube.com/results?search_query='+ search
            webbrowser.open(url)

        elif 'weather' in query:
            weather()

        elif 'joke' in query:
            joke()

        elif 'cpu usage' in query:
            cpu()

        elif 'battery level' in query:
            battery()

        elif 'shutdown' in query:
            if platform == "win32":
                os.system('shutdown /p /f')
            elif platform == "linux" or platform == "linux2" or "darwin":
                os.system('poweroff')

        elif 'screenshot' in query:
            speak("taking screenshot")
            screenshot()

        elif 'a doubt' in query:
            speak('what is the doubt sir')
            query = takeCommand()
            res = client.query(query)
            results = next(res.results).text
            speak(results)

        elif 'youtube and play' in query:
            ask = query.replace('youtube and play', '')
            search = ask.replace('search', '')
            url = 'https://www.youtube.com/results?search_query='+ search
            webbrowser.open(url)
            key.youtube_play_1()

        elif 'on youtube' in query:
            ask = query.replace('on youtube', '')
            search = ask.replace('search', '')
            url = 'https://www.youtube.com/results?search_query='+ search
            webbrowser.open(url)
            
        elif 'the time' in query:
            speak('the time is')
            time()

        elif 'remember that' in query:
            speak("what should i remember sir")
            rememberMessage = takeCommand()
            speak("you said me to remember"+rememberMessage)
            remember = open('data.txt', 'w')
            remember.write(rememberMessage)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that" + remember.read())

        elif 'on google' in query:
            query = query.replace('on google', '')
            query = query.replace('search', '')
            url = 'https://google.com/search?q=' + query
            webbrowser.open(url)
            speak('Here is What I found for' + query)

        elif 'search google' in query:
            speak('What do you want to search for?')
            search = takeCommand()
            url = 'https://google.com/search?q=' + search
            webbrowser.open(url)
            speak('Here is What I found for' + search)

        elif 'location' in query:
            speak('What is the location?')
            location = takeCommand()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.open(url)
            speak('Here is the location ' + location)
        
#key =======================================================
        elif 'running window' in query:
            key.windows()

        elif 'change window' in query:
            key.window_next()

        elif 'first window' in query:
            key.one()

        elif 'second window' in query:
            key.two()

        elif 'third window' in query:
            key.three()

        elif 'fourth window' in query:
            key.four()

        elif 'fifth window' in query:
            key.five()

        elif 'sixth window' in query:
            key.six()

        elif 'seventh window' in query:
            key.seven()

        elif 'open recent' in query:
            os.startfile('D:\\lester AI\\recent.py')
            key.recent()
            sys.exit()

        elif 'ok' in query or 'get it' in query or 'open it' in query or 'next line' in query:
            key.enter()
            pyautogui.keyUp("alt")
        
        elif 'open my typer' in query:
            os.startfile("D:\\lester AI\\sleep.py")
            os.startfile("D:\\lester AI\\typer.py")
            sys.exit()

        elif 'open settings' in query:
            key.settings()

        elif 'open notification' in query:
            key.notification()

        elif 'start menu' in query:
            key.start_menu()

        elif 'windows search' in query:
            key.search()

        elif 'show desktop' in query:
            key.show_desktop()

        elif 'game bar' in query:
            key.gamebar()

        elif 'start typing' in query:
            key.dict()

        elif 'lock pc' in query:
            key.lockpc()

        elif 'show options' in query:
            key.options()

        elif 'open cortana' in query or 'call cortana' in query:
            key.cortana()

        elif 'taskbar controlls' in query:
            key.controll()

        elif 'minimize window' in query:
            key.minimize()

        elif 'run command' in query:
            key.run()

        elif 'taskbar' in query:
            key.taskbar()

        elif 'fullscreen' in query:
            key.fullscreen()

        elif 'media fullscreen' in query or 'video fullscreen' in query:
            key.media_full()
            
        elif 'close window' in query or 'close it' in query:
            key.close()

        elif 'start menu' in query:
            key.start_menu()

        elif 'scroll up' in query:
            key.scrollup()

        elif 'scroll down' in query:
            key .scrolldown()

        elif 'right' in query:
            key.right()

        elif 'left' in query:
            key.left()

        elif 'down' in query:
            key.down()

        elif 'up' in query:
            key.up()

        elif 'take window left' in query:
            key.alignleft()

        elif 'take window right' in query:
            key.alignright()

        elif 'maximize' in query:
            key.alignup()

        elif 'normal size' in query:
            key.aligndown()

        elif 'tab' in query:
            key.tab()

        elif 'play first' in query:
            key.youtube_play_1()

        elif 'play second' in query:
            key.youtube_play_2()

        elif 'play third' in query:
            key.youtube_play_3()

        elif 'play fourth' in query:
            key.youtube_play_4()

        elif 'play fifth' in query:
            key.youtube_play_5()

        elif 'go bacck' in query or 'browser back' in query:
            key.browser_back()

        elif 'go forward' in query or 'browser forward' in query:
            key.browser_front()

        elif 'go home' in query or 'browser home' in query:
            key.browser_home()

        elif 'web refresh' in query:
            key.browser_refresh()

        elif 'refresh' in query:
            key.f5()

        elif 'play' in query or 'pause' in query:
            key.playpause()
#sleep mode===========================================================
        elif 'sleep mode' in query:
            speak('activating sleep mode')
            speak('bye')
            os.startfile("D:\\lester AI\\sleep.py")
            sys.exit()
#opening==============================================================
        elif 'open app' in query:
            speak('which application do you want to open sir')
            app = takeCommand()
            result = app.replace(' ', '')
            os.startfile(result)

        elif 'open google' in query:
            speak('opening google')
            webbrowser.open('https://google.com')
            speak('here it is')

        elif 'open python' in query:
            speak('opening python')
            os.startfile('idle')
            speak('here it is')

        elif 'open command prompt' in query or 'open CMD' in query:
            speak('opening CMD')
            os.startfile('cmd')
            speak('here it is')

        elif 'open microsoft edge' in query:
            speak('opening microsoft edge')
            os.startfile('microsoftedge')
            speak('here it is')

        elif 'open notepad' in query:
            speak('opening notepad')
            os.startfile('notepad')
            speak('here it is')

        elif 'open vpnbook' in query:
            speak('opening vpnbook')
            webbrowser.open('www.vpnbook.com')
            speak('here it is')

        elif 'open spotify' in query:
            speak('opening spotify')
            webbrowser.open('https://open.spotify.com/?_gl=1*1sl5dzn*_gcl_aw*R0NMLjE2MTQyMjUzMDQuQ2owS0NRaUFqOWlCQmhDSkFSSXNBRTlxUnRDRHB4QlpQcUZQMk9Ea2JKanpIN3BwWW5xUGRzRndiRWxfQnk0VDJOZnhZMmJERE95d0ZMZ2FBbzVaRUFMd193Y0I.*_gcl_dc*R0NMLjE2MTQyMjUzMDQuQ2owS0NRaUFqOWlCQmhDSkFSSXNBRTlxUnRDRHB4QlpQcUZQMk9Ea2JKanpIN3BwWW5xUGRzRndiRWxfQnk0VDJOZnhZMmJERE95d0ZMZ2FBbzVaRUFMd193Y0I.&_ga=2.235877441.1992213099.1614218975-999917305.1614218975&_gac=1.156809673.1614225305.Cj0KCQiAj9iBBhCJARIsAE9qRtCDpxBZPqFP2ODkbJjzH7ppYnqPdsFwbEl_By4T2NfxY2bDDOywFLgaAo5ZEALw_wcB')
            speak('here it is')

        elif 'open spotify' in query:
            speak('opening spotify')
            os.startfile('spotify')
            speak('here it is')

        elif 'open explorer' in query:
            speak('opening explorer')
            os.startfile('explorer')
            speak('here it is')

        elif 'magnify' in query:
            speak('magnifying')
            os.startfile('C:\\Windows\\System32\\Magnify.exe')
            speak('here it is')

        elif 'open task manager' in query:
            speak('opening task manager')
            os.startfile('C:\\Windows\\System32\\Taskmgr.exe')
            speak('here it is')

        elif 'open settings' in query:
            speak('opening settings')
            key.settings()
            speak('here it is')

        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open('https://youtube.com')
            speak('here it is')

        elif 'open whatsapp' in query:
            speak('opening whatsapp')
            webbrowser.open('https://web.whatsapp.com')
            speak('here it is')

        elif 'open facebook' in query:
            speak('opening facebook')
            webbrowser.open('https://www.facebook.com')
            speak('here it is')

        elif 'check my day' in query:
            speak('sir the time is')
            time()
            speak('you dont have any meetings today')
            speak('so feel free')
            speak('i am right online. call me if you want')

        elif 'open browser' in query:
            speak('opening microsoft edge')
            webbrowser.open('new=0')
            speak('here it is')

        elif 'open gmail' in query:
            speak('opening gmail')
            webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
            speak('here it is')

        elif 'open github' in query:
            speak('opening your github page')
            webbrowser.open('https://github.com')
            speak('here it is')

        elif 'open wolframalpha' in query:
            speak('opening wolframalpha')
            webbrowser.open('https://wolframalfa.com')
            speak('here it is')

        elif 'open instagram' in query:
            speak('opening instagram')
            webbrowser.open('https://instagram.com')
            speak('here it is')

        elif 'open twitter' in query:
            speak('opening twitter')
            webbrowser.open('https://twitter.com')
            speak('here it is')

#common==========================================================

        elif 'who created you' in query:
            if platform == "win32" or "darwin":
                speak('MBS created me. He created me as a AI assistant.')
            elif platform == "linux" or platform == "linux2":
                name = getpass.getuser()
                speak(name, 'is my master. He is running me right now')

        elif 'leicester' in query:
            speak('yes sir')

        elif 'thanks' in query or 'thank you' in query:
            speak('welcome sir')

        elif 'your name' in query:
            speak('My name is lester')

        elif 'are you online' in query:
            speak('yes sir i am')

        elif 'who are you' in query:
            speak('i am lester, the AI assistant of MBS')

        elif 'who is mbs' in query or 'who is this mbs' in query:
            speak('MBS is my master, He is a student')
            speak('who programmed me, for his ease of acess')
            speak('Do you want to here more about him')
            ans = takeCommand()
            if 'yes' in ans:
                try:
                    os.startfile('D:\lester AI\MBS.html')
                    speak('opening MBS about web page')
                    speak('MBS means muhammed bilal s')
                    speak('I am Muhammed Bilal. I am studing at G H S S anchalummodu school for pre degree.I am living at India kerala kollam. I love programming, coding, Craft ...etc.')
                except:
                    speak('sorry cannot open now')
            else:
                speak('ok')

        elif 'repeat what i say' in query:
            speak('what do you want me to repeat')
            repeat = takeCommand()
            speak(repeat)

        elif 'hi to mom' in query or 'hi to mum' in query:
            speak('hi mom')
            speak('i know you shamila')
            speak('is it right')

        elif 'say hi to' in query:
            query = query.replace('say hi to', '')
            query = query.replace('my', '')
            speak('hi' + query)

        elif 'welcome to' in query:
            query = query.replace('say welcome to', '')
            query = query.replace('my', '')
            speak('hi' + query)
            speak('welcome to the world of MBS technology')
            speak('i am lester, a AI developed by MBS.')

        elif 'restart' in query:
            os.startfile('D:\\lester AI\lester.py')
            sys.exit()

        elif 'pronouncer' in query:
            speak("started pronouncer. type the text you want me to pronounce")
            get = str(input("type here:"))
            speak(get)

        elif 'good morning' in query or 'good evening' in query or 'good afternoon' in query:
            wishMe()

        elif 'i am back' in query:
            speak('welcome back sir')
            speak('how can i help you')
            
        elif 'stands for' in query:
            speak('I stands for JUST A RATHER VERY INTELLIGENT SYSTEM')

        elif 'do me a favour' in query:
            speak('what do you want me to do, sir')

        elif 'scan pc' in query:
            speak('ok sir, starting pc scan')
            speak('scanning')
            speak('')
            speak('')
            speak('scaning completed')
            cpu()
            battery()
            speak('no malecious file or folder detected')
            speak('if you want to do a advanced scan then tell me')

        elif 'leicester are you there' in query:
            speak("Yes Sir, at your service")

        elif 'hello' in query:
            speak('hi')


        elif 'how are you' in query:
            speak('i am fine, sir')
#sound=================================================
        elif 'sound mute' in query:
            speak('muting PC volume')
            Sound.mute()

        elif 'sound to zero' in query:
            speak('setting sound to 0')
            Sound.volume_min()

        elif 'sound up' in query or 'volume up' in query:
            key.volumeup()

        elif 'sound down' in query or 'volume down' in query:
            key.volumedown()

        elif 'mute' in query or 'unmute' in query:
            key.volume()

        elif 'sound to max' in query:
            Sound.volume_max()
            speak('volume setted to 100')

        elif 'set sound' in query:
            volume.volume()

        elif 'volume state' in query:
            print("Current volume | %s" % str(Sound.current_volume()))
            print("Sound muted    | %s" % str(Sound.is_muted()))

#=====================================================================

        elif 'news' in query:
            speak('Ofcourse sir..')
            os.startfile("D:\\lester AI\\news.py")

        elif 'voice' in query:
            if 'female' in query:
                engine.setProperty('voice', voices[0].id)
            else:
                engine.setProperty('voice', voices[1].id)
            speak("changing voice")
            speak("how is this")

        elif 'p' in query:
            print("ask any thing")
        
        else:
            if 'what' in query or 'who' in query or 'when' in query or 'why' in query or 'how' in query:
                ask = query
                try:
                    res = client.query(ask)
                    results = next(res.results).text
                    print('wolf')
                    speak(results)
                
                except:
                    results = wikipedia.summary(ask, sentences=2)
                    print('wiki')
                    speak(results)
            
