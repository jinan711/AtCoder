import math
import itertools
X1, X2, X3 = map(int,input().split())
mod = 998244353
A = []
for i in range(X1):
    A.append(1)
for i in range(X2):
    A.append(2)
print(A)
print(len(list(itertools.permutations(A))))