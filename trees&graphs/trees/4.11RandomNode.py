from random import randint

class node:
    def __init__(self,v):
        self.v=v
        self.parent=None
        self.left=None
        self.right=None
        self.size=1
    
class Tree:
    def __init__(self):
        self.root=None
    def insert(self,v):
        self.root=self.inserthelper(self.root,v)
        
    def inserthelper(self,root,v):
        if root is None:
            return node(v)
        root.size+=1
        if v<root.v:
            root.left=self.inserthelper(root.left,v)
            root.left.parent=root
        elif v>root.v:
            root.right=self.inserthelper(root.right,v)
            root.right.parent=root
        return root
    

    def delete(self,v):
        root=self.root
        self.root=self.deletehelper(root,v)
    
    def deletehelper(self,root,v):
        root.size-=1
        if root.v==v:
            if root.left is None and root.right is None:
                return None
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            if root.right:
                x=self.inordersucc(root)
                root.v=x.v
                root.right=self.deletehelper(root.right,x.v)
                #copy x content to root and delete x

        elif v<root.v:
            root.left=self.deletehelper(root.left,v)
        elif v>root.v:
            root.right=self.deletehelper(root.right,v)
        return root
    def inordersucc(self,root):
        root=root.right
        while(root.left):
            root=root.left
        return root
    def randomnode(self):
        root=self.root
        print(self.getrandomnode(root).v)
    def getrandomnode(self,root):
        if root.left is None:
            leftsize=0
        else:
            leftsize=root.left.size
        
        #random number from 1 to size
        randomnum=randint(1,root.size)

        if randomnum==leftsize+1:
           return root
        elif(randomnum<=leftsize):
            return self.getrandomnode(root.left)
        else:
            return self.getrandomnode(root.right)
        
        



T=Tree()
T.insert(9)
T.insert(10)
T.insert(1)
T.insert(3)


