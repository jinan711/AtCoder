import bisect
N, K = map(int,input().split())
A = list(map(int,input().split()))
MaxA = [0] * N
for i in range(N):
    MaxA[i] = A[i] + (i+1) * K

MAmin = min(MaxA)

def ng(x):
    n = 0
    for i in range(N):
        if x > A[i]:
            n += (x - A[i] + i) // (i+1)
            if n > K:
                return True
    return False

vals = range(min(A), MAmin + 2)
ind = bisect.bisect_left(vals, True, key=ng)

print(vals[ind]-1)