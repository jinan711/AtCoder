N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = [0]
for i in range(N-1):
    if (A[i] + A[i+1])%M != B[i]:
        # print(i,'a')
        if C[-1] == M:
            C.append(1)
        else:
            C[-1] += 1
    else:
        # print(i,'d')
        C.append(0)
print(C)
cnt = 0
for c in C:
    if c != 0:
        cnt += 1
print(cnt)