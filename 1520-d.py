t = int(input())
ans = []
def solve():
    hash_table = {}
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        b_i = str(a[i] - i)
        if b_i in hash_table:
            hash_table.update({b_i: hash_table.get(b_i) + 1})
        else:
            hash_table.update({b_i: 1})

    n = max(hash_table.values())
    return n * (n - 1) // 2


for i in range(t):
    ans.append(solve())

print(*ans, sep="\n")
