N = int(input())
XY = [tuple(map(int,input().split())) for _ in range(N)]
X = sorted(XY)
Y = sorted(XY, key=lambda a: a[1])
# print(X)
# print(Y)
# chk = set()
ans = 0
miny = N
for x, y in X:
    if y <= miny:
        # print('X',x, y,miny)
        ans += 1
        miny = y
# for x, y in X:
#     if y <= miny and (x, y) not in chk:
#         # print('X',x, y,miny)
#         ans += 1
#         miny = y
        # chk.add((x, y))
# minx = N
# for x, y in Y:
#     if x <= minx and (x, y) not in chk:
#         print('Y',x,y,minx)
#         ans += 1
#         minx = x
#         chk.add((x, y))
# print(chk)
print(ans)
