H, W = map(int,input().split())
# print(25*H*H,W*10000)
# print(W/H**2*10000)
if 25 * H * H <= W*10000:
    print("Yes")
else:
    print("No")