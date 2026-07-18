from itertools import product

def my(N, A, B):
    C = [0]
    for i in range(N-1):
        if (A[i] + A[i+1]) % 2 != B[i]:
            if C[-1] == 2:
                C.append(1)
            else:
                C[-1] += 1
        else:
            C.append(0)

    cnt = 0
    for c in C:
        if c != 0:
            cnt += 1
    return cnt


def official(N, A, B):
    C = A[:]
    D = A[:]

    D[0] += 1

    cnt0 = 0
    cnt1 = 1

    for i in range(N-1):
        if (C[i] + C[i+1]) % 2 != B[i]:
            C[i+1] += 1
            cnt0 += 1

        if (D[i] + D[i+1]) % 2 != B[i]:
            D[i+1] += 1
            cnt1 += 1

    return min(cnt0, cnt1)


for N in range(2, 11):
    print("checking", N)

    for A in product([0, 1], repeat=N):
        A = list(A)

        for B in product([0, 1], repeat=N-1):
            B = list(B)

            ans1 = my(N, A, B)
            ans2 = official(N, A, B)

            if ans1 != ans2:
                print("Found!")
                print("N =", N)
                print("A =", A)
                print("B =", B)
                print("my =", ans1)
                print("official =", ans2)
                exit()

print("No difference found.")