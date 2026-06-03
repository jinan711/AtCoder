T = int(input())
for _ in range(T):
    S = input()
    chars = [0] * 26
    for s in S:
        chars[ord(s)-ord('a')] += 1
    csum = sum(chars)
    cmax = max(chars)
    # print(csum,cmax)
    if cmax < csum - cmax + 2:
        print("Yes")
        ans = ""
        cmaxind = chars.index(cmax)
        chars[chars.index(cmax)] = 0
        for i in range(csum):
            if i % 2 == 0:
                ans += chr(cmaxind + ord('a'))
            else:
                ind = chars.index(max(chars))
                ans += chr(ind + ord('a'))
                chars[ind] -= 1
        print(ans)
    else:
        print("No")
    # print(chars)