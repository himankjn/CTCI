from collections import defaultdict, deque
class node:
    def __init__(self,v):
        self.v=v
        self.left=None
        self.right=None

class depthlists:
    def __init__(self):
        self.L=defaultdict(list)
    
    

class binary_tree:
    def __init__(self,root):
        self.root=root
    

    def lod(self):
        lists=defaultdict(list)
        visited={}
        self.traverse(self.root,0,lists)
        return lists
    def traverse(self,root,lvl,lists):
        if(root is None):
            return
        lists[lvl].append(root.v)
        self.traverse(root.left,lvl+1,lists)
        self.traverse(root.right,lvl+1,lists)
"""
    def bfs(self,q,level,DL):
        cur=self.root
        q.append(cur)
        level[cur.v]=0
        while q:
            cur=q.popleft()
            DL.L[level[cur.v]].append(cur.v)
            if(cur.left is not None):
                level[cur.left.v]=level[cur.v]+1
                q.append(cur.left)
            if(cur.right is not None):
                level[cur.right.v]=level[cur.v]+1
                q.append(cur.right)
        return DL
"""
        

root=node(2)
root.left=node(4)
root.right=node(6)
root.left.left=node(9)
root.left.right=node(8)
root.right.left=node(3)
root.right.right=node(1)
Tree=binary_tree(root)

print(Tree.lod())