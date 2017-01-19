import cv2
from fuchikoma import *
import time

cam_pan = 0#77
cam_tilt =0#77

cap = cv2.VideoCapture(0)
#smaller windows are faster but less accurate
FRAME_W = 440
FRAME_H = 280
cap.set(3, 440) #640WIDTH
cap.set(4, 280) #480HEIGHT
                                    
cascPath = '/usr/share/opencv/lbpcascades/lbpcascade_frontalface.xml'
#face_cascade = cv2.CascadeClassifier('/home/pi/Desktop/NAVI/memory/haar/haarcascade_frontalface_default.xml')
face_cascade=cv2.CascadeClassifier(cascPath)###
#eye_cascade = cv2.CascadeClassifier('/home/pi/Desktop/NAVI/memory/haar/haarcascade_eye.xml')
FUCHI.attention()
time.sleep(.85)
FUCHI.lf_midraise()
FUCHI.move(5,cam_pan)
FUCHI.move(6,cam_tilt)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist( gray )###
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print(len(faces))
    # Display the resulting frame
    for (x,y,w,h) in faces:
        # Draw a green rectancv2.CascadeClassifier(cascPath)gle around the face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
         #//////////////////////////////////////////////
         # Track first face

        # Get the center of the face
        x = x + (w/2)
        y = y + (h/2)

        # Correct relative to center of image
        turn_x  = float(x - (FRAME_W/2))
        turn_y  = float(y - (FRAME_H/2))

        # Convert to percentage offset
        turn_x  /= float(FRAME_W/2)
        turn_y  /= float(FRAME_H/2)

        # Scale offset to degrees
        turn_x   *= 7.5 # VFOV
        turn_y   *= 7.5 # HFOV
        cam_pan  += -turn_x
        cam_tilt += turn_y

        # Clamp Pan/Tilt to 0 to 180 degrees
        cam_pan = max(0,min(180,cam_pan))
        cam_tilt = max(0,min(180,cam_tilt))

        # Update the servos
        FUCHI.move(5,cam_pan)
        FUCHI.move(6,cam_tilt)
        #/////////////////////////////////
        '''roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)'''

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
