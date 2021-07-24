def flip(n,i):
    mask=1<<i
    return n^mask

def nextnum(n):
    orig=n
    idx=0
    numones=0

    while(n&1!=1):
        idx+=1
        n=n>>1
    while(n&1!=0):
        numones+=1
        idx+=1
        n=n>>1
    
    orig=flip(orig,idx)
    mask=~((1<<idx)-1)
    orig=orig&mask
    orig=orig|((1<<numones-1)-1)
    return orig

 

def prevnum(n):
    orig=n
    idx=0
    numones=0

    while(n&1!=0):
        idx+=1
        n=n>>1
        numones+=1
    while(n&1!=1):
        idx+=1
        n=n>>1
    
    orig=flip(orig,idx)
    mask=-1<<(idx)
    orig=orig&mask

    
    orig=orig|(((1<<numones+1)-1)<<(idx-numones-1))
    return orig


#13948->#13967
print(nextnum(13948))
print(prevnum(13948))
