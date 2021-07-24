#using recursin O(n*2^n)
def subsets(A):
    if len(A)==0:
        return [[]]
    
    subset=subsets(A[:-1])
    a=subset[:] 
    
    for i in subset:
        a.append(i+[A[-1]])
    return a




#using combinatorics
#every element has two options of being in a subset. either present or abset. 1/0
#hence every subset of power set can be represented using a binary string of 1/0 indicating presence of an element

def subs(A):
    #generate all binary strings

    maxnum=pow(2,len(A)) #1<<len(A)
    #for every every string from 0 to 2^n if string&1 is true then add that index ele to subset
    subsets=[]
    for k in range(0,pow(2,len(A))):
        index=0
        subset=[]
        while k!=0:
            if k&1==1:
                #the ith index ele is in subset
                subset.append(A[index])
            index+=1
            k=k>>1
        subsets.append(subset)
    return subsets

A=['a','b','c']
print(subs(A))