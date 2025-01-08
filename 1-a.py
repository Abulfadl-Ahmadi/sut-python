n, m, a = map(int, input().split())

def ceil(n):
    if n % 1 == 0:
        return int(n)
    else:
        return int(n) + 1

print(ceil(n / a) * ceil(m / a))
# OK