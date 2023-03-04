import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import openai as op


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # getting details of current voice
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Mister Rabidas")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Mr Rabidaas")
    else:
        speak("Good Evening Mr Rabidaas")

    speak("I am Nova , sir please tell me how may i help you")
 

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
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":

    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("acording to wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Acording to wikipedia")
            print(results)
            speak(results)

        elif query[:5].lower() == "close":
            import closeapp
            st = [query[5:]]
            closeapp.close(st[0])
            speak("closed")

        elif 'open youtube' in query:
            speak("Opening youtube on your default browser sir")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening google on your default browser sir")
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            speak("Opening facebook on your default browser sir")
            webbrowser.open("facebook.com")

        elif 'open my wordpress dashboard' in query:
            speak("Opening your site on your default browser sir")
            webbrowser.open("rumource.com/wp-admin")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print("The time is", strTime)
            speak(f"Sir the time is, {strTime}")

        elif 'code' in query:
            speak("opening VS code for you sir,")
            codePath = "C:\\Users\\santo\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'upgrade' in query:
            speak("opening code for you sir,")
            codePath = "c:\\Users\\santo\\Desktop\\njarvis\\tempCodeRunnerFile.py"
            os.startfile(codePath)

        elif 'open whatsapp' in query:
            codePath = "C:\\Users\\santo\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            speak("opening whatsapp for you sir,")
            os.startfile(codePath)

        elif 'good bye' in query:
            speak("okay sir, i am going to sleep call me anytime")
            break

        elif 'goodbye' in query:
            speak = ("I am going to sleep mood sir , call me anytime ")
            break

        elif 'play something' in query:
            speak("what should i play sir?")
            song = takeCommand().lower()
            if 'tony stark' in song:

                speak("Okay sir")
                webbrowser.open("www.youtube.com/watch?v=spbpq9ffi2E")
                speak("I am playing Gasoline")

            elif 'kirtan' or 'Radha' in song:
                speak('Okay sir')
                webbrowser.open('https://www.youtube.com/watch?v=6ZwwapPikyQ')

            else:
                speak("i am going to play something, that you might like sir.")
                webbrowser.open(
                    'www.youtube.com/watch?v=qcVt9-LqpJI&list=LL&index=19')

        elif 'friend' and 'you' in query:
            speak('No sir i am just your little creation , i am always here to assist you')

        elif 'today' in query:
            speak('Today is friendship day sir. but i dont think you have any friends')

        elif 'Neural' in query:
            speak('my Neural networks are not ready sir')

        elif "excited" in query:
            speak('Maybe they found another trend sir,')

        elif 'face detection' in query:
            speak("okay sir,")
            codePath = "C:\\Users\\santo\\Desktop\\Ajarvis\\Face_detection.py"
            os.startfile(codePath)

        elif 'open my site' in query:
            speak("Opening Infinite Grow Official Website for you sir")
            webbrowser.open("https://infinitegrow.blogspot.com/")

        
                
        # else:
        #     speak('currently i am not ready for perform this action')
