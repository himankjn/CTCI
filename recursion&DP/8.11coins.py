def makechange(n):
    denom=[25,10,5,1]
    seen={}
    return numofways(n,denom,0,seen)
def numofways(n,denom,index,seen):   
    #begin with first denom(25)
    #include all possible number of it (0,1,2...) and for remaning amount recursively call for next denom(10)
    
    
    #base case. if we are denomination(penny=1) then only one possible way
    if(index==len(denom)-1):
        return 1
    totalways=0
    i=0
    while denom[index]*i<=n:
        remaining=n-denom[index]*i
        if(not seen.get((remaining,index+1),False)):
            seen[(remaining,index+1)]=numofways(remaining,denom,index+1,seen)
        totalways+=seen[(remaining,index+1)]
        i+=1
    return totalways


print(makechange(25))