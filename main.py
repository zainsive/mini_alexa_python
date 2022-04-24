import keyboard
import speech_recognition as sr
import pyttsx3
import wikipedia
from pygame import mixer
import pywhatkit

engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[1].id)
def get_audio():
    mixer.init()
    recorder = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something....")
        audio = recorder.listen(source)
    text = recorder.recognize_google(audio)
    print(f"Said: {text}")
    return text

def run_alexa():
    textout = get_audio()
    if "Alexa" in textout:
        text_content = textout.split("Alexa")[1]
        if "play" in text_content:
            text_play = text_content.split("play")[1]
            engine.say(f"playing {text_play}")
            engine.runAndWait()
            pywhatkit.playonyt(text_play)
        if "search" in text_content:
            text_search = text_content.split('search')[1]
            engine.say(f"searching {text_search}")
            engine.runAndWait()
            pywhatkit.search(text_search)
            infotext=wikipedia.summary(text_search,sentences= 5)
            engine.say(infotext)
            engine.runAndWait()
    else:
        engine.say("say hi alexa")
        engine.runAndWait()

while True:
    try:
        if keyboard.is_pressed(" "):
            run_alexa()

    except:
        break