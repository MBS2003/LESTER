import requests
import json
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def speak_news():
    url = 'http://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=4a453adb40864126bc3c5404f0d93176'
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    speak('Source: The Times Of India')
    speak('Todays Headlines are..')
    for index, articles in enumerate(arts):
        speak(articles['title'])
        if index == len(arts)-1:
            break
        speak('next')
    speak('These were the top headlines, Have a nice day Sir!!..')

def getNewsUrl():
    return 'http://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=4a453adb40864126bc3c5404f0d93176'

if __name__ == '__main__':
    speak_news()
    speak('Do you want to read the full news...')
    test = takeCommand()
    if 'yes' in test:
        speak('Ok Sir, Opening browser...')
        webbrowser.open(getNewsUrl())
        speak('You can now read the full news from this website.')
    else:
        speak('No Problem Sir')
