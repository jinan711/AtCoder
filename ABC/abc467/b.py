N = int(input())
lost = 0
for i in range(N):
    A, B, S = input().split()
    if S == "keep":
        lost += int(B)-int(A)
print(lost)