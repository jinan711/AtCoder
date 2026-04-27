N, Q = map(int,input().split())
pile = [1] * N
stack = [1] * N
cardind = list(range(N))
abvcard = [0] * N
blwcard = [0] * N
# print(pile)
# print(stack)
# print(cardind)
# print(abvcard)
# print(blwcard)

for _ in range(Q):
    C, P = map(int,input().split())
    c = cardind[C-1]
    p = cardind[P-1] 
    pile[p] += stack[C-1]
    stack[P-1] += stack[C-1]
    pile[c] -= stack[C-1]
    cardind[C-1] = cardind[P-1]
    if blwcard[C-1] != 0:
        abvcard[blwcard[C-1]-1] = 0
    abvcard[P-1] = C
    blwcard[C-1] = P
    # print(pile)
    # print(stack)
    # print(cardind)
    # print(abvcard)
    # print(blwcard)
ans = [0] * N
for i in range(N):
    if blwcard[i] == 0:
        if abvcard[i] == 0:
            ans[i] = 1
        else:
            cnt = 2
            ind = abvcard[i] - 1
            # print(i,ind,abvcard[ind])
            while abvcard[ind] != 0:
                ind = abvcard[ind] - 1
                # print(i,ind,abvcard[ind])
                cnt += 1
            ans[i] = cnt
    if blwcard[i] != 0:
        ans[i] = 0
print(*ans)