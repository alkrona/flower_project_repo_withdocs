import mediapipe as mp
import cv2 as cv
import posemodule as pm
import time 
import useful_functions
import wave1
def wave_direction_chooser(time_of_action,z_axis_values,array_var,lmList):
    if time.time()>time_of_action[array_var - 1] + 0.2:
                        choice=0
                        z_axis_values[array_var]=abs(lmList[15][1])
                        time_of_action[array_var]=time.time()
                        if array_var<15:
                            array_var+=1
                        else :
                            array_var=0
                        count=0
                        for x in z_axis_values:
                            if x>10:
                                count+=1
                        if count>4:
                            mini=[]
                            
                            for x in z_axis_values:
                                if x>10:
                                    mini.append(x)
                            z_min=min(mini)
                            z_max=max(mini)
                            if abs(z_max-z_min)>200:
                                # print(z_axis_values)
                                # print(z_max,z_min)
                                #print(array_var)
                                #print(time_of_action)
                                t=time.time()
                                state=1
                                if mini.index(z_max)>mini.index(z_min):

                                    print("success1")
                                    print(mini)
                                    choice=1
                                    wave1.main_wave_generator(0)
                                elif mini.index(z_max)<mini.index(z_min) :
                                    print("success2")
                                    print(mini)
                                    wave1.main_wave_generator(1)
                                    choice=2
                                
                                zero_matrix=[]
                                useful_functions.list_initializator(zero_matrix,16)
                                #arduino_sender.sendData(zero_matrix)
                                
                                z_max=0
                                z_min=0
                                for i in range(len(z_axis_values)):
                                    z_axis_values[i]=0
                                array_var=0
    return array_var,time_of_action,z_axis_values 
def wave_direction_chooser2(time_of_action2,z_axis_values2,array_var2,lmList):
     if time.time()>time_of_action2[array_var2-1] + 0.2:
                         choice=0
                         z_axis_values2[array_var2]=abs(lmList[15][2])
                         time_of_action2[array_var2]=time.time()
                         if array_var2<15:
                             array_var2+=1
                         else :
                             array_var2=0
                         count=0
                         for x in z_axis_values2:
                             if x>10:
                                 count+=1
                         if count>4:
                             mini=[]
                            
                             for x in z_axis_values2:
                                 if x>10:
                                     mini.append(x)
                             z_min=min(mini)
                             z_max=max(mini)
                             if abs(z_max-z_min)>200 :
                                
                                #  print(z_axis_values2)
                                #  print(z_max,z_min)
                                #  print(array_var)
                                 #print(time_of_action)
                                t=time.time()
                                state=1
                                if mini.index(z_max)>mini.index(z_min) and  z_max>lmList[12][2]:

                                        print("success3")
                                        print(mini)
                                        choice=3
                                        wave1.main_wave_generator(2)
                                    
                                
                                elif mini.index(z_max)<mini.index(z_min):

                                    print("success4")
                                    choice=4
                                    print(mini)
                                    wave1.main_wave_generator(3)
                                     
                                 
                                zero_matrix=[]
                                useful_functions.list_initializator(zero_matrix,16)
                                 #arduino_sender.sendData(zero_matrix)
                                
                                z_max=0
                                z_min=0
                                for i in range(len(z_axis_values2)):
                                    z_axis_values2[i]=0
                                array_var2=0
     return array_var2,time_of_action2,z_axis_values2
def the_main_function():
    print("now here ")
    cap= cv.VideoCapture(1)
    detector=pm.PoseDetector(detectionCon=.8)
    cap.set(3,680)
    cap.set(4,480)
    buttonList=[]
    width=30
    height=30
    traversal=[]
    array_var=0
    z_axis_values=[]
    useful_functions.list_initializator(z_axis_values,20)
    time_of_action=[]
    useful_functions.list_initializator(time_of_action,20)
    #separation
    array_var2=0
    z_axis_values2=[]
    useful_functions.list_initializator(z_axis_values2,20)
    time_of_action2=[]
    useful_functions.list_initializator(time_of_action2,20)
    wave1.main_wave_generator(0)
    t_secondary=time.time()
    switch=1
    while switch==1:
        success,img=cap.read()
        img=cv.flip(img,1)
        img=detector.findPose(img)
        lmList,bbox=detector.findPosition(img,False)
        if len(lmList)==33:
            #print(time_of_action,z_axis_values,array_var)
            #checking for the x- postion , if yes breaking code
            print(lmList[16][0],lmList[15][0],lmList[14][1],lmList[16][1])
            if lmList[16][1]>lmList[15][1] and lmList[14][2]>lmList[16][2] and lmList[14][2]>lmList[12][2] and lmList[13][2]>lmList[15][2] and lmList[13][2]>lmList[15][2] and time.time()>t_secondary+3:
                switch=0
                print("going back to program 1")
                break
            array_var,time_of_action,z_axis_values=wave_direction_chooser(time_of_action,z_axis_values,array_var,lmList)
            array_var2,time_of_action2,z_axis_values2=wave_direction_chooser2(time_of_action2,z_axis_values2,array_var2,lmList)
            


        

            
            
            
        
        cv.imshow("Pose",img)
        cv.waitKey(1)
    cap.release()
    cv.destroyAllWindows()
def main():
    the_main_function()
if __name__ == "__main__":
    main()