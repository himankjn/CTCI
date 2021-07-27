def search(L,x):
    return binarys(L,x,0,len(L)-1)
def binarys(L,x,low,high):
    if(low>high):
        return -1
    mid=(low+high)//2
    if(L[mid]==x):
        return mid
    elif(L[mid]==""):
        left=binarys(L,x,low,mid-1)
        right=binarys(L,x,mid+1,high)
        if(left==-1 and right==-1):
            return -1
        elif(left==-1):
            return right
        else:
            return left
    elif(L[mid]<x):
        return binarys(L,x,mid+1,high)
    elif(L[mid]>x):
        return binarys(L,x,low,mid-1)

L=["at","","" , "" , "" ,"ball","","car",
"" , "" ,"dad","" ,""]
print(search(L,"at"))