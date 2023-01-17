import cv2 as cv
import handmodule as htm
import mediapipe as mp
import time
import buttonmath
import math
#import controller
import loli
#import serialLed
#import  led
import concurrent.futures
import multiprocessing

def ButArr2Mat(i):
    return(int(i/10),i%10)
def ButMat2Arr(x,y):
    return(x*10 + y)
def viable(i):
    if(0<=i<150):
        return True

class Button:
    def __init__(self,pos,xspan,yspan,value,color):
        self.pos=pos
        self.xspan=xspan
        self.yspan=yspan
        self.value=value
        self.color=color
    def draw(self,img):
        #cv.polylines(img, [[self.pos[0],self.pos[1]],[self.pos[0]+self.xspan,self.pos[1]-self.yspan],[self.pos[0]+self.xspan*2,self.pos[1]],[self.pos[0]+self.xspan,self.pos[1]+self.yspan]],True, self.color, cv.FILLED)
        #cv.polylines(img, [[self.pos[0],self.pos[1]],[self.pos[0]+self.xspan,self.pos[1]-self.yspan],[self.pos[0]+self.xspan*2,self.pos[1]],[self.pos[0]+self.xspan,self.pos[1]+self.yspan]],True, (50,50,50), 3)
        cv.line(img,[self.pos[0],self.pos[1]],[self.pos[0]+self.xspan,self.pos[1]-self.yspan],self.color,3)
        cv.line(img,[self.pos[0]+self.xspan,self.pos[1]-self.yspan],[self.pos[0]+self.xspan*2,self.pos[1]],self.color,3)
        cv.line(img,[self.pos[0]+self.xspan*2,self.pos[1]],[self.pos[0]+self.xspan,self.pos[1]+self.yspan],self.color,3)
        cv.line(img,[self.pos[0],self.pos[1]],[self.pos[0]+self.xspan,self.pos[1]+self.yspan],self.color,3)
        
        #cv.putText(img,self.value,(self.pos[0]+40,self.pos[1]+60),cv.FONT_HERSHEY_COMPLEX_SMALL,2,(50,50,50),2)
    
    def Activation(self,x,y,img):
        if self.pos[0]>x-100 and self.pos[0]<x+100 and self.pos[1]>y and self.pos[1]<y+200:
            if self.color==(225,225,225):
                self.color=(0,0,255)
                cv.line(img,[self.pos[0],self.pos[1]],[self.pos[0]+self.xspan,self.pos[1]-self.yspan],self.color,3)
                cv.line(img,[self.pos[0]+self.xspan,self.pos[1]-self.yspan],[self.pos[0]+self.xspan*2,self.pos[1]],self.color,3)
                cv.line(img,[self.pos[0]+self.xspan*2,self.pos[1]],[self.pos[0]+self.xspan,self.pos[1]+self.yspan],self.color,3)
                cv.line(img,[self.pos[0],self.pos[1]],[self.pos[0]+self.xspan,self.pos[1]+self.yspan],self.color,3)
                
            
    def deActivation(self,x,y,img):
        if self.pos[0]>x-100 and self.pos[0]<x+100 and self.pos[1]>y and self.pos[1]<y+200:
            if self.color==(0,0,255):
                self.color=(225,225,225)
                cv.line(img,[self.pos[0],self.pos[1]],[self.pos[0]+self.xspan,self.pos[1]-self.yspan],self.color,3)
                cv.line(img,[self.pos[0]+self.xspan,self.pos[1]-self.yspan],[self.pos[0]+self.xspan*2,self.pos[1]],self.color,3)
                cv.line(img,[self.pos[0]+self.xspan*2,self.pos[1]],[self.pos[0]+self.xspan,self.pos[1]+self.yspan],self.color,3)
                cv.line(img,[self.pos[0],self.pos[1]],[self.pos[0]+self.xspan,self.pos[1]+self.yspan],self.color,3)
    def turnOn(self,img):
        self.color=(0,0,255)
        cv.line(img,[self.pos[0],self.pos[1]],[self.pos[0]+self.xspan,self.pos[1]-self.yspan],self.color,3)
        cv.line(img,[self.pos[0]+self.xspan,self.pos[1]-self.yspan],[self.pos[0]+self.xspan*2,self.pos[1]],self.color,3)
        cv.line(img,[self.pos[0]+self.xspan*2,self.pos[1]],[self.pos[0]+self.xspan,self.pos[1]+self.yspan],self.color,3)
        cv.line(img,[self.pos[0],self.pos[1]],[self.pos[0]+self.xspan,self.pos[1]+self.yspan],self.color,3)

    def returnLocation(self):
        #returns the location of the button
        return (self.pos)
    def isOn(self):
        if self.color==(0,0,255):
            return True
    def isOff(self):
        if self.color==(225,225,225):
            return True
def matrix_creation(matrix):
    for x in range(4):
        for y in range(4):
            matrix.append(0)
def button_Object_creation(xspan,yspan,buttonList,Button):
    for x in range(4):
        for y in range(4):
            xpos=x*xspan + y*yspan +40
            ypos= - x*xspan  + y*yspan+200
            buttonList.append(Button((int(xpos),int(ypos)),xspan,yspan,"6",(225,225,225)))
            print(xpos,ypos)
def allOn():
    for ele in buttonList:
        if ele.isOff():
            return False
    return True


cap = cv.VideoCapture(0)
cap.set(3,680)
cap.set(4,480)
detector = htm.HandDetector(detectionCon=0.8,maxHands=1)
variablecount =0
routemap=[[15],[11,14,10],[13,9,5,6,7],[12,8,4,0,1,2,3]]
buttonList=[]
traversal =[]
width=80
height=80
xspan =40
yspan =40

Dict={0:6,1:10,2:13,3:15,4:3,5:7,6:11,7:14,8:1,9:4,10:8,11:12,12:0,13:2,14:5,15:9}


#temX=0
#temY=0
#dummy1=0
variablecount=0

state =0
t =time.time()
time.sleep(1)
t1=time.time()
matrix=[]
prev_matrix=[]
sending_matrix=[]
matrix_creation(sending_matrix)
matrix_creation(matrix)
matrix_creation(prev_matrix)
print(prev_matrix[5])
elementalList=[]
Displaylocation=[]
time_matrix=[]
for _ in range(16):
    time_matrix.append(0)
button_Object_creation(xspan,yspan,buttonList,Button)
#valueList=["0","1","2","3","4","5"]
state=1


def runner(t,prev_matrix,sending_matrix):
    while True:
        success,img = cap.read()
        #print(success)
        img=cv.flip(img,1)
        hands,img=detector.findHands(img)
        for button in buttonList:
            button.draw(img)
        if hands:
            lmList = hands[0]['lmList']
            x,y,z=lmList[8]
            e18=lmList[18]
            e20=lmList[20]
            e19=lmList[19]
            e16=lmList[16]
            e10=lmList[10]
            e12=lmList[12]
            e6=lmList[6]
            e8=lmList[8]
            e2=lmList[2]
            e4=lmList[4]
            #cv.line(img, (x-50, y), (x+50, y), (255, 0, 255), 3)
            #cv.line(img, (x-50, y), (x-50, y+100), (255, 0, 255), 3)
            #cv.line(img, (x-50, y+100), (x+50, y+100), (255, 0, 255), 3)
            #cv.line(img, (x+50, y), (x+50, y+100), (255, 0, 255), 3)
            
            for i,button in enumerate(buttonList):
            
                '''if (loli.poseChecker(e18,e20,e19,e16,e10,e12,e6,e8,e2,e4) and state ==0) :
                        
                        for ele in routemap:
                                
                                    
                            for buttLoc in ele:
                                buttonList[buttLoc].turnOn()
                                
                            for i in range(len(matrix)):
                                if buttonList[i].isOn():

                                    matrix[Dict[i]]=1
                    
                                else:
                                    matrix[Dict[i]]=0
                            
                            time.sleep(1)
                            cv.imshow("image",img)
                            cv.waitKey(1)
                            led.sendData(matrix)
                        state =1       
                            
                        for button in buttonList:
                            button.draw(img)
                        cv.imshow("image",img)
                        cv.waitKey(1)'''
                print(lmList[8])
                if lmList[8][1]<lmList[6][1] and lmList[12][1]<lmList[10][1] and lmList[16][1]<lmList[14][1]:
                    t=time.time() 
                    # z1=
                    # if(time)
                elif lmList[8][1]<lmList[6][1] and lmList[12][1]<lmList[10][1] and lmList[16][1]<lmList[14][1]: 
                    button.Activation(x,y,img)
                elif lmList[8][1]>lmList[6][1] and lmList[12][1]>lmList[10][1] and lmList[16][1]>lmList[14][1] :
                    
                
                    button.deActivation(x,y,img)
                    state =0
            for i in range(len(matrix)):
                if buttonList[i].isOn():

                    matrix[Dict[i]]=1
                    
                else:
                    matrix[Dict[i]]=0
            '''
            if time.time()-t>=0.1:
                sending_matrix=[]
                matrix_creation(sending_matrix)
                #print(f"current version{time.time()} matrix is {matrix}")
                #print(f"current version{time.time()} matrix is {prev_matrix}")
                for i in range(len(matrix)):
                    if matrix[i]>prev_matrix[i]:
                        sending_matrix[i]=1
                    elif matrix[i]<prev_matrix[i]:
                        sending_matrix[i]=2
                    elif matrix[i]==prev_matrix[i] and matrix[i]==1:
                        sending_matrix[i]=3
                    elif matrix[i]==prev_matrix[i] and matrix[i]==0:
                        sending_matrix[i]=0
                prev_matrix=matrix.copy()
                
                t=time.time()
                msg= str(sending_matrix)
                message = msg.encode(FORMAT)
                msg_length=len(message)
                sent_length= str(msg_length).encode(FORMAT)
                sent_length+=b' '*(HEADER- len(sent_length))
                client.send(sent_length)
                client.send(message)
'''

                        
                

               


                
            
            #fh=open('demo.txt','w+')
            #content=str(matrix)
            #fh.write(content)
            #fh.close()
            #print(content)
            #file = open("demo.txt", "r")
            #content = fh.read()
            #print("\nContent in file1.txt:\n", content)
            #fh.close()




                        
        # else:
        #     msg= str(sending_matrix)
        #     message = msg.encode(FORMAT)
        #     msg_length=len(message)
        #     sent_length= str(msg_length).encode(FORMAT)
        #     sent_length+=b' '*(HEADER- len(sent_length))
        #     client.send(sent_length)
        #     client.send(message)

        
        
        cv.imshow("image",img)
        cv.waitKey(1)
runner(t,prev_matrix,sending_matrix)
