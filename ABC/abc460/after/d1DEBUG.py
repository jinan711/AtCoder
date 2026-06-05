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

DEBUG = True
if DEBUG:
    print('B:')
    for row in B:
        print(''.join(row))
    print()

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

def pretty_row(row):
    return [ 'inf' if e == INF else e for e in row ]

step = 0
if DEBUG:
    print('initial G:')
    for row in G:
        print(pretty_row(row))
    print('queue:', list(q))
    print('---')

while q:
    y, x = q.popleft()
    step += 1
    for dy, dx in D:
        ny, nx = y + dy, x + dx
        if not(0 <= ny < H and 0 <= nx < W):
            continue
        if G[ny][nx] > G[y][x]:
            G[ny][nx] = G[y][x] + 1
            q.append((ny, nx))
    if DEBUG:
        print(f'step {step}, pop {(y, x)}')
        for row in G:
            print(pretty_row(row))
        print('queue:', list(q))
        print('---')

for g in G:
    print(''.join('.' if e % 2 == 0 else '#' for e in g))
