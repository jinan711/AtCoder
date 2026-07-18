N, D = map(int,input().split())
ST = [tuple(map(int,input().split())) for _ in range(N)]
ans = 0
for i in range(N-1):
    for j in range(i+1,N):
        s = max(ST[i][0],ST[j][0])
        t = min(ST[i][1],ST[j][1])
        ans += max(0, t - s - D + 1)
print(ans)