T = int(input())
for _ in range(T):
    X1, Y1, R1, X2, Y2, R2 = map(int,input().split())
    xdis = (X1-X2)**2
    ydis = (Y1-Y2)**2
    dis = xdis+ydis
    rsum = (R1+R2)**2
    rsub = (R1-R2)**2
    if rsub <= dis <= rsum:
        print("Yes")
    else:
        print("No")
