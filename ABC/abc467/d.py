T = int(input())
def dist(x,y):
    return x**2 + y**2
for _ in range(T):
    px,py,qx,qy,rx,ry,sx,sy = map(int,input().split())
    pqC = ((px+qx)/2,(py+qy)/2)
    pqR = ((px-qx)**2+(py-qy)**2)**(1/2)/2
    c1x = (px+qx)/2 + (pqR**2-())