N = int(input())
L = [list(map(int,input().split())) for _ in range(N)]
X, Y = map(int,input().split())
print(L[X-1][Y])