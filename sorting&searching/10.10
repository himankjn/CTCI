#O(2^(M+N))
def search(M,r,c,x):
    rows=len(M)
    cols=len(M[0])

    if(r>=rows or c>=cols):
        return -1
    if(x==M[r][c]):
        return (r,c)
    elif(x<M[r][c]):
        return -1
    elif(x>M[r][c]):
        one=search(M,r+1,c,x)
        two=search(M,r,c+1,x)
        if(one==-1 and two==-1):
            return -1
        elif(one==-1):  
            return two
        else:
            return one




#O(logN*logM)

def searcheff(M,x):
    #start top right. if x is smaller then do col-- else if x is larger then do r++
    
    r=0
    c=len(M[0])-1
    while(r<len(M) and c>=0):
        if(x==M[r][c]):
            return (r,c)
        elif(x<M[r][c]):
            c-=1
        else:
            r+=1
    
    return -1

M=[[15,20,40,85],[20,35,80,95],[30,55,95,105],[40,80,100,120]]
print(searcheff(M,80))