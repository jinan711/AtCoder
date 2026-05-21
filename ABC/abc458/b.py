H, W = map(int,input().split())
X = [[0] * W for _ in range(H)]
if H == 1:
    if W == 1:
        X[0][0] = 0
    elif W == 2:
        X[0][0] = 1
        X[0][1] = 1
    else:
        for i in range(W):
            X[0][i] = 2
        X[0][0] = 1
        X[0][-1] = 1
elif H == 2:
    if W == 1:
        X[0][0] = 1
        X[1][0] = 1
    elif W == 2:
        for i in range(H):
            for j in range(W):
                X[i][j] = 2
    else:
        for i in range(H):
            for j in range(W):
                X[i][j] = 3
            X[i][0] = 2
            X[i][-1] = 2 
else:
    if W == 1:
        for i in range(H):
            X[i][0] = 2
        X[0][0] = 1
        X[-1][0] = 1
    elif W == 2:
        for i in range(W):
            for j in range(H):
                X[j][i] = 3
            X[0][i] = 2
            X[-1][i] = 2
        
    else:
        for i in range(H):
            if i == 0 or i == H-1:
                for j in range(W):
                    X[i][j] = 3
                X[i][0] = 2
                X[i][-1] = 2 
            else:
                for j in range(W):
                    X[i][j] = 4
                X[i][0] = 3
                X[i][-1] = 3
for i in range(H):
    print(*X[i])