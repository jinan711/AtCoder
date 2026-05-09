N, K = map(int,input().split())
L = [list(map(int,input().split())) for _ in range(N)]
C = list(map(int,input().split()))

Blen = 0
for i in range(N):
    if Blen + L[i][0] * C[i] >= K:
        # print(K, Blen)
        num = K - Blen
        # print('1',num)
        num %= L[i][0]
        # print('2',num)
        if num == 0:
            num = L[i][0]
        print(L[i][num])
        exit()
    else:
        Blen += L[i][0] * C[i]