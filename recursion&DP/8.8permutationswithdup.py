#O(n!) where n is no. of unique ele

def perm(s):
    count={}
    for c in s:
        count[c]=count.get(c,0)+1
    allperms=[]

    permutil(count,"",allperms)
    print(allperms)

def permutil(count,prefix,allperms):
    
    #if hashmap count is over then add current prefix to list of perms
    flag=True
    for k,v in count.items():
        if v!=0:
            flag=False
            break

    if(flag):
        allperms.append(prefix)
        return
    
    for k,v in count.items():
        if v!=0:
            count[k]-=1
            permutil(count,prefix+k,allperms)
            count[k]+=1

s="aabbc"
perm(s)