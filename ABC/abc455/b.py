H, W = map(int,input().split())
S = [input() for _ in range(H)]
cnt = 0
for i in range(H):
    for j in range(W):
        for k in range(H-i):
            for l in range(W-j):
                # print(i,j,k,l)
                flag = True
                for m in range(k+1):
                    for n in range(l+1):
                        # print('a','m=',m,'n=',n,i+m,j+n,i+k-m,j+l-n)
                        if S[i+m][j+n] != S[i+k-m][j+l-n]:
                            flag = False
                if flag:
                    cnt += 1
                    # print('tr',i,j,k,l)
print(cnt)