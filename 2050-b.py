t = int(input())

ans = []
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    odds = 0
    no_odds = 0
    evens = 0
    no_evens = 0
    flage = False
    for i in range(n):
        if flage:
            odds += a[i]
            no_odds += 1
        else:
            evens += a[i]
            no_evens += 1
        flage = not flage

    if (((odds / no_odds) % 1 == 0) and ((evens / no_evens) % 1 == 0)) and ((odds / no_odds) == (evens / no_evens)):
        ans.append("YES")
    else:
        ans.append("NO")


for _ in range(t):
    solve()

print(*ans, sep="\n")
