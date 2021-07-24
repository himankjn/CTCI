def flipbits(n,m):
    count=0
    while(n!=0 or m!=0):
        count+=(n&1 ^ m&1)
        n=n>>1 
        m=m>>1
    return count

print(flipbits(29,15))