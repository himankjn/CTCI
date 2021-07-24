class node:
    def __init__(self,val):
        self.val=val
        self.parent=None
        self.left=None
        self.right=None
    
class BST:
    def __init__(self,root):
        self.root=root
    
    def inorder_successor(self,root):
        if(root.right):
            root=root.right

            while(root.left):
                root=root.left
            print("inorder succ=",root.val)
            return
        #no right subtree. the inorder_succ is above this node.
        #if this node is to its left of its parent then parent is inorder_succ
        #else if this node is to right of its parent then its inorder_succ is above the parent untill parent.left is child.
        #use a example diagram to check inorder_succ of leaf nodes
        else:
            par=root.parent
            child=root
            
            while(par is not None and par.right==child):
                child=par
                par=par.parent

            if(par is None):
                print("no inorder successor")
            else:
                print("inorder succ=",par.val)        


root=node(6)
root.left=node(4)
root.right=node(8)
root.left.parent=root
root.right.parent=root

root.left.left=node(1)
root.left.left.parent=root.left

root.left.right=node(5)
root.left.right.parent=root.left

root.right.left=node(7)
root.right.left.parent=root.right
root.right.right=node(9)
root.right.right.parent=root.right
Tree=BST(root)
Tree.inorder_successor(root.left.right)