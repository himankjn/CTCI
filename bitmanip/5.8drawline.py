def drawline(screen,width,x1,x2,y):
    height=len(screen)/width
    for i in range(x1,x2+1):
        screen[width*y+i]=1

screen=  [0]*16
drawline(screen,2,1,3,2)


print(screen)