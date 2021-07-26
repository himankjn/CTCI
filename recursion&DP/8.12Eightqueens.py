def eightqueens():
    column={}
    return queens(0,column)


#start with row 0. for every column check if its possible to place queen in this column considering previous row placements.
#if possible place it there and move to next row till last row is reached
def queens(row,column):
    if row==8:
        return 1
    ways=0
    for col in range(0,8):
        if(isvalid(row,col,column)):
            column[row]=col
            ways+=queens(row+1,column)
    return ways
def isvalid(row,col,column):
    #if any row till this row has queen placement contradicting this one then return False
    for row2 in range(0,row):
        col2=column[row2]
        if(col==col2):
            return False
        
        #check diagonal 
        coldist=abs(col-col2)
        rowdist=abs(row-row2)
        if coldist==rowdist:
            return False
    
    return True

print(eightqueens())