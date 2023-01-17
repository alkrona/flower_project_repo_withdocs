import cv2 as cv
class Button:
    def __init__(self,pos,xspan,yspan,value,isactive,color):
        self.pos=pos
        self.xspan=xspan
        self.yspan=yspan
        self.value=value
        self.isactive=isactive
        self.color=color
        
        state_Dict={}
        for i in range(21):
            if 10*i>100:
                state_Dict[i]=200-10*i
            else :
                state_Dict[i]=10*i
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
            return True
        else:
            self.isactive=0
            return False
            
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
        for i in range(21):
            if 10*i>100:
                state_Dict[i]=200-10*i
            else :
                state_Dict[i]=10*i
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
    def astroid_activation(self,x,y,img):
        #cv.line(img,[self.pos[0],self.pos[1]],[self.pos[0]+self.xspan,self.pos[1]-self.yspan],self.color,3)
        #cv.line(img,[self.pos[0]+self.xspan,self.pos[1]-self.yspan],[self.pos[0]+self.xspan*2,self.pos[1]],self.color,3)
        #cv.line(img,[self.pos[0]+self.xspan*2,self.pos[1]],[self.pos[0]+self.xspan,self.pos[1]+self.yspan],self.color,3)
        #cv.line(img,[self.pos[0],self.pos[1]],[self.pos[0]+self.xspan,self.pos[1]+self.yspan],self.color,3)
        # bax = bx - ax
        # bay = by - ay
        # dax = dx - ax
        # day = dy - ay

        # if ((x - ax) * bax + (y - ay) * bay < 0.0) return false
        # if ((x - bx) * bax + (y - by) * bay > 0.0) return false
        # if ((x - ax) * dax + (y - ay) * day < 0.0) return false
        # if ((x - dx) * dax + (y - dy) * day > 0.0) return false
        if self.pos[0]<x and (self.pos[0] + self.xspan)>x  and self.pos[1]<y and self.pos[1]+ self.yspan>y:
            self.isactive=1
            self.value=100
            return True
        else:
            self.isactive=0
            self.value=0
            return False
            

