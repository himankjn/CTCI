def swapbits(n):
    #101010101010....
    return  ( (n&0xaaaaaaaa)>>1 | (n&0x55555555)<<1)

print(swapbits(5))
