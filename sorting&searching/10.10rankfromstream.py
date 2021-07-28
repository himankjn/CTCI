"""
: Imagine you are reading in a stream of integers. Periodically, you wish to be able 
to look up the rank of a numberx (the number of values less than or equal to x). lmplementthe data 
structures and algorithms to support these operations. That is, implement the method track ( int 
x), which is called when each number is generated, and the method getRankOfNumber(int 
x), which returns the number of values less than or equal to x (not including x itself). 
"""


class tracknums:
    def __init__(self):
        self.ranks={}
    
    def track(self,n):
        maxkey=0
        for key in self.ranks.keys():
            if(key<=n and key>maxkey):
                maxkey=key
        if(maxkey==0):
            self.ranks[n]=0
        else:
            self.ranks[n]=self.ranks[maxkey]+1

        for key in self.ranks.keys():
            if(key>n):
                self.ranks[key]+=1
    
    
    def getrank(self,n):
        return self.ranks[n]
                    

nums=tracknums()
N=[5, 1, 4, 4, 5, 9, 7, 13, 3]
for n in N:
    nums.track(n)

print(nums.getrank(4))