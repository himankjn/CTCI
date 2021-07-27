#O(logn+logn)= O(logn)

def at(A,i):
    if(i>=len(A)):
        return -1
    else:
        return A[i]
def search(A,x):
    idx=1
    while at(A,idx)!=-1 and at(A,idx)<x:
        idx*=2
    
    return binary_s(A,x,idx//2,idx)

def binary_s(A,x,low,high):
    while(low<=high):
        mid=(low+high)//2
        if(at(A,mid)>x or at(A,mid)==-1):
            high=mid-1
        elif(at(A,mid)<x):
            low=mid+1
        else:
            return mid
    return -1


A=[1, 3, 4, 5, 7, 10, 14]
print(search(A,4))