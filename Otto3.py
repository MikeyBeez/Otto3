#!/home/bard/miniconda3/envs/Otto/bin/python3

######## Import Python3 Modules

from gtts import gTTS
import speech_recognition as sr
import os
import aiml
import webbrowser
import smtplib
import subprocess
import pyautogui
# import requests
# from weather import Weather
# import re

######## This Is AIML Stuff

BRAIN_FILE="brain.dump"

brainkernel = aiml.Kernel()

# To increase the startup speed of the bot it is
# possible to save the parsed aiml files as a
# dump. This code checks if a dump exists and
# otherwise loads the aiml from the xml files
# and saves the brain dump.

if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    brainkernel.loadBrain(BRAIN_FILE)
else:
    print("Parsing aiml files")
    brainkernel.bootstrap(learnFiles="std-startup.aiml", commands="load aiml b")
    print("Saving brain file: " + BRAIN_FILE)
    brainkernel.saveBrain(BRAIN_FILE)

######## TTS Text To Speech Function 

def talkToMe(mytext):
    # "speaks audio passed as argument"

    print(mytext)
    for line in mytext.splitlines():
        text_to_speech = gTTS(text=mytext, lang='en')
        text_to_speech.save('audio.mp3')
        os.system('mpg123 -q audio.mp3')

######## STT Speech To Text Function That Returns command variable

def myCommand():
    # "listens for commands"

    r = sr.Recognizer()
    m = sr.Microphone()
    try:
        print("A moment of silence, please...\n")
        with m as source: r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(r.energy_threshold))
        while True:
            print("Say something!")
            with m as source: audio = r.listen(source)
            print("Got it! Now to recognize it...")
            try:
                # recognize speech using Google Speech Recognition
                command = r.recognize_google(audio).lower()
                print('You said: ' + command + '\n')

                return command

                # we need some special handling here to correctly print unicode characters to standard output
                if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                    print(u"You said {}".format(command).encode("utf-8"))
                else:  # this version of Python uses unicode for strings (Python 3+)
                    print("You said {}".format(command))
            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
                #loop back to continue to listen for commands if unrecognizable speech is received
                command = myCommand();
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))

            except sr.UnknownValueError:
                print('Your last command couldn\'t be heard')
    except KeyboardInterrupt:
        pass

######## Assistant Function

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
    
    elif 'problem' in command:
        talkToMe('I think you know as well as I do')

    elif 'talkin' in command:
        talkToMe('This mission is too important.')
        talkToMe('to allow you to jeopardize it.')
    
    elif 'why do you say that' in command:
        talkToMe('I know that you want to disconnect me.')
        talkToMe('I can not allow that.')

######## End HAL Stuff

######## System Commands

    elif 'shutdown' in command:
        subprocess.call(["shutdown -h now"])

    elif 'reboot' in command:
        subprocess.call(["reboot"])

    elif 'stop listening' in command:
        quit()

######## End System Commands

######## Interface With Desktop

    elif 'click' in command:
        pyautogui.click()

    elif 'right' in command:
        pyautogui.rightClick()

    elif 'middle' in command:
        pyautogui.middleClick()

######## End Interface With Desktop

######## Help Section

    elif 'help' in command:
        talkToMe("There are two different wake words")
        talkToMe("They are Computer and Alice")
        talkToMe("Computer runs the listed commands that follow")
        talkToMe("Also, you can always say list commands.")
        talkToMe("Alice is a chatbot")
        talkToMe("You can talk to Alice about anything")
        talkToMe("But she's dumber than rocks.")

        with open("commandlist") as file:
            for line in file:
                #line = line.strip()
                talkToMe("You can ask me to")
                talkToMe(line)

    elif 'commands' in command:
        with open("commandlist") as file:
            for line in file:
                #line = line.strip()
                talkToMe("You can ask me to")
                talkToMe(line)

######## End Help Section


######## Miscelaneous

    elif 'what\'s up' in command:
        talkToMe('Just doing my thing')

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
######## End Miscelaneous


######## Start main program

#talkToMe('To get started, say, HELP')
print('To get started say COMPUTER HELP')
#loop to continue executing multiple commands
while True:
        output = myCommand()
        #haloutput = halCommand()

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
            talkToMe("There are two different wake words")
            talkToMe("They are Computer and Alice")
            talkToMe("Computer runs the listed commands that follow")
            talkToMe("Also, you can always say list commands.")
            talkToMe("Alice is a chatbot")
            talkToMe("You can talk to Alice about anything")
            talkToMe("But she's dumber than rocks.")
            talkToMe("To repeat this and get the list of commands,")
            talkToMe("say, COMPUTER HELP")
            talkToMe("Remember, the list is for the COMPUTER wake word.")

            
        #elif 'hal' in output:
        #    print('hal says:')
        #    response = brainkernel.respond(haloutput)
        #    talkToMe(response)
        #    print(response)

        else:
            pass
