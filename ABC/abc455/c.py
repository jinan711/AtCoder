N, K = map(int,input().split())
A = list(map(int,input().split()))
Adict = {}
for a in A:
    if a in Adict:
        Adict[a] += a
    else:
        Adict[a] = a
Adict = sorted(Adict.items(), key=lambda x:x[1])
# print(Adict)
ans = 0
for i in range(len(Adict)-K):
    # print(Adict[i][1])
    ans += Adict[i][1]
print(ans)