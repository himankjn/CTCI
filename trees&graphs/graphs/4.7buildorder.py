from collections import defaultdict


class Graph:
    def __init__(self,V):
        self.V=V
        self.edges=defaultdict(list)
    def addedge(self,src,dest):
        self.edges[src].append(dest)

    #using standard algo. remove 0 incoming edge vertices again and again
    def topologicalsort(self):
        sorted_v=[]
        visited={}
        while len(sorted_v)!=len(self.V):
            if(self.topsort(sorted_v,visited)==-1):
                return "no toplogical sort. cycle exists"
        return sorted_v
    def topsort(self,sorted_v,visited):
        #O(V)
        cur_poss={v:False for v in self.V}
        #O(E)
        for src,sublist in self.edges.items():
            for dest in sublist:
                cur_poss[dest]=True
        #remaining cur_pos which are false have no incoming edges
        #O(V)
        poss=[v for v in self.V if cur_poss[v]==False and not visited.get(v,False)]
        if(not poss):
            #there is cycle
            return -1

        for v in poss:
            self.edges[v]=[]
            visited[v]=True
            
        sorted_v.extend(poss)
        
    """
    #using dfs
    def topologicalsort(self):
        s=[]
        visited={}
        v_stack={}
        for v in self.V:
            if not visited.get(v,False):
                if self.dfs(v,visited,s,v_stack):
                    return "cycle exists"
        
        return s[::-1]
    
    
    #below dfs also takes care if there are cycles and hence no topological sort
    def dfs(self,src,visited,s,v_stack):
        visited[src]=True
        v_stack[src]=True

        for neighbour in self.edges[src]:
            if visited.get(neighbour,False) and v_stack.get(neighbour,False):
                return True
            if not visited.get(neighbour,False):
                if self.dfs(neighbour,visited,s,v_stack):
                    return True

        v_stack[src]=False
        s.append(src)
        return False
    """
    




V=['a','b','c','d','e','f']
G=Graph(V)
G.addedge('a','d')
G.addedge('f','b')
G.addedge('b','d')
G.addedge('f','a')
G.addedge('d','c')
#G.addedge('c','a')

print(G.edges)
print(G.topologicalsort())