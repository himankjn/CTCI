#Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the
#end to hold B. Write a method to merge B into A in sorted order

def shift(A,idx):
    if(idx==len(A)-1):
        return
    shift(A,idx+1)
    A[idx+1]=A[idx]
    
def sortedmerge(A,B):
    cur=0
    idxA=0
    idxB=0

    while(idxA<len(A) and idxB<len(B)):
        if(A[idxA]<B[idxB]):
            idxA+=1
        else:
            shift(A,idxA)
            A[idxA]=B[idxB]
            idxA+=1
            idxB+=1
   
A=[4,5,8,12,float('inf'),float('inf'),float('inf'),float('inf'),float('inf')]
B=[1,3,9,11,13]
sortedmerge(A,B)
print(A)