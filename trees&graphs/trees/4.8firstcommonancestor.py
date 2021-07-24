class node:
    def __init__(self,v):
        self.v=v
        self.left=None
        self.right=None
    def __str__(self):
        return str(self.v)
class binary_tree:
    def __init__(self,root):
        self.root=root

    #O(n) 
    def fca(self,root,p,q):
        if(not self.covers(root,p) or not self.covers(root,q)):
            #one of the nodes is not even in the tree. wrong input.
            return None
        #if p and q on different sides of root then root is fca
        #if both p and q on same side(left or right) then look for fca on that side
        elif(self.covers(root.left,p) and self.covers(root.left,q)):
            return self.fca(root.left,p,q)
        elif(self.covers(root.right,p) and self.covers(root.right,q)):
            return self.fca(root.right,p,q)
        else:
            return root
    def covers(self,root,n):
        if root is None:
            return False
        elif root==n:
            return True
        else:
            return self.covers(root.left,n) or self.covers(root.right,n)

root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(6)
root.right.right=node(7)

T=binary_tree(root)

print(T.fca(root,root.left.left,root.left.right))

