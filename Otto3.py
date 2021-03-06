#!/home/bard/miniconda3/envs/Otto/bin/python3

######## IMPORT PYTHON3 MODULES
import pyaudio
# from pygame import mixer
from gtts import gTTS
import aiml
import speech_recognition as sr
import pocketsphinx
import pyautogui
import subprocess
# import socket
import os
# import glob
import webbrowser
from time import localtime, strftime
import DateTime
import re
import requests
import wikipedia
from random import randrange
import psutil
import sys

#import smtplib
#from weather import Weather

###############################################################################################
###############################################################################################
#
#   Welcome to Julia -- your virtual assistant
#
#   You can say "Julia Help" to get started
#
###############################################################################################
###############################################################################################

def myVars():
    myDir = os.getcwd()
    global playcounter 
    playcounter = 0
    wakeWord = "julia" 

####Not impemented yet
def runJulius():

    try:
        for lineTest in iter(sys.stdin.readline, b''):
            if "juli" in lineTest:
                print (lineTest)
    except KeyboardInterrupt:
        sys.stdout.flush()
        pass

####End Not impemented yet

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

###############################################################################################
######## THIS IS AIML SETUP STUFF
# aiml is the stuff for the Alice chatbot.
# aiml is modular; so it's easy to add to it.
# all the plugin files are in the "standard" subdirectory. 

# make a variable for the file name
def aimylStuff():
    BRAIN_FILE="brain.dump"

    # This is creating a kernel object from the imported aiml module
    brainkernel = aiml.Kernel()

    # To increase the startup speed of the bot, it is
    # possible to save the parsed aiml files as a dump.
    # This code checks if a dump exists, and
    # otherwise loads the aiml from the xml files.
    # Then it saves the brain dump as brain.dump.

    # the kernel object we just made is empty.  We need to load it.
    if os.path.exists(BRAIN_FILE):
        print("Loading from brain file: " + BRAIN_FILE)
        brainkernel.loadBrain(BRAIN_FILE)
    else:
        print("Parsing aiml files")
        brainkernel.bootstrap(learnFiles="std-startup.aiml", commands="load aiml b")
        print("Saving brain file: " + BRAIN_FILE)
        brainkernel.saveBrain(BRAIN_FILE)

######## END AIML SETUP STUFF

###############################################################################################

######## TTS TEXT TO SPEECH FUNCTION 

# This gets used all over to speak text aloud.
# It also prints to the console for people with bad memories.

def talkToMe(mytext):
    # "speaks audio passed as argument"
    print(mytext)
    # can handle multiline text.
    #for line in mytext.splitlines():
        # uses the google text to speech module to synthesize text
    text_to_speech = gTTS(text=mytext, lang='en-uk')
        # saves syntesized speech to audio.mp3
        # this file gets written, played. and overwritten
        # over and over again.
    text_to_speech.save('audio.mp3')
        # the sox modules wrapper is mpg123.
        # This is called by the operating system imported os module.
    os.system('mpg123 -q audio.mp3')

######## END TTS TEXT TO SPEECH FUNCTION 

###############################################################################################

######## STT SPEECH TO TEXT FUNCTION THAT RETURNS THE VARIABLE: command

def myCommand():
    # "listens for commands"
    # We imported this up above "import speech_recognition as sr"
    # We create a recognizer object and assign it to the variable r.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #talkToMe("To get started, you can say julia help.")
        print("listening")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        # Here we create the variable audio and fill it with captured audio.
        audio = r.listen(source)
    try:
        # Here we create the variable command and fill it with text converted from audio.
        #Use pocketsphinx for wake word
        command = r.recognize_sphinx(audio).lower()
        print('Pocketsphinx thinks you said: ' + command + '\n')
    # This except block is catching errors if the try block fails.
    # loop back to continue to listen for commands if unrecognizable speech is received
    # except sr.UnknownValueError:
    except Exception as e:
        print('waiting . . .  ' +str(e))
        command = myCommand()
    # Use Google for speech to text.  Google is more accurate than pocketsphinx.  Basically pocetsphinx sucks, but it's a good local engin for a wake word.
    try:
        #if "julia" in command or "alice" in command:
        if "julia" in command:
            command = r.recognize_google(audio).lower()
            print('Google thinks you said: ' + command + '\n')

        # This tiny line is important. It is returning the command variable with the
        # new value we just set.  It will be used later.
        return command
    except Exception as e:
        print('problem with Google STT')
        pass

######## END STT SPEECH TO TEXT FUNCTION THAT RETURNS THE VARIABLE: command

###############################################################################################

######## BEGIN GIGANTIC ASSISTANT FUNCTION

def assistant(command, playcounter):

######## Big If Statement for Executing Commands

######## Open Stuff

    if 'open reddit' in command:
        #reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.reddit.com/'
        #if reg_ex:
        #    subreddit = reg_ex.group(1)
        #    url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')
        talkToMe('reddit is opening, shit head!')

# next command

    if 'open youtube' in command:
        url = 'https://www.youtube.com/'
        webbrowser.open(url)
        print('Done!')
        talkToMe('youtube is opening, shit head!')

# next command

    if 'dictation' in command:
        url = 'https://docs.google.com/document/u/0/'
        webbrowser.open(url)
        print('Done!')
        talkToMe('Opening a new document, Sir.')
        # Maximize the window
        pyautogui.hotkey('winleft', 'up')
        # I have a 4k display.  You may need to find 
        # your own point.  I used 
        # xdotool getmouselocation --shell
        # to find the location where to click
        # change duration if your internet is slow.
        pyautogui.moveTo(777, 777, duration=.3)
        pyautogui.click()

# next command

    if 'search' in command:
        url = 'https://google.com'
        webbrowser.open_new_tab(url)
        # Maximize the window
        pyautogui.hotkey('winleft', 'up')
        # I have a 4k display.  You may need to find 
        # your own point.  I used 
        # xdotool getmouselocation --shell
        # to find the location where to click
        # change duration if your internet is slow.
        pyautogui.moveTo(2716, 1209, duration=.3)
        pyautogui.click()
        pyautogui.moveTo(1302, 546, duration=.3)
        pyautogui.click()
        pyautogui.moveTo(2716, 1209, duration=.3)
        pyautogui.click()

# next command

    if 'microphone' in command:
        pyautogui.hotkey('ctrl', 'S')

# next command

    elif 'terminal' in command:
        #subprocess.call(["terminator"])
        subprocess.call(['terminator','-T', 'First'])
        pyautogui.moveTo(2201, 1001, duration=.1)
        pyautogui.click()
        pyautogui.hotkey('winleft', 'right')

# next command

    elif 'open website' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
            print('Done!')
        else:
            pass

######## End Open Stuff

######## Query Stuff
    elif 'wikipedia' in command:
        talkToMe("Searching Wikipedia . . . ")
        command = command.replace("julia", "")
        command = command.replace("julius", "")
        command = command.replace("wikipedia", "")
        try:
            results = wikipedia.summary(command)
            wikiurl = wikipedia.page(command)
            webbrowser.open_new_tab(wikiurl.url)
            print(results)
            talkToMe(results)
        except:
            print("Disambiguation error") 
            talkToMe("Disambiguation error") 

    
# next command
    elif 'look up' in command:
        talkToMe("Searching Wikipedia . . . ")
        command = command.replace("julia", "")
        command = command.replace("julius", "")
        command = command.replace("look up", "")
        results = wikipedia.summary(command, sentences = 3)
        wikiurl = wikipedia.page(command)
        print(wikiurl.url)
        webbrowser.open_new_tab(wikiurl.url)
        print(results)
        talkToMe(results)
    
# next command
    elif 'music' in command:
        if playcounter == 0:
            talkToMe("Choosing random song . . . ")
        with open('/home/bard/Code/Otto3/mymusiclist.txt') as f:
            mymusic = f.read().splitlines()
            random_index = randrange(len(mymusic))
            song = mymusic[random_index]
            print(song)
            playthis = 'mpg123 -q ' + song
            subprocess.call(playthis, shell=True)
            #if checkIfProcessRunning('projectM-pulseaudio'):
            #    print('Yes a projectM process was running')
            #else:
            #    print('No projectM process was running')
            #    pmcommand = 'projectM-pulseaudio 2>/dev/null'
            #    subprocess.call(pmcommand, shell=True)
            #    pyautogui.moveTo(301, 300, duration=.1)
            #    pyautogui.click()
            #    pyautogui.hotkey('winleft', 'up')
            #    pyautogui.click()
            #    pyautogui.hotkey('winleft', 'left')
            if playcounter <= 2:
                playcounter = playcounter + 1
                print(playcounter)
                assistant(command, playcounter)
            else:
                playcounter=0

    
# next command

######## End Query Stuff


######## Polite Stuff
    elif 'hello' in command or 'hi' in command:
        talkToMe('Welcome.  I am Julia, your virtual artificial intelligence assistant.')
        print('Welcome.  I am Julia, your virtual artificial intelligence assistant.')
        talkToMe('How may I help you?')
        print('How may I help you?')
    
# next command
    elif 'thanks' in command or 'tanks' in command or 'thank you' in command:
        talkToMe('You are welcome')
        print('You are welcome')

# next command
    #elif 'julia' in command:
    #    talkToMe('Yes Sir? What can I do for you sir?')
    #    print('Yes Sir? What can I do for you sir?')

# next command
    elif 'how are you' in command or 'and you' in command or 'are you okay' in command:
        talkToMe('Fine thank you.')
        print('Fine thank you.')

######## End Polite Stuff

######## HAL Stuff
    elif 'open the pod door' in command:
        talkToMe('I am sorry, Dave. I am afraid I can not do that.')
    
# next command
    elif 'problem' in command:
        talkToMe('I think you know as well as I do')

# next command
    elif 'talkin' in command:
        talkToMe('This mission is too important.')
        talkToMe(' I can not to allow you to jeopardize it.')
    
# next command
    elif 'why do you say that' in command:
        talkToMe('I know that you want to disconnect me.')
        talkToMe('I can not allow that.')

######## End HAL Stuff

######## System Commands

    elif 'shutdown' in command:
        subprocess.call(["shutdown -h now"])

# next command

    elif 'reboot' in command:
        subprocess.call(["reboot"])

# next command

    elif 'stop listening' in command:
        talkToMe("Goodbye, Sir, powering off")
        print("Goodbye, Sir, powering off")
        quit()

######## End System Commands

######## Interface With Desktop

    elif 'click' in command:
        pyautogui.click()

# next command
    elif 'other' in command:
        pyautogui.rightClick()

# next command
    elif 'middle' in command:
        pyautogui.middleClick()

# next command
    elif 'right' in command:
        pyautogui.moveTo(400, 400, duration=.1)
        pyautogui.click()
        pyautogui.hotkey('winleft', 'right')

# next command
    elif 'left' in command:
        pyautogui.moveTo(2200, 1000, duration=.1)
        pyautogui.click()
        pyautogui.hotkey('winleft', 'left')

# next command

    elif 'maximize' in command:
        pyautogui.click()
        pyautogui.hotkey('winleft', 'up')

# next command
    elif 'minimize' in command:
        pyautogui.click()
        pyautogui.hotkey('winleft', 'h')

######## End Interface With Desktop

######## Help Section
    elif 'help' in command:
        #talkToMe("There are three different wake words")
        talkToMe("There are two different wake words")
        talkToMe("They are Julia, and Alice")
        talkToMe("Julia runs the listed commands that follow")
        talkToMe("You can always say JULIA HELP.")
        talkToMe("Also, you can always say JULIA list commands.")
        talkToMe("Alice is a chatbot")
        talkToMe("You can talk to Alice about anything")
        talkToMe("But she's dumber than rocks.")
        talkToMe("You can ask Julia to")

        with open("commandlist") as file:
            for line in file:
                #line = line.strip()
                talkToMe(line)
# next command
    elif 'commands' in command:
        talkToMe("You can ask Julia to")
        with open("commandlist") as file:
            for line in file:
                #line = line.strip()
                talkToMe(line)

######## End Help SectionEND

######## Miscelaneous
    elif 'what\'s up' in command:
        talkToMe('Just doing my thing')

# next command
    # elif 'joke' in command:
    #     res = requests.get(
    #             'https://icanhazdadjoke.com/',
    #             headers={"Accept":"application/json"}
    #             )
    #     if res.status_code == requests.codes.ok:
    #         talkToMe(str(res.json()['joke']))
    #     else:
    #         talkToMe('oops!I ran out of jokes')

#     elif 'current weather in' in command:
#         reg_ex = re.search('current weather in (.*)', command)
#         if reg_ex:
#             city = reg_ex.group(1)
#             weather = Weather()
#             location = weather.lookup_by_location(city)
#             condition = location.condition()
#             talkToMe('The Current weather in %s is %s The tempeture is %.1f degree' % (city, condition.text(), (int(condition.temp())-32)/1.8))
    #
    # elif 'weather forecast in' in command:
    #     reg_ex = re.search('weather forecast in (.*)', command)
    #     if reg_ex:
    #         city = reg_ex.group(1)
    #         weather = Weather()
    #         location = weather.lookup_by_location(city)
    #         forecasts = location.forecast()
    #         for i in range(0,3):
    #             talkToMe('On %s will it %s. The maximum temperture will be %.1f degree.'
    #                      'The lowest temperature will be %.1f degrees.' % (forecasts[i].date(), forecasts[i].text(), (int(forecasts[i].high())-32)/1.8, (int(forecasts[i].low())-32)/1.8))

#    elif 'email' in command:
#        talkToMe('Who is the recipient?')
#        recipient = myCommand()
#
#        talkToMe('What should I say?')
#        content = myCommand()
#
#        #init gmail SMTP
#        mail = smtplib.SMTP('smtp.gmail.com', 587)
#
#        #identify to server
#        mail.ehlo()
#
#        #encrypt session
#        mail.starttls()
#
#        #login
#        mail.login('username', 'password')
#
#        #send message
#        mail.sendmail('John Fisher', 'JARVIS2.0@protonmail.com', content)
#
#        #end mail connection
#        mail.close()
#
#        talkToMe('Email sent.')
#
#    else:
#        talkToMe('I don\'t know what you mean!')
#
######## End Miscelaneous Section

######## END GIGANTIC ASSISTANT FUNCTION

###############################################################################################

######## START MAIN PROGRAM
def main():
    myVars()
    if checkIfProcessRunning('julius'):
        print("julius is running")
    else:
        #linetest = subprocess.call('sh /home/bard/Code/Otto3/catchjuli.sh')
        #print(linetest)
        #runJulius()
        pass

    #aimylStuff()
    #print('If you are on Ubuntu, ignore the following ALSA errors')
    #print('pyaudio was compiled on a different linux')
    #print('If you can not bear them, you will need to recompile pyaudio.')
    #loop to continue executing multiple commands

    #Uncomment the following line for noobs
    #talkToMe("To get started, You can say julia help.")
    print("To get started, You can say 'Julia help.'")
    print("To get started, You can say 'Julia help.'")
    print("To get started, You can say 'Julia help.'")
    print("To get started, You can say 'Julia help.'")
    print("To get started, You can say 'Julia help.'")
    print("To get started, You can say 'Julia help.'")
    #talkToMe("Hello, Sir.  How can I be of assistance?")
    print("Hello, Sir.  How can I be of assistance?")

    while True:
            output = myCommand()

            # Below are the two sections for the three wake words:

            if 'juli' in output:
                print('The Julia responds:\n')
                assistant(output, playcounter)
                print(output)

#            elif 'alice' in output:
#                print('Alice says:')
#                response = brainkernel.respond(output)
#                talkToMe(response)
#                print(response)
#
#  I removed the following help function and the wake word "help"
#  It was starting accidentially, triggered by normal conversation.
#  Now you must say "julia help" to get this functionality.
#
#            elif 'help' in output:
#                talkToMe("There are three different wake words")
#                talkToMe("They are Help, Julia, and Alice")
#                talkToMe("Julia runs the listed commands that follow")
#                talkToMe("Also, you can always say JULIA list commands.")
#                talkToMe("Alice is a chatbot")
#                talkToMe("You can talk to Alice about anything")
#                talkToMe("But she's dumber than rocks.")
#                talkToMe("Say ALICE, what's the capital of England?")
#                talkToMe("To repeat this and get the list of commands,")
#                talkToMe("say, JULIA HELP")
#                talkToMe("Remember, the list is for the JULIA wake word.")
#
#
            else:
                pass

######## END MAIN FUNCTION
######## CALL MAIN FUNCTION
main()
###############################################################################################
