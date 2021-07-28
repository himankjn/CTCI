"""
In an array of integers, a "peak" is an element which is greater than or equal to 
the adjacent integers and a "valley" is an element which is less than or equal to the adjacent integers. For example, in the array {5, 8, 6, 2, 3, 4, 6}, {8, 6} are peaks and {5, 2} are valleys. Given an array 
of integers, sort the array into an alternating sequence of peaks and valleys.
"""
#O(nlogn)
#Note. for every triplet the order is small<=medium<=large. just swap last two to create peak.
#note if peaks are inorder then so will the valleys automatically.
def alternate(A):
    A.sort()
    i=1
    j=len(A)-1

    while(i<=j):
        swap(A,i,i-1)
        i+=2
    return A

def swap(A,i,j):
    temp=A[i]
    A[i]=A[j]
    A[j]=temp



#O(n) without sorting
#Note: we dont need to sort. we just take care of every triplet. such that largest of the three numbers is in the middle and move on to next triplet.
#1 3 2 4 5  first take care of (1,3,2) then move to (2,4,5) and so on.
def PandV(A):
    i=1
    while(i<len(A)):
        prev=A[i-1]
        cur=A[i]
        next=A[i+1]

        if(cur<next or cur<prev):
            if(prev>next):
                idx=i-1
            else:
                idx=i+1
            swap(A,i,idx)
        i+=2
    return A
def swap(A,i,j):
    temp=A[i]
    A[i]=A[j]
    A[j]=temp

A=[5, 1, 4, 4, 5, 9, 7, 13, 3]
print(PandV(A))