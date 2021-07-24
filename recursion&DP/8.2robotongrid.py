#allpahts using recursion. O(2^(r+c))
def findpath(grid,r,c,curpath,paths):
    rows=len(grid)
    cols=len(grid[0])

    curpath.append((r,c))
    if(r==rows-1 and c==cols-1):
        paths.append(list(curpath))

    if(r+1<rows and grid[r+1][c]==0):
        findpath(grid,r+1,c,curpath,paths)
        
    if(c+1<cols and grid[r][c+1]==0):
        findpath(grid,r,c+1,curpath,paths)

    
    curpath.pop()





#single path
#using memorization. just one path. if already visited a cell mark it and dont traverse it again.
def fp(grid):
    rows=len(grid)
    cols=len(grid[0])
    visited={}
    if(findp(grid,0,0,rows,cols,paths,visited)):
        return list(reversed(paths))
    return None

def findp(grid,r,c,rows,cols,paths,visited):

    if(r>=rows or c>=cols or grid[r][c]==-1):
        return False
    
    if(visited.get((r,c),False)):
        return False
    
    if( (r==rows-1 and c==cols-1) or findp(grid,r+1,c,rows,cols,paths,visited) or findp(grid,r,c+1,rows,cols,paths,visited)):
        paths.append((r,c))
        return True
    
    visited[(r,c)]=True
    return False



grid=[[0 ,-1,0 ,0,0],
      [0 ,0 ,0 ,0,-1],
      [-1,-1,-1,0,0],
      [0 ,-1,0 ,0,0]]

paths=[]
curpath=[]
#print(fp(grid))
findpath(grid,0,0,curpath,paths)
print(paths)
print(len(paths))
