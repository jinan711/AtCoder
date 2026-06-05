from collections import deque
H, W = map(int,input().split())
S = [input() for _ in range(H)]

D = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
B = [['.'] * W for _ in range(H)] 
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            for dy, dx in D:
                ny, nx = i + dy, j + dx
                if not(0 <= ny < H and 0 <= nx < W):
                    continue
                if S[ny][nx] == '.':
                    B[ny][nx] = '#'
print(B)
C = []
for i in range(H):
    for j in range(W):
        if B[i][j] == '#':
            C.append((i, j))

INF = 10 ** 19
G = [[INF] * W for _ in range(H)]
q = deque()
for y, x in C:
    G[y][x] = 1
    q.append((y, x))

while q:
    y, x = q.popleft()
    for dy, dx in D:
        ny, nx = y + dy, x + dx
        if not(0 <= ny < H and 0 <= nx < W):
            continue
        if G[ny][nx] > G[y][x]:
            G[ny][nx] = G[y][x] + 1
            q.append((ny, nx))
# print(G)
for g in G:
    # ans = ""
    # for e in g:
    #     if e % 2 == 0:
    #         e += '#'
    #     else:
    #         e += '.'
    # print(ans)
    print("".join('.' if e % 2 == 0 else '#' for e in g))
