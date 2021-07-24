num=13 #1101

def getbit(num,bit):
    mask=1<<bit #0100
    res=0 if num&mask==0 else 1
    return res
print(getbit(13,3))

def setbit(num,bit):
    mask=1<<bit
    num=num|mask
    return num

print(setbit(num,1))

def clearbit(num,bit):
    mask=1<<bit
    mask=~mask
    return num&mask

print(clearbit(num,3))

def clearmostsigthrough(num,bit):
    #00000011111
    mask=1<<bit
    mask=mask-1
    return num&mask

def clearleastsigthrough(num,bit):
    mask=1<<bit
    mask=mask-1
    mask=~mask
    return num&mask


def updatebit(num,bit,v):
    clearmask=1<<bit
    clearmask=~clearmask
    return (num&clearmask)|(v<<bit)




