#import pygame
import time
import grovepi
# port D3
ultrasonic_ranger = 6

while True:
    try:
        ranger=grovepi.ultrasonicRead(ultrasonic_ranger)
        #crash_sound=pygame.mixer.Sound("/home/pi/Desktop/NAVI/sounds/eep.wav")

        # Read distance value from Ultrasonic
        print(ranger)
        if ranger<=1000 and ranger>500:
           # pygame.mixer.Sound.play(crash_sound)
           print('CLOSE!!')
           time.sleep(1)
            
        elif ranger<=500 and ranger >=250:
            #pygame.mixer.Sound.play(crash_sound)
            print('very CLOSE!!!')
            time.sleep(0.5)

        elif ranger<=250:
            #pygame.mixer.Sound.play(crash_sound)
            print('TOO FUCKING CLOSE!!!')
            time.sleep(0.25) 

    except TypeError:
        print ("Error")
    except IOError:
        print ("Error")
