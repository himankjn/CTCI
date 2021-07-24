import sys
class node:
    def __init__(self,v):
        self.data=v
        self.left=None
        self.right=None
class binary_tree:
    def __init__(self,root):
        self.root=root

    def val_bst(self):
        initial_min=-sys.maxsize
        initial_max=sys.maxsize
        root=self.root
        return self.validatenoderec(root,initial_min,initial_max)
    def validatenoderec(self,root,min,max):
        if root is None :
            return True
        if(root.data<max and root.data>min and self.validatenoderec(root.left,min,root.data) and self.validatenoderec(root.right,root.data,max)):
            return True
        return False
        

    #using inorder traversal
    def bst_ornot(self):
        root=self.root
        A=[-sys.maxsize]
        flag=[True]
        self.inorder(root,A,flag)
        return flag[0]
    
    #using inorder if ascending order then bst.
    def inorder(self,root,A,flag):
        if(root is None):
            return
        self.inorder(root.left,A,flag)
        
        if root.data<=A[-1]:
            flag[0]=False
        A.append(root.data)
            
        self.inorder(root.right,A,flag)
    
root=node(6)
root.left=node(4)
root.right=node(1)
"""
root.left.left=node(1)
root.left.right=node(5)
root.right.left=node(7)
root.right.right=node(1)
"""
Tree=binary_tree(root)

print(Tree.val_bst())