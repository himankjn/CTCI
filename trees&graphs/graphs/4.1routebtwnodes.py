from collections import defaultdict
from collections import deque
class Graph:
    def __init__(self):
        self.edges=defaultdict(list)

    def addedge(self,src,dest):
        self.edges[src].append(dest)


    def route(self,a,b):
        visited={}
        #return self.dfsroute(a,b,visited)
        return self.bfsroute(a,b,visited)

    def bfsroute(self,src,dest,visited):
        q=deque()
        q.append(src)
        visited[src]=True

        while(q):
            cur=q.popleft()
            for neighbour in self.edges[cur]:
                if(neighbour==dest):
                    return True
                if not visited.get(neighbour,False):
                    q.append(neighbour)
                    visited[neighbour]=True
        return False
    def dfsroute(self,src,dest,visited):
        visited[src]=True
        for neighbour in self.edges[src]:
            if(dest==neighbour):
                return True
            if(not visited.get(neighbour,False) and self.dfsroute(neighbour,dest,visited)):
                return True
        return False



G=Graph()
G.addedge(1,2)
G.addedge(2,3)
G.addedge(3,4)
G.addedge(5,6)
