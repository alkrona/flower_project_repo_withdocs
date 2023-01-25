import cv2 as cv
import mediapipe as mp
import posemodule as pm
import time 
import testing_wave_menu_integration
import testing_push_menu_integration
import testing_push_menu_intergration_version2
import arduino_sender
import circle_pattern
import circular_pattern
import random
import analytical_wave_speed_test
import pythonToFirebasesender
mode=1
cap = cv.VideoCapture(1) # used to set the correct webcam
cap.set(3,680)
cap.set(4,480)
detector=pm.PoseDetector(detectionCon=.8)
t_initial=time.time()
t_secondary=time.time()
while True:
    success,img = cap.read()
    img=cv.flip(img,1)
    img=detector.findPose(img)
    lmList,bbox=detector.findPosition(img,False)
    if len(lmList)==33: # checking if the output is correct
        if lmList[16][1]>lmList[15][1] and lmList[14][2]>lmList[16][2] and lmList[14][2]>lmList[12][2] and lmList[13][2]>lmList[15][2] and lmList[13][2]>lmList[15][2] and time.time()>t_secondary+3:
            t_initial=time.time() # checking to see if the person has displayed an X pattern to the screen.
            print("engage mode 1")
            cap.release() # frees up the webcam for use by another application
            cv.destroyAllWindows()
            #testing_push_menu_integration.the_main_function()
            testing_push_menu_intergration_version2.the_main_function()
            t_initial=time.time()
            print("came - back")
            r=[]
            r1=[]
            for _ in range(16):
                r.append(100)
                r1.append(0)
            arduino_sender.SerialObject(r)
            pythonToFirebasesender.firesender(r)
            arduino_sender.SerialObject(r1)
            pythonToFirebasesender.firesender(r1)
            analytical_wave_speed_test.the_main_function()
            t_initial=time.time()
            print("came - back")
            r=[]
            r1=[]
            for _ in range(16):
                r.append(100)
                r1.append(0)
            arduino_sender.SerialObject(r)
            pythonToFirebasesender.firesender(r)
            arduino_sender.SerialObject(r1)
            pythonToFirebasesender.firesender(r1)
            cap = cv.VideoCapture(1)
            cap.set(3,680)
            cap.set(4,480)
            t_secondary=time.time()
            
        
    elif time.time()-t_initial>180:
        #print("success")
        
        t_initial=time.time()
        while t_initial +10 >time.time() :
            
            circle_pattern.circle_pattern_generator()
            
        t_initial=time.time()
       # print("finised operation")
    cv.imshow("image",img)
    cv.waitKey(1)