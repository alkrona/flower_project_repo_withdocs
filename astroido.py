import random
from button_class import Button
import useful_functions
import cv2 as cv
import handmodule as htm
import mediapipe as mp
import time
import arduino_sender
width=80
height=80
xspan =60
yspan =60
x_List=[0,5,10,15,12,9,6,3]# this is a list that contains the members of the button array required to create the x symbol
b_List=[2,3,6,7]
movable_buttons =[2,3,6,7]
projectile_entry_buttons=[0,4,12,14,15]
cap = cv.VideoCapture(0)
cap.set(3,680)
cap.set(4,480)
detector = htm.HandDetector(detectionCon=0.8,maxHands=1)
def button_Object_creation(xspan,yspan,buttonList,Button):
    for x in range(4):
        for y in range(4):
            xpos=x*xspan + y*yspan +120
            ypos= - x*xspan  + y*yspan+180
            buttonList.append(Button((int(xpos),int(ypos)),xspan,yspan,0,0,(225,225,225)))
            print(xpos,ypos)

buttonList=[]
projectile_path_Dict={0:[0,1,2,3],4:[4,5,6,7],12:[12,9,6,3],14:[14,10,6,2],15:[15,11,7,3]}
current_projectile_list=(random.sample(projectile_entry_buttons,3))   
button_Object_creation(xspan,yspan,buttonList,Button)
'''for _ in  range(10):
    current_projectile_list=(random.sample(projectile_entry_buttons,3))
    l1=[]
    l2=[]
    l3=[]
    l4=[]
    for ele in current_projectile_list:
        l1.append(projectile_path_Dict[ele][0])
        l2.append(projectile_path_Dict[ele][1])
        l3.append(projectile_path_Dict[ele][2])
        l4.append(projectile_path_Dict[ele][3])
    '''
i1=0
i2=0
i3=0
i4=0
Dictofmine=[0,1,2,3]
def value_assigner(buttonList,i1,i2,i3,i4,Dictofmine,current_projectile_list,projectile_path_Dict,gameover):
    for ele in current_projectile_list:
        
        buttonList[projectile_path_Dict[ele][0]].value,p1=value_finder(i1)
        buttonList[projectile_path_Dict[ele][1]].value,p2=value_finder(i2)
        buttonList[projectile_path_Dict[ele][2]].value,p3=value_finder(i3)
        buttonList[projectile_path_Dict[ele][3]].value,p4=value_finder(i4)
        
        if p1==1 and buttonList[projectile_path_Dict[ele][0]].isactive ==1 or  p2==1 and buttonList[projectile_path_Dict[ele][1]].isactive ==1 or p3==1 and buttonList[projectile_path_Dict[ele][2]].isactive ==1 or p4==1 and buttonList[projectile_path_Dict[ele][3]].isactive ==1:
            print("Game over")
            return False
            
def value_finder(i):

    active=False
    if i>=0 and i<=100:
        active=True
        return i,active
        
    elif i>100 and i<=200:
        active=True
        return 200-i,active
    else:
        return 0,active

    pass
print(current_projectile_list)
while True:
    success,img = cap.read()
    #print(success)
    img=cv.flip(img,1)
    hands,img=detector.findHands(img)
    for ele in buttonList:
        ele.draw(img)
    if hands:
        lmList = hands[0]['lmList']
        x,y,z=lmList[8]
    gameover=0
    for _ in range(4):
        
        i1=0
        i2=0
        i3=0
        i4=0
        current_projectile_list=(random.sample(projectile_entry_buttons,1))  
        while True:

            success,img = cap.read()
            #print(success)
            img=cv.flip(img,1)
            hands,img=detector.findHands(img)
            for ele in buttonList:
                ele.draw(img)
            
            cv.imshow("image",img)
            
            i1+=10
            if i1>=100:
                i2+=10
            if i1>=200:
                i3+=10
            if i1>300:
                i4+=10
            if hands:
                
                lmList = hands[0]['lmList']
                x,y,z=lmList[9]
                cv.circle(img,(x,y),4,(255,255,0),3)
                cv.imshow("image",img)
                
                for ele in b_List:
                    buttonList[ele].astroid_activation(x,y,img)
            value_assigner(buttonList,i1,i2,i3,i4,Dictofmine,current_projectile_list,projectile_path_Dict,gameover)
            
            

            m=[]
            useful_functions.list_initializator(m,16)
            for i,ele in enumerate(buttonList):
                Dict={0:6,1:10,2:13,3:15,4:3,5:7,6:11,7:14,8:1,9:4,10:8,11:12,12:0,13:2,14:5,15:9}
                m[Dict[i]]=ele.value
            #print(m)
            arduino_sender.sendData(m)
            if gameover==1:
                i=0
                while i<=100:

                    i+=5
                    for ele in m:
                        ele=i
                    arduino_sender.sendData(m)
                
            
            if i1>500 or gameover==1:
                break
            


