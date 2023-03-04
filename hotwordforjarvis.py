import speech_recognition as sr
import os


def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print("user said:", query)

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


while True:

    query = takeCommand().lower()

    if 'wake up' or 'time to work' in query:
        os.startfile('C:\\Users\\santo\\Desktop\\Ajarvis\\test.py')
        break

    elif 'nova' in query:
        os.startfile('C:\\Users\\santo\\Desktop\\Ajarvis\\test.py')
        break

    elif 'wake' in query:
        os.startfile('C:\\Users\\santo\\Desktop\\Ajarvis\\test.py')
        break

    else:
        print("Nothing..")