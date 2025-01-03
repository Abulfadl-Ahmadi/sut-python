n = int(input())

A = list(map(int, input().split()))

s = 0
for i in range(3):
    s += int(2 * (A[i] % 2 - 0.5))

f = 0 if s > 0 else 1

for i in range(n):
    if A[i] % 2 == f:
        print(i + 1)


