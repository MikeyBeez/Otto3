# Otto3
This is a very simple voice assistant that uses SpeechRecognizer.
I've had a lot of trouble setting up a working environment for Uberi SpeechRecognition, however.  Pyaudio needs to be working right first.  Then you can install speechrecognition.  There are instructions here https://github.com/Uberi/speech_recognition  Even then, I had to install pyaudio using pip and then pip install speechrecognition.  In the end I've got it working.      

Add The GNUstep Speech Engine.  It works very well.  
I'd be interested in seeing how to change the voice.  

sudo apt-get install gnustep-gui-runtime

Then test it by 
say "hello"

I haven't started working on commands yet.  So far, Otto can 
listen, convert speech to text, and use that text to fire off commands.

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
