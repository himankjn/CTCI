class node:
    def __init__(self,v):
        self.v=v
        self.left=None
        self.right=None

class BST:
    def __init__(self,root):
        self.root=root
    
    def sequences(self):
        root=self.root
        print(self.seqhelper(root))
    
    def seqhelper(self,root):
        #will store return value containing sequences of current tree and below
        curseq=[]

        #for leaf node the sequences are empty lists.
        if(root is None):
            return [[]]

        #will contain weaved sequences of subsequences left and right subtrees
        #note: each subtree will have many sequences not just one.
        fin=[]

        leftseq=self.seqhelper(root.left)
        rightseq=self.seqhelper(root.right)

        #weave all subsequences starting with cur node val.
        prefix=[root.v]
        for l in leftseq:
            for r in rightseq:
                self.weave(l,r,fin,prefix)
                for f in fin:
                    curseq.append(f)
        

        return curseq


    #weave merges two lists in all possible combinations but keeping relative ordering of each array
    def weave(self,a1,a2,fin,prefix):
        #if a1 or a2 is empty then just add remaining array to prefix and that is one of the subsequences
        if(not a1):
            prefix.extend(a2)
            fin.append(prefix)
            return
        if(not a2):
            prefix.extend(a1)
            fin.append(prefix)
            return
        #if both a1 and a2 has elements recursively find sequences by fixing first element.
        #eg: seq([1,2,3],[4,5,6])
        #=   [1] + seq([2,3],[4,5,6])
        #and [4] + seq([1,2,3],[5,6])
        self.weave(a1[1:],a2,fin,prefix+[a1[0]])
        self.weave(a1,a2[1:],fin,prefix+[a2[0]])


root=node(3)
root.left=node(1)
root.left.left=node(0)
root.left.right=node(2)
root.right=node(4)
T=BST(root)
T.sequences()