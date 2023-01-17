import arduino_sender
def circle_pattern_generator():
    outer_circle= [0,4,8,12,13,14,15,11,7,3,2,1]
    inner_circle=[5,9,10,6]
    outer_circle_startpoints=[]
    outer_circle_middlepoints=[]
    outer_circle_endpoints=[]
    inner_circle_startpoints=[]
    inner_circle_middlepoints=[]
    inner_circle_endpoints=[]
    Dict={0:6,1:10,2:13,3:15,4:3,5:7,6:11,7:14,8:1,9:4,10:8,11:12,12:0,13:2,14:5,15:9}
    for i in range(len(outer_circle)):
        outer_circle_startpoints.append(i*30)
        outer_circle_middlepoints.append(i*30 + 100)
        outer_circle_endpoints.append(i*30 + 200)
    for i in range(len(inner_circle)):
        inner_circle_startpoints.append(i*30)
        inner_circle_middlepoints.append(i*30 + 100)
        inner_circle_endpoints.append(i*30 + 200)
    i=0
    j=0
    matrix=[]
    for _ in range(16):
        matrix.append(0)
    b=1
    k=0
    while b==1:
        
        i+=12
        j+=4
        for x in range(len(outer_circle)):
            if i>outer_circle_startpoints[x] and i<outer_circle_middlepoints[x]:
                matrix[Dict[outer_circle[x]]]=i-outer_circle_startpoints[x]
            elif i>outer_circle_middlepoints[x] and i<outer_circle_endpoints[x]:
                matrix[Dict[outer_circle[x]]]=200-(i-outer_circle_startpoints[x])
            else :
                matrix[Dict[outer_circle[x]]]=0
        for x in range(len(inner_circle)):
            if j>inner_circle_startpoints[x] and j<inner_circle_middlepoints[x]:
                matrix[Dict[inner_circle[x]]]=j-inner_circle_startpoints[x]
            elif j>inner_circle_middlepoints[x] and j< inner_circle_endpoints[x]:
                matrix[Dict[inner_circle[x]]]=200-(j-inner_circle_startpoints[x])
            else:
                matrix[Dict[inner_circle[x]]]=0
        arduino_sender.sendData(matrix)
        if i>530:
            i=i%530
            k+=1
        if j>290:
            j=j%290
        if k>4:
            b=1
            break
def main():
    circle_pattern_generator()
if __name__ == "__main__":
    main()  