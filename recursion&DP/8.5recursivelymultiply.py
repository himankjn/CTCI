#O(log(n))
#multiply n and m using recursion and bit shifting

#8*9=  (4*9) *2
#4*9= (2*9) *2
#2*9= (1*9)*2
#1*9= 9
def recmul(n,m):
    if(n==1):
        return m
    if(m==1):
        return n
    
    if n&1==1:
        #odd n case
        return (recmul(n>>1,m)<<1)+m
    else:
        #even n case
        return recmul(n>>1,m)<<1

print(recmul(5,9))
