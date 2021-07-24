import sys

class node:
    def __init__(self,v):
        self.data=v
        self.left=None
        self.right=None

class binary_tree:
    def __init__(self,root):
        self.root=root

    def check_balanced(self):
        root=self.root
        h=self.height(root)
        if(h==-sys.maxsize):
            print("unbalanced")
        else:
            print("balanced")
    def height(self,root):
        if(root is None):
            return -1

        lh=self.height(root.left)
        rh=self.height(root.right)
        
        #this is to propogate unbalance status up the stack
        #if tree is unbalanced at left or right node just send the info up the tree
        #this is the only way to break out of recursion. that is to return error code up the stack by backtrack
        #alternatively use a class flag to indicate that we found unbalance.
        if(lh==-sys.maxsize):
            return -sys.maxsize
        if(rh==-sys.maxsize):
            return -sys.maxsize

        if(abs(lh-rh)>1):
            return -sys.maxsize
            #or self.flag=False
        return 1+max(lh,rh)
  

root=node(2)
root.left=node(4)
#root.right=node(6)
root.left.left=node(9)
root.left.right=node(8)
#root.right.left=node(3)
#root.right.right=node(1)
#root.right.right.right=node(10)
#root.right.right.right.right=node(11)
Tree=binary_tree(root)
Tree.check_balanced()