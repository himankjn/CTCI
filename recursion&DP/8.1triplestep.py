def ts(n):
    dp=[0]*(n+1)
    return triplestep(n,dp)
def triplestep(n,dp):
    if(n<0):
        return 0
    if n==0 or n==1:
        return 1
    
    else:
        if dp[n]==0:
            dp[n]=triplestep(n-1,dp)+triplestep(n-2,dp)+triplestep(n-3,dp)
        return dp[n]


print(ts(4))

    