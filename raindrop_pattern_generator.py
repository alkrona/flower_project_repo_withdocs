import arduino_sender
import time
def converter(num):
    if num<=100:
        return num
    if num>100:
        return 200-num
def allocater(matrix,set1,set2,set3,val1,val2,val3,Dict):
    mat =[]
    for _ in  range(16):
         mat.append(0)
    for i in range(len(mat)):
        if i in set1:
             mat[Dict[i]]=val1
        if i in set2:
             mat[Dict[i]]=val2
        if i in set3:
            mat[Dict[i]]=val3
    #print(mat)
    return(mat)
def raindrop():
    set1=[6]
    set2=[1,5,9,2,10,3,7,11]
    set3=[0,4,8,12,13,14,15]
    Dict={0:6,1:10,2:13,3:15,4:3,5:7,6:11,7:14,8:1,9:4,10:8,11:12,12:0,13:2,14:5,15:9}
    matrix=[]
    for _ in range(16):
        matrix.append(0)
    matrix[Dict[6]]=33
    m1=matrix.copy()




    arduino_sender.sendData(m1)
    
    # while True:
    #     for ele in mlist:
    #         #print(ele)
    #         final.sendData(ele)
    #         time.sleep(0.2)
    i=0
    j=0
    k=0
    t=time.time()
    while time.time()<t+6:
        i+=4
        if i>=30:
            j+=4
        if i>=60:
            k+=4
        m=allocater(matrix,set1,set2,set3,converter(i%200),converter(j%200),converter(k%200),Dict)
        arduino_sender.sendData(m)
    while i!=0 or j !=0 or k!=0:
        if i>=4:
            i-=4
        if j>=4:
            j-=4
        if k>=4:
            k-=4
        m=allocater(matrix,set1,set2,set3,converter(i%200),converter(j%200),converter(k%200),Dict)
        arduino_sender.sendData(m)
        #print("success")
        #print(m)
def main():
    raindrop()
if __name__ == "__main__":
    main()