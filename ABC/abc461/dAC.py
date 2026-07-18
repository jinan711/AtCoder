H, W, K = map(int,input().split())
S = [input() for _ in range(H)]
A = [[0] * (W+1) for _ in range(H+1)]
for i in range(H):
    for j in range(W):
        if S[i][j] == '1':
            A[i][j+1] = 1
for i in range(1,H+1):
    for j in range(1,W+1):
        A[i][j] += A[i-1][j]
print(A)
ans = 0
for i in range(1,H+1):
    for j in range(i, H+1):
        B = [0] * (W+1)
        for k in range(1, W+1):
            B[k] = B[k-1] + (A[j][k]-A[i-1][k])
        r1 = 0
        r2 = 0
        for l in range(len(B)-1):
            r1 = max(r1,l+1)
            r2 = max(r2,l+1)
            while r1 < len(B) and B[r1]-B[l] < K:
                r1 += 1
            while r2 < len(B) and B[r2]-B[l] <= K:
                r2 += 1
            ans += r2-r1
print(ans)