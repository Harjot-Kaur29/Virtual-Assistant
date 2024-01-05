import pyttsx3
import speech_recognition as sr
import datetime
import pyjokes
import pywhatkit
import pyautogui
import wikipedia
import os
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

engine.setProperty('rate',200)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening..')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            return command
    except:
        return ""
    
def greeting():
    current_time = datetime.datetime.now()
    hour = current_time.hour
    if 3<=hour<12:
        talk('good morning boss!')
    elif 12<=hour<18:
        talk('good afternoon boss!')
    else:
        talk('good evening boss')


    
def run_jarvis():
    command = take_command()
    if 'hello' in command:
        talk('hi boss,how r u')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'exit' in command:
        talk('goodbye!')
        exit()
    elif 'play' in command:
        song = command.replace('play',"")
        talk('playing' + song)
        pywhatkit.playonyt(command)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is' + time)
    elif 'open' in command:
        command = command.replace('open', '')
        pyautogui.press('super')
        pyautogui.typewrite(command)
        pyautogui.sleep(1)
        pyautogui.press('enter')
        talk('opening' + command)
    elif 'close' in command:
        talk('closing sir!')
        pyautogui.hotkey('alt','f4')

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person,2)
        print(info)
        talk(info)
    
    elif 'remember that' in command:
        rememberMessage = command.replace('remember that','')
        talk('you told me to remember that' + rememberMessage)
        remember = open('remember.txt', 'a')
        remember.write(rememberMessage)
        remember.close()

    elif 'what do you remember' in command:
        remember = open('remember.txt' , 'r')
        talk('you told me to remember' + remember.read())

    elif 'clear remember file' in command:
        file = open('remember.txt','w')
        file.write(f"")
        talk('done boss!everything i remember has been deleted')

    elif 'shutdown' in command:
        talk('closing the pc in')
        talk('3. 2. 1')
        os.system('shutdown /s /t 1')

    elif 'restart' in command:
        talk('restart the pc in')
        talk('3. 2. 1')
        os.system('shutdown /r /t 1')
    elif 'search' in command:
        user_query = command.replace('search', '')
        user_query = user_query.strip()  # Remove leading/trailing spaces
        user_query = user_query.replace(' ', '%20')  # Replace spaces with %20 in the URL
        webbrowser.open(f'https://www.google.com/search?q={user_query}')
        talk('This is what I found on the internet.')

    elif 'stop' in command or 'start' in command:
        pyautogui.press('space')
        talk('Done boss')

    elif 'full screen' in command:
        pyautogui.press('f')
        talk('Done boss')
    
    elif 'theatre screen' in command:
        pyautogui.press('t')
        talk('Done boss')

    else:
        talk('i dont understand')

greeting()
while True:
    run_jarvis() 