from math import isqrt

def prime_gen(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, isqrt(n) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime

n = int(input())
X = list(map(int, input().split()))

max_sqrt = max(isqrt(x) for x in X)
prime = prime_gen(max_sqrt)

for x in X:
    root = isqrt(x)
    if root * root == x and prime[root]:
        print("YES")
    else:
        print("NO")
