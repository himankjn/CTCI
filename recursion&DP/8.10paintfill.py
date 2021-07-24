
def paintfill(image,r,c,newcol,visited):
    if(image[r][c]==newcol):
        return
    visited[(r,c)]=True
    rows=len(image)
    cols=len(image[0])

    if((r-1)>=0 and not visited.get((r-1,c),False) and image[r-1][c]==image[r][c]):
        paintfill(image,r-1,c,newcol,visited)
    if((c-1)>=0 and not visited.get((r,c-1),False) and image[r][c-1]==image[r][c]):
        paintfill(image,r,c-1,newcol,visited)
    if((r+1)<rows and not visited.get((r+1,c),False) and image[r+1][c]==image[r][c]):
        paintfill(image,r+1,c,newcol,visited)
    if((c+1)<cols and not visited.get((r,c+1),False) and image[r][c+1]==image[r][c]):
        paintfill(image,r,c+1,newcol,visited)
    
    image[r][c]=newcol

image=[[1,1,1],[1,1,0],[1,0,1]] 
visited={}
paintfill(image,1,1,3,visited)
print(image)
