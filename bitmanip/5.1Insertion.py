"""
Insertion: You are given two 32-bit numbers, N and M, and two bit positions, i and
j. Write a method to insert M into N such that M starts at bit j and ends at bit i. You
can assume that the bits j through i have enough space to fit all of M. That is, if
M = 10011, you can assume that there are at least 5 bits between j and i. You would not, for
example, have j = 3 and i = 2, because M could not fully fit between bit 3 and bit 2.
EXAMPLE
Input:
N
10000000000, M
Output: N = 10001001100
"""

N=1024 #1024
M=19 #10 
j=6
i=2

def insert(N,M,j,i):
    clearmask=~((1<<(j-i+1))-1<<i)
    N=N&clearmask

    mask=M<<i
    return N|mask

print(insert(N,M,j,i))