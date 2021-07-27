def search(A,x):
    mididx=find_smallest(A,0,len(A)-1)
    left=binary_s(A,0,mididx-1,x)
    right=binary_s(A,mididx,len(A)-1,x)
    if(left==-1 and right==-1):
        print("doesnt exist")
        return
    if(left==-1):
        return right
    return left
def binary_s(A,low,high,x):
    if(low>high):
        return -1
    mid=(low+high)//2
    if(A[mid]<x):
        return binary_s(A,mid+1,high,x)
    elif(A[mid]>x):
        return binary_s(A,low,mid-1,x)
    else:
        return mid
def find_smallest(A,low,high):
    if(low==high):
        return low
    
    mid=(low+high)//2
    if(A[mid]<A[high]):
        return find_smallest(A,low,mid)
    else:
        return find_smallest(A,mid+1,high)
    

A=[15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
print(search(A,5))