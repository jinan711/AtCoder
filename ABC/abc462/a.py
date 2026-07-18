S = input()
ans = ""
nums = ('0','1','2','3','4','5','6','7','8','9')
for s in S:
    if s in nums:
        ans += s
print(ans)