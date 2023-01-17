import useful_functions
import cv2 as cv
import handmodule as htm
import mediapipe as mp
import time
import raindrop_pattern_generator
import arduino_sender

z_axis_values=[]
useful_functions.list_initializator(z_axis_values,20)
time_of_action=[]
useful_functions.list_initializator(time_of_action,20)
cap = cv.VideoCapture(1)
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
array_var=0
z_max=0
z_min=0
b_List=[2,3,6,7]
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
i=0
useful_functions.list_initializator(matrix,16)
class Button:
    def __init__(self,pos,xspan,yspan,value,isactive,color):
        self.pos=pos
        self.xspan=xspan
        self.yspan=yspan
        self.value=value
        self.isactive=isactive
        self.color=color
        
        state_Dict={}
        for i in range(41):
            if 5*i>100:
                state_Dict[i]=200-5*i
            else :
                state_Dict[i]=5*i
    def draw(self,img):
        #cv.polylines(img, [[self.pos[0],self.pos[1]],[self.pos[0]+self.xspan,self.pos[1]-self.yspan],[self.pos[0]+self.xspan*2,self.pos[1]],[self.pos[0]+self.xspan,self.pos[1]+self.yspan]],True, self.color, cv.FILLED)
        #cv.polylines(img, [[self.pos[0],self.pos[1]],[self.pos[0]+self.xspan,self.pos[1]-self.yspan],[self.pos[0]+self.xspan*2,self.pos[1]],[self.pos[0]+self.xspan,self.pos[1]+self.yspan]],True, (50,50,50), 3)
        cv.line(img,[self.pos[0],self.pos[1]],[self.pos[0]+self.xspan,self.pos[1]-self.yspan],self.color,3)
        cv.line(img,[self.pos[0]+self.xspan,self.pos[1]-self.yspan],[self.pos[0]+self.xspan*2,self.pos[1]],self.color,3)
        cv.line(img,[self.pos[0]+self.xspan*2,self.pos[1]],[self.pos[0]+self.xspan,self.pos[1]+self.yspan],self.color,3)
        cv.line(img,[self.pos[0],self.pos[1]],[self.pos[0]+self.xspan,self.pos[1]+self.yspan],self.color,3)
        
        #cv.putText(img,self.value,(self.pos[0]+40,self.pos[1]+60),cv.FONT_HERSHEY_COMPLEX_SMALL,2,(50,50,50),2)
    
    def Activation(self,x,y,img):
        if self.pos[0]>x-50 and self.pos[0]<x+50 and self.pos[1]>y and self.pos[1]<y+100:
            self.isactive=1
            
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
    def is_active(self):
        if self.isactive==1:
            return True
        else :
            return False
    def state_controller(self):
        if self.value>=40:
            self.value=0
            self.isactive=0
        else :
            self.value+=1
    def current_value(self):
        state_Dict={}
        for i in range(41):
            if 5*i>100:
                state_Dict[i]=200-5*i
            else :
                state_Dict[i]=5*i
        return(state_Dict[self.value])
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
def button_Object_creation(xspan,yspan,buttonList,Button):
    for x in range(4):
        for y in range(4):
            xpos=x*xspan + y*yspan +200
            ypos= - x*xspan  + y*yspan+300
            buttonList.append(Button((int(xpos),int(ypos)),xspan,yspan,0,0,(225,225,225)))
            print(xpos,ypos)

buttonList=[]

    
button_Object_creation(xspan,yspan,buttonList,Button)


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
            
            
            
            
            
               
                
            
        if True :
            for i,button in enumerate(buttonList):
                button.Activation(x,y,img)
                state=0
    matrix=[]
    useful_functions.list_initializator(matrix,16)
    for i,ele1 in enumerate(buttonList):
                    
        if ele1.is_active():
                        
            ele1.state_controller()
        Dict={0:6,1:10,2:13,3:15,4:3,5:7,6:11,7:14,8:1,9:4,10:8,11:12,12:0,13:2,14:5,15:9}
        matrix[Dict[i]]=ele1.current_value()
            
    arduino_sender.sendData(matrix)
        #print(matrix)
                
                   
           
           

               


                
            
    cv.imshow("image",img)
    cv.waitKey(1)


