from math import gcd

t = int(input())
res = [[] for _ in range(t)]

for i in range(t):
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    for j in range(q):
        l, r = map(int, input().split())
        big = max(*A[l - 1:r]) if r - l >= 1 else A[l - 1]
        D = [big - a for a in A[l - 1:r]]
        res[i].append(gcd(*D))
for i in range(t):
    print(*res[i], sep=" ")

