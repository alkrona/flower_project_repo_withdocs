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
mode=1
cap = cv.VideoCapture(1)
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
    if len(lmList)==33:
        if lmList[16][1]>lmList[15][1] and lmList[14][2]>lmList[16][2] and lmList[14][2]>lmList[12][2] and lmList[13][2]>lmList[15][2] and lmList[13][2]>lmList[15][2] and time.time()>t_secondary+3:
            t_initial=time.time()
            print("engage mode 1")
            cap.release()
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
            arduino_sender.SerialObject(r1)
            testing_wave_menu_integration.the_main_function()
            t_initial=time.time()
            print("came - back")
            r=[]
            r1=[]
            for _ in range(16):
                r.append(100)
                r1.append(0)
            arduino_sender.SerialObject(r)
            arduino_sender.SerialObject(r1)
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