from mod import SerialObject
import time
import concurrent.futures
import asyncio
arduino = SerialObject()

time.sleep(3)




def sendData(matrix):
    
    #print(matrix)           
    arduino.sendData(matrix)    