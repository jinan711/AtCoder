N, K = map(int,input().split())
A = list(map(int,input().split()))
MaxA = [0] * N
for i in range(N):
    MaxA[i] = A[i] + (i+1) * K
# print(MaxA)
MAmin = min(MaxA)
l = min(A)
r = MAmin + 1
while r-l > 1:
    mid = l + (r-l) // 2
    n = 0
    flag = False
    for i in range(N):
        m = 0
        if mid > A[i]:
            if (mid - A[i]) % (i+1) == 0:
                m = (mid - A[i]) // (i+1)
            else:
                m = (mid - A[i]) // (i+1) + 1
        n += m
        if n > K:
            flag = True
    if flag:
        r = mid
    else:
        l = mid
print(l)
