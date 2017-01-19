import speech_recognition as sr
from espeak import espeak
import time
import random
import cgi,os,cgitb,sys
#sys.path.append("/home/pi/Desktop/NAVI/MYO_KOMA")
#from grove_rgb_lcd import *
#from GROVE import grovepi
cgitb.enable()
###nltk scikit cluster dependancies
import pickle
import string
import collections
'''from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer'''
from pprint import pprint
###//////////////////////// 
class ROOK():
    with open('/home/pi/Desktop/NAVI/memory/FEELINGS/emo.txt', 'r') as f:
        MOOD= int(f.read())#random.randint(0, 100)# happy sad soso grumpy
        f.close()
    
    if MOOD>=0 and MOOD <25:#gloomy
        tspd=100#talkspd
    elif MOOD>=25 and MOOD <75:
        tspd=170# reg
    elif MOOD>=75:
        tspd=350# happy
#//////////////////////////////////////////////speak module
    def say(something):
        POS=open('/home/pi/Desktop/NAVI/memory/FEELINGS/positive.txt', 'r')
        NEG=open('/home/pi/Desktop/NAVI/memory/FEELINGS/negative.txt', 'r')
        try:
            import subprocess
            talk=117                            #v voice       #s rate     p pitch   a volume
            voice1=subprocess.Popen(["espeak", "-v", "mb-en1","-s","tspd","-p","190","-a","80", something])
            #setText(something)#if negative in something set rgb etc
            
            ONeg=NEG.readlines()
            OPos=POS.readlines()
            for ONeg in something:#red if negativ
                ROOK.MOOD-=1
                #print(ROOK.MOOD)
                '''for c in range(0,255):
                    setRGB(255,255-c,255-c)'''
                    
            for OPos in something:#rndm yellow if positive
                ROOK.MOOD+=1
                #print(ROOK.MOOD)
                '''for c in range(0,255):
                    setRGB(255,255,255-c)'''
                    #time.sleep(.01)
              
            '''if OPos and ONeg not in something:#random color otherwise
                setRGB(random.randint(0,255),random.randint(0,255),random.randint(0,255))'''

            NEG.close()
            POS.close()
                    
        except Exception as e:
            print(e.message)
    #/////////////////////////////////////////////load name if exists 
    def loadname():
        file=open("/home/pi/Desktop/NAVI/memory/name.txt", "r")
        Name=file.read()
        if Name!="":
            return Name
        else:
            namesake()
    #///////////////#name self n save otherwise
    def namesake():
        names=['Kenneth','77','Rook','Tobio','Delta','Capricorn','Saint','i-selerian','Hal','Humphreys','Zir-Al-Mega','Zero','Friender','Amuro','Hector','Alpha','Hubris','monty']
        NAME=names[random.randint(0,len(names)-1)]
        fi=open("/home/pi/Desktop/NAVI/memory/name.txt", "w")#"a"
        fi.write("\n" + NAME)
        fi.close()
        return NAME

    NAME=loadname() + "_6S(NasBot)"
    #/////////////////////////////////////////////load uswe name if exists 
    def loaduser():
        file=open("/home/pi/Desktop/NAVI/memory/username.txt", "r")
        user=file.read()
        if user!="":
            return user
        else:
            saveuser()
    #///////////////#ask name n save otherwise
    def saveuser():
        USER=input(NAME +': so whats yer name?')
        fi=open("/home/pi/Desktop/NAVI/memory/username.txt", "w")#"a"
        fi.write("\n" + USER)
        fi.close()
        return USER

    USER=loaduser()

    def calc():
        ROOK.say('math')
        from BASIC import calculator

    def browse():
        ROOK.say('what would you like to look up?')
        google = input('Google search:')
        webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % google)
        #remove_tab to open new window

    def scrape():
        ROOK.say('basic web scraping')
        from BASIC import scrape1
        
    def colors():
        ROOK.say('whoo hoo')
        from BASIC import colorplay

    def paint():
        ROOK.say('lets paint')
        from BASIC import paint

    '''def EMagnet():
        ROOK.say('testing electromagnet')
        from GROVE import emagnet
        
    def ColorSense():
        ROOK.say('the color is...')
        from GROVE import COLOR, grove_i2c_color_sensor'''
        
    def Music():
        ROOK.say('shuffling music')
        from BASIC import music
        
    def Cam():
        ROOK.say('say cheese n die')
        from VISION import camera

    def Faces():
        ROOK.say('searching for faces')
        from VISION import Face_Detect
        
    def Smiles():
        ROOK.say('smile for me')
        from VISION import smile

    def HandyDandy():
        ROOK.say('talk with your hands')
        from VISION import gesture

    def Tracker():
        ROOK.say('tracking faces')
        from SERVO_VISION import FaceTrack
        
    def Convert():
        EX=input("what file are you converting to python3?")
        converter=(['2to3', 'EX'])
        subprocess.call(converter)

    def Mood():
        feeing=''
        if ROOK.MOOD>=0 and ROOK.MOOD<25:
            feeling='gloomy'
        elif ROOK.MOOD>=25 and ROOK.MOOD<75:
            feeling='ok'
        elif ROOK.MOOD>=75:
            feeling='happy!'  
        ROOK.say('I feel...' + feeling)

           
#/////////////////////////////////////////////////////////////////lighting mood
'''def lite_mood():#mood influenced by air quality light color
    light_sensor = 0
    air_sensor = 2
    gro=4
    threshold = 10
    grovepi.pinMode(light_sensor,"INPUT")
    grovepi.pinMode(air_sensor,"INPUT")
    
    while gro>0 :
        try:
            # Get sensor value
            sensor_value = grovepi.analogRead(light_sensor)
            air_value = grovepi.analogRead(air_sensor)
            
            # Calculate resistance of sensor in K
            resistance = (float)(1023 - sensor_value) * 10 / sensor_value
            #print(ROOK.MOOD)
            gro-=1
            if gro<=0:
                CountDown(500000)

            if resistance > threshold:
                #print(ROOK.MOOD)
                ROOK.MOOD+=random.random()
            else:
                ROOK.MOOD-=random.random()
                #//////////////////////////
            if sensor_value > 700:
                ROOK.MOOD-=random.randint(1,3)
                ROOK.say("DANGER! DANGER!")
            elif sensor_value > 300:
                ROOK.MOOD+=random.random()
            else:
                ROOK.MOOD+=random.random()
            
            #time.sleep(.5)

        except IOError:
            print ("Error")
#/////////////////////////////////cluster learning with conversation input
def CountDown(sec):
    while sec>0:
        sec -= 1
        if sec<=0:
            lite_mood()
        #time.sleep(1)'''

#lite_mood()
'''def process_text(text, stem=True):
    # Tokenize text and stem words removing punctuation 
    transtable = {ord(s):None for s in string.punctuation}
    transtable[ord("/")] = "u"
    text = text.translate(transtable)
    tokens = word_tokenize(text)

    if stem:
        stemmer = PorterStemmer()
        tokens = [stemmer.stem(t) for t in tokens]

    return tokens
 
 
def cluster_texts(texts, clusters=3):#clusters=15
    """ Transform texts to Tf-Idf coordinates and cluster texts using K-Means """
    vectorizer = TfidfVectorizer(tokenizer=process_text,
                                 stop_words=stopwords.words('english'),
                                 max_df=0.25,#.25
                                 min_df=0.0028,#.01
                                 lowercase=True)
 
    tfidf_model = vectorizer.fit_transform(texts)
    km_model = KMeans(n_clusters=clusters)
    km_model.fit(tfidf_model)
    
    #shows top 10 words per cluster
    order_centroids = km_model.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names()
    for i in range(clusters):
        print ("Cluster %d:" % i)
        for ind in order_centroids[i, :10]:
            print (" %s" % terms[ind])
 
    clustering = collections.defaultdict(list)
 
    for idx, label in enumerate(km_model.labels_):
        clustering[label].append(idx)
    return clustering

    
    
if __name__ == "__main__":
    articles = []
    fi=pickle.load(open("memory/known.data", "rb"))#fi=open("memory/adapt.txt", "r")
    #data=fi.readlines()
    #for line in data:
      #  articles.append(line) 
    clusters = cluster_texts(fi, 6)#articles
    #for i in clusters:
    pprint(dict(clusters))    
    #    pprint(clusters[i])'''
'''def mictest():
import pyaudio

#device index 0 for speakers 1 for mic
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        dev = p.get_device_info_by_index(i)
        ROOK.say((i,dev['name'],dev['maxInputChannels']))
    main()'''
