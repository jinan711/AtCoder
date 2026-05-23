N = int(input())
S = list(input().split())
ans = ""
for i in range(N):
    if ord(S[i][0]) < ord('s'):
        ans += str((ord(S[i][0])-1)//3 - 30)    
    elif S[i][0] != 'z':
        ans += str((ord(S[i][0])-2)//3 - 30)   
    else:
        ans += '9'
print(ans)