def ButArr2Mat(i):
    return(i%15,int(i/15))
def ButMat2Arr(x,y):
    return(x + y*15)
def viable(i):
    if(0<=i<150):
        return True