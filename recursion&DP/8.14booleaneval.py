def string_to_bool(s):
    return s == "1"


def totalways(s,res,dp):

    #compute for res=True. if its false then total-res
    if(len(s)==0):
        return 0
    if(len(s)==1):
        return 1 if string_to_bool(s) == res else 0
    if(dp.get(str(res)+s)):
        return dp[str(res)+s]
    ways=0
    #for every operator eval left and right side
    for i in range(1,len(s),2):
        c=s[i]
        left=s[:i]
        right=s[i+1:]

        lefttrue=totalways(left,True,dp)
        leftfalse=totalways(left,False,dp)
        righttrue=totalways(right,True,dp)
        rightfalse=totalways(right,False,dp)

        total=(righttrue+rightfalse)*(lefttrue+leftfalse)

        if(c=='^'):
            totaltrue=lefttrue*rightfalse + leftfalse*righttrue
        elif(c=='|'):
            totaltrue=lefttrue*righttrue + lefttrue*rightfalse + leftfalse*righttrue
        elif(c=="&"):
            totaltrue=lefttrue*righttrue
        
        subways=totaltrue if res else total-totaltrue
        ways=ways+subways

    dp[str(res)+s]=ways
    return ways

print(totalways("1|0^0&1|1",True,{}))
