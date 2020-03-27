#!/home/bard/miniconda3/envs/Otto/bin/python3

######## IMPORT PYTHON3 MODULES

from gtts import gTTS
import speech_recognition as sr
import os
import aiml
import webbrowser
import smtplib
import subprocess
import pyautogui
import playsound
# import requests
# from weather import Weather
# import re

###############################################################################################

######## THIS IS AIML SETUP STUFF
# aiml is the stuff for the Alice chatbot.
# aiml is modular; so it's easy to add to it.
# all the plugin files are in the "standard" subdirectory. 

# make a variable for the file name
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
    for line in mytext.splitlines():
        # uses the google text to speech module to synthesize text
        text_to_speech = gTTS(text=mytext, lang='en')
        # saves syntesized speech to audio.mp3
        # this file gets written, played. and overwritten
        # over and over again.
        text_to_speech.save('audio.mp3')
        # the sox modules wrapper is mpg123.
        # This is called by the operating system imported os module.
        # os.system('mpg123 -q audio.mp3')
        # I'm testing this using the playsound package
        playsound.playsound(audio)

######## END TTS TEXT TO SPEECH FUNCTION 

###############################################################################################

######## STT SPEECH TO TEXT FUNCTION THAT RETURNS THE VARIABLE: command

def myCommand():
    # "listens for commands"

    # We imported this up above "import speech_recognition as sr"
    # We create a recognizer object and assign it to the variable r.
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready\n ')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        # Here we create the variable audio and fill it with captured audio.
        audio = r.listen(source)

    try:
        # Here we create the variable command and fill it with text converted from audio.
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    # This except block is catching errors if the try block fails.
    # loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();

    # This tiny line is important. It is returning the command variable with the
    # new value we just set.  It will be used later.

    return command

######## END STT SPEECH TO TEXT FUNCTION THAT RETURNS THE VARIABLE: command

###############################################################################################

######## BEGIN GIGANTIC ASSISTANT FUNCTION

def assistant(command):

######## Big If Statement for Executing Commands

######## Open Programs

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

    elif 'terminal' in command:
        #subprocess.call(["terminator"])
        subprocess.call(['terminator','-T', 'First'])
        pyautogui.moveTo(2201, 1001, duration=.1)
        pyautogui.click()
        pyautogui.hotkey('winleft', 'right')

####### I may not implement this.I'm not sure it's that helpful
#    elif 'open website' in command:
#        reg_ex = re.search('open website (.+)', command)
#        if reg_ex:
#            domain = reg_ex.group(1)
#            url = 'https://www.' + domain
#            webbrowser.open(url)
#            print('Done!')
#        else:
#            pass

######## End Open Programs

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
        quit()

######## End System Commands

######## Interface With Desktop

    elif 'click' in command:
        pyautogui.click()

# next command

    elif 'right' in command:
        pyautogui.rightClick()

# next command

    elif 'middle' in command:
        pyautogui.middleClick()

######## End Interface With Desktop

######## Help Section

    elif 'help' in command:
        talkToMe("There are three different wake words")
        talkToMe("They are Help, Computer, and Alice")
        talkToMe("Computer runs the listed commands that follow")
        talkToMe("Also, you can always say COMPUTER list commands.")
        talkToMe("Alice is a chatbot")
        talkToMe("You can talk to Alice about anything")
        talkToMe("But she's dumber than rocks.")
        talkToMe("You can ask me to")

        with open("commandlist") as file:
            for line in file:
                #line = line.strip()
                talkToMe(line)
# next command

    elif 'commands' in command:
        talkToMe("You can ask me to")
        with open("commandlist") as file:
            for line in file:
                #line = line.strip()
                talkToMe(line)

######## End Help Section


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

    # elif 'current weather in' in command:
    #     reg_ex = re.search('current weather in (.*)', command)
    #     if reg_ex:
    #         city = reg_ex.group(1)
    #         weather = Weather()
    #         location = weather.lookup_by_location(city)
    #         condition = location.condition()
    #         talkToMe('The Current weather in %s is %s The tempeture is %.1f degree' % (city, condition.text(), (int(condition.temp())-32)/1.8))
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

talkToMe('To get started, you can say, HELP')

print('To get started say COMPUTER HELP')

#loop to continue executing multiple commands

while True:
        output = myCommand()
        #haloutput = halCommand()

        # Below are the three sections for the three wake words:

        if 'computer' in output:
            print('The computer responds:\n')
            assistant(output)
            print(output)

        elif 'alice' in output:
            print('Alice says:')
            response = brainkernel.respond(output)
            talkToMe(response)
            print(response)

        elif 'help' in output:
            talkToMe("There are three different wake words")
            talkToMe("They are Help, Computer, and Alice")
            talkToMe("Computer runs the listed commands that follow")
            talkToMe("Also, you can always say COMPUTER list commands.")
            talkToMe("Alice is a chatbot")
            talkToMe("You can talk to Alice about anything")
            talkToMe("But she's dumber than rocks.")
            talkToMe("Say ALICE, what's the capital of England?")
            talkToMe("To repeat this and get the list of commands,")
            talkToMe("say, COMPUTER HELP")
            talkToMe("Remember, the list is for the COMPUTER wake word.")


        else:
            pass

######## END MAIN PROGRAM

###############################################################################################
