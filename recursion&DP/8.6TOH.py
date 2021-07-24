def toh(n,x,y,z):
    if(n==0):
        return
    toh(n-1,x,z,y)
    print("move disk from {} to {}".format(x,y))
    toh(n-1,z,y,x)

toh(3,'x','y','z')