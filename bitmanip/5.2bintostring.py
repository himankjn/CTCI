
def bintostring(n):
    fins="0."
    while(len(fins)<34 and n!=0):
        n*=2
        intpart=1 if n>=1 else 0
        n=n-1 if n>=1 else n
        fins+=str(intpart)

    return fins

print(bintostring(0.25))