import arduino_sender
import time
matrix=[]
matrix2=[]
for _ in range(16):
    matrix.append(100)
    matrix2.append(0)
while True:
    arduino_sender.sendData(matrix)
    time.sleep(.5)
    arduino_sender.sendData(matrix2)
    time.sleep(.5)