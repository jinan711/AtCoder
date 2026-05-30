from collections import deque
H, W = map(int,input().split())
S = [input() for _ in range(H)]
B = []
cnt = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            B.append((i,j))
            cnt += 1


inf = 10 ** 9
q = deque()
dist = [[inf for _ in range(W)] for _ in range(H)]
d = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
for b in B:
    q.append(b)
    dist[b[0]][b[1]] = 0
# print(q)
while q:
    y, x = q.popleft()
    # print(x,y)
    # C1 = []
    # C2 = []
    # C3 = []
    for dy, dx in d:
        ny, nx = y+dy, x+dx
        # C1.append((ny,nx))
        if nx < 0 or nx >= W or ny < 0 or ny >= H:
            # C3.append((ny,nx))
            continue
        if dist[ny][nx] == inf:
            dist[ny][nx] = dist[y][x] + 1
            q.append((ny,nx))
            # C2.append((ny,nx))
    # print(C1)
    # print(C2)
    # print(C3)
    # print(x,y,q)
    # for i in range(H):
    #     print(dist[i])
for i in range(H):
    ans = ""
    for s in dist[i]:
        if s % 2 == 0:
            ans += '#'
        else:
            ans += '.'
    print(ans)
