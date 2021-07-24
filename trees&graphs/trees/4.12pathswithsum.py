class node:
    def __init__(self,v):
        self.v=v
        self.left=None
        self.right=None

class Tree:
    def __init__(self,root):
        self.root=root
    #O(NlogN)
    def pathsum(self,finalsum):
        root=self.root
        return self.findallpathsum(root,finalsum)
    
    def findallpathsum(self,root,finalsum):
        
        totalpaths=0

        #paths starting with sum from root
        count=[0]
        self.pathsumhelp(root,0,finalsum,count)
        totalpaths+=count[0]

        leftpaths=rightpaths=0
        if(root.left):
            leftpaths=self.findallpathsum(root.left,finalsum)
        if(root.right):
            rightpaths=self.findallpathsum(root.right,finalsum)

        totalpaths=totalpaths+leftpaths+rightpaths
        return totalpaths


        
    def pathsumhelp(self,root,cur_sum,finalsum,count):
        if(root is None):
            return 
        if(root.v+cur_sum==finalsum):
            count[0]+=1
        
        self.pathsumhelp(root.left,root.v+cur_sum,finalsum,count)
        self.pathsumhelp(root.right,root.v+cur_sum,finalsum,count)
    

    #O(N)
    def pathsum2(self,s):
        root=self.root
        runningsum={}
        runningsum[0]=1
        count=[0]
        cursum=0
        self.pathsum2help(root,cursum,s,runningsum,count)
        return count[0]
    def pathsum2help(self,root,cursum,s,runningsum,count):
            if root is None:
                return
            cursum+=root.v
            if(runningsum.get(s-cursum,False)):
                count[0]+=runningsum[s-cursum]

            runningsum[cursum]=runningsum.get(cursum,0)+1

            self.pathsum2help(root.right,cursum,s,runningsum,count)
            self.pathsum2help(root.left,cursum,s,runningsum,count)
            runningsum[cursum]=runningsum[cursum]-1

root=node(6)
root.left=node(-1)
root.left.left=node(3)
root.left.right=node(2)
root.left.right.left=node(6)
root.left.right.left.left=node(-5)
root.left.right.left.right=node(3)
root.left.right.left.right.right=node(-1)
root.left.right.right=node(1)
root.right=node(2)
root.right.right=node(0)

T=Tree(root)

print(T.pathsum2(8))