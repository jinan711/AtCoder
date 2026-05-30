import bisect
N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort(reverse=True)
B.sort()
for i in range(N):
    A[i] *= 2
# print(A)
# print(B)
cnt = 0
for a in A:
    ind = bisect.bisect_right(B,a)
    # print(a,ind-1,B)
    if a >= B[ind-1]:
        B.remove(B[ind-1])
        cnt += 1
    # print(a,ind-1,B)
print(cnt)