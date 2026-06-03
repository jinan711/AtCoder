N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort()
for i in range(N):
    A[i] *= 2
# print(A)
# print(B)
cnt = 0
ind = 0
for a in A:
    if ind < M and B[ind] <= a  :
        cnt += 1
        ind += 1
print(cnt)