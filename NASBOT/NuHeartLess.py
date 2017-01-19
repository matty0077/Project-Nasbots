import random, pickle, os
import os.path
from NuMind import *
from datetime import datetime
t = datetime.now().strftime('%k %M')

from fuchikoma import *

#//////////////////////////////////////////////////////////////
#a = input(ROOK.USER + ": ")#/////////////////edit for speech recognition
#while True:
'''import threading,NuMind
def MooDS():
    FEEL=threading.Thread(target=NuMind.CountDown, args=(150,))
    FEEL.start()
MooDS()'''

#class talk
def response(a):
    #try:
    print("sphinx supposes you said " + a)
    
    POS=open('/home/pi/Desktop/NAVI/memory/FEELINGS/positive.txt', 'r')
    NEG=open('/home/pi/Desktop/NAVI/memory/FEELINGS/negative.txt', 'r')

    ONeg=NEG.readlines()
    OPos=POS.readlines()

    for ONeg in a:#red if negativ
        ROOK.MOOD-=1
        
    for OPos in a:#red if negativ
        ROOK.MOOD+=1
        
    if "quit" in a:
        pickle.dump(self.known, open('memory/known.data', 'wb'))
        with open('memory/FEELINGS/emo.txt', 'w') as f:
            f.write('%d' % ROOK.MOOD)
            f.close()
        print("Saving...")
        exit()

    if "calculate" in a :
        ROOK.calc()

    if "what time is it" in a:
        ROOK.say('time is %s'%t)

    if "search" in a:
        ROOK.browse()

    if "scrape" in a:
        ROOK.scrape()
        
    if "colors" in a:
        ROOK.colors()

    if "paint" in a:
        ROOK.paint()

    if "convert" in a:
        ROOK.Convert()
        
    '''if "magnet" in a:
        ROOK.EMagnet()

    if "what color is that" in a:
        ROOK.ColorSense()'''

    if "music" in a:
        ROOK.Music()

    if "camera" in a:
        ROOK.Cam()

    if "faces" in a:
        ROOK.Faces()

    if "tracker" in a:
        ROOK.say("testing basic targeting")
        import FaceTrack.py

    if "attention" in a:
        FUCHI.attention()
        
    if "who are you" in a:
        ROOK.say("I am "+ ROOK.NAME + " and you are " + ROOK.USER)
        ROOK.say('silly')

    if "how do you feel" in a:
        print(ROOK.MOOD)
        ROOK.Mood()

    if "servo" in a:
        ROOK.MyoMy()

    if "what can you do" in a:
        ROOK.say("well...what i can say is that i was designed to make up for lost senses and limbs, and expand existing ones...among other things")    

    if "#" in a:
        a = ""

    NEG.close()
    POS.close()
    
    '''except sr.UnknownValueError:
        ROOK.say("Google Speech Recognition could not understand audio")
        ROOK.say("say again...?")

    except sr.RequestError as e:
        ROOK.say("Could not request results from Google Speech Recognition service; {0}".format(e))
        ROOK.say("You're not connected for whatever reason...lets try again")'''

    
while True:
    print("listening...")                           #webcam 44100       #512
    r = sr.Recognizer()                             #usb mic 16000      #128
    m=sr.Microphone(device_index = 1, sample_rate = 16000, chunk_size = 128)
    with m as source:
        r.adjust_for_ambient_noise(source, duration=1) # listen for 1 second to calibrate the energy threshold for ambient noise levels
        r.energy_threshold = 1250#175#400
        r.dynamic_energy_threshold = True
        audio = r.listen(source)
        with open("sounds/records/microphone-results.wav", "wb") as f:
            f.write(audio.get_wav_data())
        audio.pause_threshold = 0.65
        
    a=r.recognize_google(audio)
    #a=r.recognize_sphinx(audio)
    response(a)


    

