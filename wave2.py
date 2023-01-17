import useful_functions
import arduino_sender
from time import sleep
wave_list=[[0],[4,1],[8,5,2],[12,9,6,3],[13,10,7],[14,11],[15]]
wave_list_rightToLeft=[[15],[14,11],[13,10,7],[12,9,6,3],[8,5,2],[1,4],[0]]
wave_list_topToBottom=[[12],[8,13],[4,9,14],[0,5,10,15],[1,6,11],[2,7],[3]]
wave_list_bottomToTop=[[3],[2,7],[1,6,11],[0,5,10,15],[4,9,14],[8,13],[12]]
amplitude_list=[0,10,20,30,50,70,100]
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
def correct_value_passer(arr,amplitude_list,i):
    for x in range(len(arr)):
        arr[x]=amplitude_list[(i+x)%7]
    
    
    return arr
def matrix_filler(arr,matrix,dict,wave_list):
    for x,array in enumerate(wave_list):
        for ele in array:
            matrix[dict[ele]]=arr[x]
while True:
    i+=1
    current_wave_value=correct_value_passer(current_wave_value,amplitude_list,i)
    
    matrix_filler(current_wave_value,matrix,Dict,wave_selector[j])
    arduino_sender.sendData(matrix)
    print(matrix)
    if i>20:
        i=0
        j+=1
        j=j%4
