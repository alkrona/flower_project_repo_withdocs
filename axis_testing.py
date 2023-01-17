import mediapipe as mp
import cv2 as cv
import posemodule as pm
cap= cv.VideoCapture(2)
detector=pm.PoseDetector(detectionCon=.8)
cap.set(3,680)
cap.set(4,480)
while True:
        success,img=cap.read()
        img=cv.flip(img,1)
        img=detector.findPose(img)
        lmList,bbox=detector.findPosition(img,False)
        if len(lmList)==33:
            print(lmList[15])
        cv.imshow("image",img)
        cv.waitKey(1)