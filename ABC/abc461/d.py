H, W, K = map(int,input().split())
S = [input() for _ in range(H)]
ans = 0
for ho in range(H):
    for wo in range(W):
        for he in range(1,H-ho+1):
            for we in range(1,W-wo+1):
                cnt = 0
                for i in range(he):
                    for j in range(we):
                        if S[ho+i][wo+j] == '1':
                            cnt += 1
                        print(ho,wo,he,we,i,j,cnt)
                if cnt == K:
                    ans += 1
print(ans)