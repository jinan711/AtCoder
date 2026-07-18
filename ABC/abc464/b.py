H, W = map(int,input().split())
C = [input() for _ in range(H)]
C2 = []
C3 = []
C4 = []
C5 = []
f = True
for i in range(H):
    flag = True
    for j in range(W):
        if C[i][j] == '#':
            flag = False
    if flag and f:
        f = False
    else:
        C2.append(C[i])
print(C2)
f = True
for i in range(len(C2)-1,-1,-1):
    flag = True
    for j in range(W):
        if C2[i][j] == '#':
            flag = False
    if flag and f:
        f = False
    else:
        C3.append(C2[i])
print(C3)
f = True
for i in range(W):
    flag = True
    for j in range(len(C3)):
        if C3[j][i] == '#':
            flag = False
    if flag and f:
        f = False
    else:
        C4.append(C3[j])
print(C4)
f = True
for i in range(len(C5[0])-1,-1,-1):
    flag = True
    for j in range(len(C3)):
        if C4[j][i] == '#':
            flag = False
    if flag and f:
        f = False
    else:
        C5.append(C4[j])

for c in C5:
    print(c)