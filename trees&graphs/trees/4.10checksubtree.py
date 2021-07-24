class node:
    def __init__(self,v):
        self.v=v
        self.left=None
        self.right=None

class Tree:
    def __init__(self,root):
        self.root=root

    #is this root2 tree a subtree of this tree?
    def issubtree(self,root2):
        root1=self.root
        root2=root2
        #note: in case of duplicates in tree store all the nodes in which root2 is same as root1 and check identicality for all those.
        #now root1 points to the same value as root2
        root1=self.traverse(root1,root2)

        #now recursively check if trees are identical
        return self.isidentical(root1,root2)
    def isidentical(self,root1,root2):
        if(root1 is None and root2 is None):
            return True
        if(root1 is None or root2 is None):
            return False
        if(root1.v != root2.v):
            return False
        return self.isidentical(root1.left,root2.left) and self.isidentical(root1.right,root2.right)


    def traverse(self,root1,root2):
        if(root1 is None):
            return None

        if(root1.v==root2.v):
            return root1
        
        left=self.traverse(root1.left,root2)
        right=self.traverse(root1.right,root2)
        if(left is None):
            return right
        else:
            return left

root1=node(5)
root1.left=node(2)
root1.right=node(8)
root1.left.left=node(1)
root1.left.right=node(3)
root1.right.left=node(6)
root1.right.right=node(10)

root2=node(8)
root2.left=node(6)
root2.right=node(10)

T=Tree(root1)
print(T.issubtree(root2))
