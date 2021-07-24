#O(n!)
def perm(s,prefix,allperms):


    if(not s):
        allperms.append(prefix)
        return
    for i in range(0,len(s)):
        remaining=s[:i]+s[i+1:]
        char=s[i]
        perm(remaining,prefix+char,allperms)



allperms=[]
s="abcd"
perm(s,"",allperms)
print(allperms)


