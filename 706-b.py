n = int(input())
X = list(map(int, input().split()))
q = int(input())
M = [int(input()) for _ in range(q)]

X.sort()

for m in M:
    left, right = 0, n
    while left < right:
        mid = (right + left) // 2
        if X[mid] <= m:
            left = mid + 1
        else:
            right = mid
    print(left)

