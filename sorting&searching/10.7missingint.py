#note using every bit we can represent one integer.
#hence one byte can represent 8 integers.
#map int to bit. i.e int 0 to 7-> byte 1. 

def missingint(N):
    bits=[0]*(len(N)//8+1)
    for n in N:
        byteno=n//8
        bitno=n%8
        bits[n//8]=bits[n//8] | 1<<bitno
    
    for j in range(len(bits)):
        for i in range(0,8):
            if bits[j]&(1<<i)==0:
                print(j*8+i)


missingint(range(511)+range(512,1024))
