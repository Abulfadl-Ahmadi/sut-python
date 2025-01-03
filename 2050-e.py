import sys

inf = int(1e9)

def solve():
    a, b, res = input().split()
    n, m = len(a), len(b)
    dp = [[inf] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        dp[i + 1][0] = dp[i][0] + (a[i] != res[i])
    for j in range(m):
        dp[0][j + 1] = dp[0][j] + (b[j] != res[j])
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = min(dp[i - 1][j] + (a[i - 1] != res[i + j - 1]),
                           dp[i][j - 1] + (b[j - 1] != res[i + j - 1]))
    print(dp[n][m])
    for i in range(n+1):
        for j in range(m+1):
           print(f"{dp[i][j]}", end="")
        print()

def main():
    tests = int(input())
    for _ in range(tests):
        solve()

if __name__ == "__main__":
    main()

