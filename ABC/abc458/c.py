S = input()
Cs = []
ans = 0
for i in range(len(S)):
    if S[i] == 'C':
        ans += min(i+1,len(S)-i)
        # print(i+1,len(S)-i)
print(ans)