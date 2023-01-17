import useful_functions
import arduino_sender
import pythonToFirebasesender
from time import sleep
wave_list=[[0],[4,1],[8,5,2],[12,9,6,3],[13,10,7],[14,11],[15]]
wave_list_rightToLeft=[[15],[14,11],[13,10,7],[12,9,6,3],[8,5,2],[1,4],[0]]
wave_list_topToBottom=[[12],[8,13],[4,9,14],[0,5,10,15],[1,6,11],[2,7],[3]]
wave_list_bottomToTop=[[3],[2,7],[1,6,11],[0,5,10,15],[4,9,14],[8,13],[12]]
amplitude_list=[0,10,20,30,50,70,100,70,50,30,20,10]
wave_selector=[]
wave_selector.append(wave_list)
wave_selector.append(wave_list_rightToLeft)
wave_selector.append(wave_list_topToBottom)
wave_selector.append(wave_list_bottomToTop)
Dict={0:6,1:10,2:13,3:15,4:3,5:7,6:11,7:14,8:1,9:4,10:8,11:12,12:0,13:2,14:5,15:9}
current_wave_value=[]
matrix=[]
useful_functions.list_initializator(current_wave_value,7)
useful_functions.list_initializator(matrix,16)
i=0
j=0
def correct_value_passer(arr,i):

    
    if i<40:
        arr[0]=i
    elif i>=40 and i<80:
        arr[0]=80 -i
    elif i>=80:
        arr[0]=0
    if i>=40 and i<=160:
        if i<100:
            arr[1]=i-40
        else:
            arr[1]=160-i
    if i<40 or i>160:
        arr[1]=0
    #wave 3
    if i>=60 and i<=220:
        if i<140:
            arr[2]=i-60
        else:
            arr[2]=220-i
    if i<60 or i>220:
        arr[2]=0
    #wave 4
    if i>=80 and i<=280:
        if i<180:
            arr[3]=i-80
        else:
            arr[3]=280-i
    if i<80 or i>280:
        arr[3]=0
    #wave 5
    if i>=120 and i<=280:
        if i<200:
            arr[4]=i-120
        else:
            arr[4]=280-i
    if i<120 or i>280:
        arr[4]=0
    #wave 6
    if i>=180 and i<=300:
        if i<240:
            arr[5]=i-180
        else:
            arr[5]=300-i
    if i<180 or i>300:
        arr[5]=0
    #wave 7
    if i>=240 and i<=320:
        if i<280:
            arr[6]=i-240
        else:
            arr[6]=320-i
    if i<240 or i>320:
        arr[6]=0
    return arr
def matrix_filler(arr,matrix,dict,wave_list):
    for x,array in enumerate(wave_list):
        for ele in array:
            matrix[dict[ele]]=arr[x]
def main_wave_generator(j,speed=10): 
    i=0
    current_wave_value=[]
    matrix=[]
    useful_functions.list_initializator(current_wave_value,7)
    useful_functions.list_initializator(matrix,16)
    wave_list=[[0],[4,1],[8,5,2],[12,9,6,3],[13,10,7],[14,11],[15]]
    wave_list_rightToLeft=[[15],[14,11],[13,10,7],[12,9,6,3],[8,5,2],[1,4],[0]]
    wave_list_topToBottom=[[12],[8,13],[4,9,14],[0,5,10,15],[1,6,11],[2,7],[3]]
    wave_list_bottomToTop=[[3],[2,7],[1,6,11],[0,5,10,15],[4,9,14],[8,13],[12]]
    amplitude_list=[0,10,20,30,50,70,100,70,50,30,20,10]
    wave_selector=[]
    wave_selector.append(wave_list)
    wave_selector.append(wave_list_rightToLeft)
    wave_selector.append(wave_list_topToBottom)
    wave_selector.append(wave_list_bottomToTop)
    Dict={0:6,1:10,2:13,3:15,4:3,5:7,6:11,7:14,8:1,9:4,10:8,11:12,12:0,13:2,14:5,15:9}           
    while i<320:
        i+=speed
        current_wave_value=correct_value_passer(current_wave_value,i)
        
        matrix_filler(current_wave_value,matrix,Dict,wave_selector[j])
        #print(j,"wave sent")
        arduino_sender.sendData(matrix)
        pythonToFirebasesender.firesender(matrix)
    
