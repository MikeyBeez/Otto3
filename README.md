# Otto3
 
As of March 27, 2020, I'm starting to write this file; so it's going to be tough to install this right now.  Your best bet is to watch a video I recorded recently, but I can't say it's good enough.  That's going to depend on how good you are at making github software work.  Usually, you need to know a lot, but I'll try to make this very easy and educational.  If you still have trouble check back soon.  I've decided to stick with this project for now and make it all work. I'll be setting up a new virtual environment soon to do a fresh install myself.  I plan to make this a video and make copious notes for this readme file.    

Here's a link to the existing video that should help with setting this up: https://www.youtube.com/watch?v=PwoZKKR6MRs

I've written and installed this on Ubuntu 18.04; so I know it works on this platform.  On other platforms, your milage may vary.

Otto3 requires git and python3. I use miniconda to create a virtual environment.  On my own system, I create a directory: 

sudo apt install git

mikdir ~/Code
cd ~/Code
git clone https://github.com/MikeyBeez/Otto3.git
cd Otto3
conda env create otto.yaml

Once you have Otto3 running, you should switch to starting Otto by running otto.sh.  You will need to edit this file to point to your conda environments python and the path to Otto3.py.  From inside your activated conda environment type which python3.  This will give you the path to your actual python command.  After you edit otto.sh, you should start otto from this shell which hides ALSA error messages that are not a problem.  For debugging, however, run Otto3.py directly.  You'll need to make it executable.    
First of all, I've made a video that should help with setting this up: https://www.youtube.com/watch?v=PwoZKKR6MRs

There is a lot of good info on aiml here:  https://www.devdungeon.com/content/ai-chat-bot-python-aiml

I hate using a big if then else statement.  It's just bad coding.  So I intend to fix that.  Even a case statement sucks.  Please let me
know if you have some thoughts on this. 

I've added an aiml chatbot from https://github.com/datenhahn/python-aiml-chatbot.  Basically, I build a brain from the standard directory then interface with tts and stt at the bottom of the Otto3.py file in the while loop.  I hope to upgrade this to aiml 2.0 at some point.  

What follows is some old text that I'm leaving for now but will update or remove later.  The video works.

This is a very simple voice assistant that uses SpeechRecognizer.
I've had a lot of trouble setting up a working environment for Uberi SpeechRecognition, however.  Pyaudio needs to be working right first.  Then you can install speechrecognition.  There are instructions here https://github.com/Uberi/speech_recognition  Even then, I had to install pyaudio using pip and then pip install speechrecognition.  In the end I've got it working.      

#############################  I don't use this anymore.  I'm only leaving this in for historical purposes
so others don't don't go down the same rat hole.

Add The GNUstep Speech Engine.  It works very well.  
I'd be interested in seeing how to change the voice.  

sudo apt-get install gnustep-gui-runtime
I may change this to use festvox for text to speech (TTS)  I think the voices are better.   

Then test it by 
say "hello"

I haven't started working on commands yet.  So far, Otto can 
listen, convert speech to text, and use that text to fire off commands.  There are two main reasons 
why I haven't really worked on commands.  First, I find the if then else structure unwieldy.  I want to write or find 
something that will lookup a commands action directly from a database.  The other reason is I'm trying to discover what
actions are better by voice.  My Echo already works fine for the weather, etc.  This is the sort of thing I have in mind:  https://www.youtube.com/watch?v=YRyYIIFKsdU    

############################

If this interests you, it's is a pretty good start for building a voice assistant.  
It's easy code to understand, although I'll probably add a bunch of comments next to make 
this an even easier base to add to.  I Jesper is based on this as well.   

I put this together after watching John G. Fisher's video on YouTube: 
https://www.youtube.com/watch?v=2eoudIBVW9w&t=213s

He has his code here:  https://github.com/jg-fisher

What I'd like to do is make this project as simple and modular as possible; so that 
others can easily contribute.   

Cheers!
M
