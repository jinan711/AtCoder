S = input()
N = int(input())
ans = ""
for i in range(N, len(S)-N):
    ans += S[i]
print(ans)