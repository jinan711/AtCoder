N, K, M = map(int,input().split())
A = dict()
for _ in range(N):
    c, v = map(int,input().split())
    if c in A:
        A[c].append(v)
    else:
        A[c] = [v]
# print(A)
Maxs = []
for c, v in A.items():
    A[c] = sorted(A[c])
    Maxs.append(A[c].pop())
# print(A)
ans = 0 
Maxs = sorted(Maxs)
for i in range(M):
    ans += Maxs.pop()
Vs = []
for c, v in A.items():
    for e in v:
        Vs.append(e)
for e in Maxs:
    Vs.append(e)
Vs = sorted(Vs, reverse=True)
for i in range(K-M):
    ans += Vs[i]
print(ans)
