from servodriver import ServoDriver

import numpy as np
from Adafruit_PWM_Servo_Driver import PWM
import traceback as traceback
import time
import sys
#sys.path.append("/home/pi/Desktop/NAVI")
import speech_recognition as sr
from espeak import espeak
from datetime import datetime
t = datetime.now().strftime('%k %M')

# Initialise the PWM device using the default address
pwm = PWM(0x40)

servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096

pwm.setPWMFreq(60)

class FUCHI:
#///////////////////////////////////////////motion
    def move(servo, angle):#, delta=170):
      #delay = max(delta * 0.003, 0.03)        # calculate delay
      zero_pulse = (servoMin + servoMax) / 2  # half-way == 0 degrees
      pulse_width = zero_pulse - servoMin     # maximum pulse to either side 
      pulse = zero_pulse + (pulse_width * angle / 80)
      #print("angle=%s pulse=%s" % (angle, pulse))
      pwm.setPWM(servo, 0, int(pulse))
      #time.sleep(delay)  # sleep to give the servo time to do its thing
      
    def mini(servo):
        #pwm.setPWM(servo, 0, servoMin)
        FUCHI.move(servo,-77)

    def plus(servo):
        #pwm.setPWM(servo,0, servoMax)
        FUCHI.move(servo, 77)

    def relax(servo):
        FUCHI.move(servo, 0)
#//////////////e////////////////////////////////////////rite arm 0 1 2 #3
    def rf_raise():
        FUCHI.move(0, 70)
        #0
        
    def rf_midraise():
        FUCHI.move(0, 35)
        
    def rb_raise():
        FUCHI.move(0, -70)
        #0
        
    def rb_midraise():
        FUCHI.move(0, -35)
    #//////////////////
    def rside_raise():
        FUCHI.move(1, -70)
        #1
    def rside_lax():
        FUCHI.move(1, -15)
        #1
#///////////////////////
    def rite_flex():
        FUCHI.move(2, 65)

    def rite_midflex():
        FUCHI.move(2, 32)    
        
        #2

    def rite_ext():
        FUCHI.move(2, -57)
        #2
    '''def left_open():
        #3
    def left_close():
        #3'''
#///////////////////////////////////////////////////////left arm 4 5 6 #7
    def lf_raise():#/////shoulder
        FUCHI.move(4, -60)

    def lf_midraise():
        FUCHI.move(4, -30)
        #4

    def lb_raise():
        FUCHI.move(4, 65)

    def lb_midraise():
        FUCHI.move(4, 32)
    
#//////////////////lateral
    def lside_raise():
        FUCHI.move(5, 70)
        #5
    def lside_lax():
        FUCHI.move(5, 15)
    
#///////////////////////bicep/tricep
    def left_flex():
        FUCHI.move(6, -65)

    def left_midflex():
        FUCHI.move(6, -32)
        
        
    def left_ext():
        FUCHI.move(6, 30)
        #6
    '''def left_open():
        #3
    def left_close():
        #3'''
#////////////////////////////////////////////////////////left leg 8 9 10 11
    def rhip_side():#////////////hip
        FUCHI.move(8, 70)

    def rhip_lax():
        FUCHI.move(8, 15)
    #////////////////////////knee
    def rknee_up():
        FUCHI.move(9, -75)# spitshine

    def rknee_upmid():
        FUCHI.move(9, -32)# spitshine

    def rknee_bup():
        FUCHI.move(9, 65)

    def rknee_bupmid():
        FUCHI.move(9, 32)
#////////////////////////#lower leg
    def rshin_bend():
        FUCHI.move(10,55)

    def rshin_bendmid():
        FUCHI.move(10,27)
        
    def rshin_bendup():
        FUCHI.move(10,-65)

    def rshin_bendupmid():
        FUCHI.move(10,-37)

#////////////////////////#ankle
    def ra_left():
        FUCHI.move(11,55)
        
    def ra_rite():
        FUCHI.move(11,-55)
#///////////////////////////////////////////////////////right leg 12 13 14 15
    def lhip_side():#////////////hip
        FUCHI.move(12, -55)

    def lhip_lax():
        FUCHI.move(12, -15)
#////////////////////////knee
    def lknee_up():
        FUCHI.move(13, 72)# spitshine

    def lknee_upmid():
        FUCHI.move(13, 36)# spitshine
        
    def lknee_bup():
        FUCHI.move(13, 65)

    def lknee_bupmid():
        FUCHI.move(13, 32)
#////////////////////////#lower leg
    def lshin_bend():
        FUCHI.move(14,-58)

    def lshin_bendmid():
        FUCHI.move(14,-29)
        
    def lshin_bendup():
        FUCHI.move(14,55)

    def lshin_bendupmid():
        FUCHI.move(14,27)

#////////////////////////#ankle
    def la_left():
        FUCHI.move(5,55)
        
    def la_rite():
        FUCHI.move(5,-55)
#/////////////////////////////////////////////ACTIONS!!!
#//////////////////////////////attention!
    def attention():
        FUCHI.relax(14)
        FUCHI.relax(13)
        time.sleep(.25)
        
        FUCHI.lhip_lax()
        FUCHI.relax(11)
        time.sleep(.25)
        
        FUCHI.relax(10)
        FUCHI.relax(9)
        time.sleep(.25)
        
        FUCHI.rhip_lax()
        FUCHI.relax(6)
        time.sleep(.25)

        FUCHI.relax (15)
        FUCHI.lside_lax()
        time.sleep(.25)
        
        FUCHI.relax(2)
        FUCHI.rside_lax()
        time.sleep(.25)

        FUCHI.relax(0)
        FUCHI.relax(4)
#///////////////////////////////////////FIGHT!!
    #///////////////////////////basick warrior
    def warrior():
        lf_midraise()
        left_midflex()
        rf_midraise()
        rite_midflex()

        lknee_upmid()
        rknee_bupmid()
        lshin_bendupmid()
        rshin_bendmid()
 #///////////////////////jab
    def jab_returner():
        lf_midraise()
        left_midflex()
        
    def jab():
        left_ext()
        lf_raise()
        time.sleep(.15)
        jab_returner()

#//////////////////////////rear hand punch
    def rite_returner():
        rf_midraise()
        rite_midflex()

        lknee_upmid()
        rknee_bupmid()
        lshin_bendupmid()
        rshin_bendmid()
        
    def rite_punch():
        lknee_upmid()
        rknee_up()
        rite_ext()
        rf_raise()
        lshin_bendmid()
        rshin_bendmid()
        time.sleep(.55)
        rite_returner()
    
#//////////////////////rite hook
#////////////////////////kicks
#////////////////////////////////////////MOVEMENT
#///////////////////////////walking
#//////////////////////////jump
#////////////////////////////split
    def split():
        lside_raise()
        rside_raise()
        lhip_side()
        rhip_side()
        ra_left()
        la_rite()
    
#////////////////////////////duck
    def duck():
        lknee_up()
        rknee_up()
        lshin_bend()
        rshin_bend()
#////////////////////////////////////////GYRO
    #omnidirection balance/standup
#//////////////////////////////////////////opencv!!
    #/////////////targeting/recognition
def face_targeting():
    import FaceTrack
#////////////////////////////////////////voice rec
#///////////////////////////////////////myo
    #full left arm control 
#//////////////////////////////////////button controls
    #strafing
    #walking fore/back
    #manual aim/autoaim
    #aim assist``lock on when captured in frame
    #punch
#////////////////////////////
#face_targeting()
#FUCHI.relax(0)
FUCHI.attention()
'''time.sleep(.5)
FUCHI.lf_midraise()
FUCHI.left_ext()'''
'''warrior()
time.sleep(.75)
jab()
time.sleep(.25)
jab()
time.sleep(.75)
rite_punch()
time.sleep(.75)
attention()'''
