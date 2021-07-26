#including rotations
def maxHeight(cuboids):
        boxes=[]
        
        for box in cuboids:
            box.sort()
        
        boxes=cuboids
            
        boxes.sort(reverse=True)
        dp={}
        
        maxh=0
        for i in range(len(boxes)):
            height=maxheight(boxes,i,dp)
            maxh=max(maxh,height)
        
        return maxh
    
def maxheight(boxes,index,dp):
        
        
        
    if(index>=len(boxes)):
        return 0
        
    if(dp.get(index,False)):
        return dp[index]
        
    maxh=0
    for i in range(index+1,len(boxes)):
        if valid(boxes[index],boxes[i]):
            height=maxheight(boxes,i,dp)
            maxh=max(maxh,height)
        
        
    maxh+=boxes[index][2]
    dp[index]=maxh 
    return maxh
    
def valid(bottom,top):
    if bottom[2]>=top[2] and  bottom[1]>=top[1] and bottom[0]>=top[0]:
        return True
        
    return False

boxes=[[4, 6, 7], [1, 2, 3], [4, 5, 6], [10, 12, 32]]
print(maxHeight(boxes))