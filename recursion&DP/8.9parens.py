
def parens(n):
    allpar=[]
    parutil(n,n,"",allpar)
    return allpar

def parutil(open,closed,prefix,allpar):
    if(open==0 and closed==0):
        allpar.append(prefix)
    if open>0:
        parutil(open-1,closed,prefix+"(",allpar)
    if closed>open:
        parutil(open,closed-1,prefix+")",allpar)




#not so efficient implementation but easier logically
#par(4) =  for every p in par(3) insert () at beginning, after every '('
#also dont add duplicates by keeping track
#this method takes longer as it does extra work computing even duplicates
def genpar(n):
  return paren(n)
    

def paren(n):
    allpars=set()
    if(n==0):
        allpars.add("")
        return allpars

    for s in paren(n-1):
        for i in range(0,len(s)):
            if(s[i]=='('):
                allpars.add(s[:i+1]+'()'+s[i+1:])
        allpars.add('()'+s)

    return allpars

print(genpar(4))
