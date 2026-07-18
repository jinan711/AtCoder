N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = []
D = []
for a in A:
    C.append(a)
    D.append(a)
D[0] += 1
cnt0 = 0
cnt1 = 1
for i in range(N-1):
    if (C[i] + C[i+1]) % M != B[i]:
        C[i+1] += 1
        cnt0 += 1
    if (D[i] + D[i+1]) % M != B[i]:
        D[i+1] += 1
        cnt1 += 1
print(min(cnt0,cnt1))