import arduino_sender
import time
def circular_pattern_generator():
    hands=[[12,9,6,3],[13,9,5,1],[14,10,6,2],[15,10,5,0],[8,9,10,11],[4,5,6,7],[14,10,6,2],[13,9,5,1],[15,10,5,0],[4,5,6,7],[8,9,10,11]]
    clock_hands=[[12,9,6,3],[13,9,6,2],[14,10,5,1],[15,10,5,0],[11,10,5,4],[7,6,9,8],[3,6,9,12],[2,6,9,13],[1,5,10,14],[0,5,10,15],[4,5,10,11],[8,9,6,7]]
    Dict={0:6,1:10,2:13,3:15,4:3,5:7,6:11,7:14,8:1,9:4,10:8,11:12,12:0,13:2,14:5,15:9}

    def value_assigner(i):
        
        if i<100:
            return i
        if i>=100 and i<=200:
            return 200-i
        else :
            return 0
    i=0
    j=0
    matrix =[]
    k=0
    for _ in range(16):
        matrix.append(0)
        
    while k<2000:
        
        if i<=200:
            i+=12
            k+=12
            for ele in clock_hands[j]:
                matrix[Dict[ele]] = value_assigner(i)
        else:
            j=(j+1)%12
            i=0
        '''
        for i in range(16):
            for j in range(16):
                if j==i:
                    matrix[Dict[j]]=100
                else:
                    matrix[Dict[j]]=0
            '''
        arduino_sender.sendData(matrix)
        
def main():
    circular_pattern_generator()
if __name__ == "__main__":
    main()  
        
