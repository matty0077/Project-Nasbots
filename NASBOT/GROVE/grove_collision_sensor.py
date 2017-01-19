#!/usr/bin/env python
#blu led d5
#red d8
#green d7

import time
import grovepi

# Connect the Grove Collision Sensor to digital port D2
# SIG,NC,VCC,GND
collision_sensor = 2

grovepi.pinMode(collision_sensor,"INPUT")

while True:
    try:
        print(grovepi.digitalRead(collision_sensor))
        time.sleep(.5)

    except IOError:
        print ("Error")
