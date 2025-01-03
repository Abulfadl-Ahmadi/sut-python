from math import sqrt
from sympy import isprime

n = int(input())
X = list(map(int, input().split()))

def is_prime(n):
    if n % 1 != 0:
        return False
    if n == 1:
        return False
    i = 2
    flag = False
    while i * i <= n:
        if n % i == 0:
            flag = True
            break
        i += 1
    if flag:
        return False
    else:
        return True
for x in X:
    if x == 1:
        print("NO")

    if isprime(sqrt(x)):
        print("YES")
    else:
        print("NO")


