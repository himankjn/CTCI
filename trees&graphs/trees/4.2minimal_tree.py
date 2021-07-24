class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class bst:
    def __init__(self,A):
        self.root=None
        self.A=A
    def minimal_tree(self):
        self.root=self.makebst(0,len(self.A)-1)

    def makebst(self,l,r):
        if(l>r):
            return None
        mid=(l+r)//2    
        cur_root=Node(self.A[mid])
        cur_root.left=self.makebst(l,mid-1)
        cur_root.right=self.makebst(mid+1,r)
        return cur_root

A=[0,1,2,3,4]

tree=bst(A)
tree.minimal_tree()

print(tree.root.left.val)
