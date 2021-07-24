
def magicindex(arr):
    l=0
    r=len(arr)-1


    while(l<=r):
        mid=(l+r)//2
        if(arr[mid]>mid):
            r=mid-1
        elif(arr[mid]<mid):
            l=mid+1
        else:
            return mid
    
    return -1


#in case of duplicates
def search(arr,l,r):

        if(l>r):
            return -1

        mid=(l+r)//2
        if(arr[mid]==mid):
            return mid
        elif(arr[mid]>mid):
            #search whole left and on right only from mid value index
            left=search(arr,l,mid-1)
            if(left>=0):
                return left
            right= search(arr,arr[mid],r)
            if(right>=0):
                return right
        else:
            #search whole right,left only till midval
            left=search(arr,mid+1,r)
            if(left>=0):
                return left
            right= search(arr,l,arr[mid])
            if(right>=0):
                return right
        


arr=[-4,2,3,3,3,9]#ans=3
print(search(arr,0,len(arr)-1))
#print(magicindex(arr))

