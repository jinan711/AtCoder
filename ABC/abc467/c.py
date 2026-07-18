N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
flag = False
cnt = 0
C = [0]
for i in range(N-1):
    if (A[i] + A[i+1])%M != B[i]:
        print(i,'a')
        if flag:
            print(i,'b')
            cnt += 1
            flag = False
        else:
            print(i,'c')
            flag = True
        if C[-1] == M:
            C.append(1)
        else:
            C[-1] += 1
    else:
        print(i,'d')
        if flag:
            flag = False
            cnt += 1
        C.append(0)
    print(i,'cnt',cnt)
print(C)
if flag:
    cnt += 1
print(len(C)-1)