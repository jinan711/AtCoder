N = int(input())
KA = [list(map(int,input().split())) for _ in range(N)]
B = [[] for _ in range(N)]
for i in range(N):
    for j in range(KA[i][0]):
        # print(KA[i][j+1])
        B[KA[i][j+1]-1].append(i+1)
# print(B)
for i in range(N):
    ans = [len(B[i])] + sorted(B[i])
    print(*ans)