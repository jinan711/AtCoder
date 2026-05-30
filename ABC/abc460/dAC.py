from collections import deque
H, W = map(int,input().split())
S = [input() for _ in range(H)]
B = [['.'] * W for _ in range(H)]
d = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            for dy,dx in d:
                ny, nx = i+dy, j + dx
                if 0 <= ny < H and 0 <= nx < W and S[ny][nx] == '.':
                    B[ny][nx] = '#'

inf = 10 ** 9
q = deque()
dist = [[inf] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if B[i][j] == '#':
            dist[i][j] = 0
            q.append((i, j))

while q:
    y, x = q.popleft()
    for dy, dx in d:
        ny, nx = y+dy, x+dx
        if 0 <= ny < H and 0 <= nx < W and dist[ny][nx] == inf:
            dist[ny][nx] = dist[y][x] + 1
            q.append((ny,nx))
for i in range(H):
    print(''.join('.' if s % 2 == 0 else '#' for s in dist[i]))
