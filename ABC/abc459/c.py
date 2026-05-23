N, Q = map(int,input().split())
rem = 0
A = [0] * N
B = [0] * (10**6)
C = [0] * (10**6)
B[0] = N
C[0] = N
for _ in range(Q):
    q1, q2 = map(int,input().split())
    if q1 == 1:
        B[A[q2-1]] -= 1
        A[q2-1] += 1
        B[A[q2-1]] += 1
        C[A[q2-1]] += 1
    else:
        print(C[q2+rem])
    # print(A)
    # print(B)
    if B[rem] == 0:
        rem += 1
