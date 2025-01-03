def solve(N, D, S):
#   if N == D or N == S:
#       return N
#    if 2 * D > N and S == 1:
#       return N
#   if 2 * S > N:
#       return S
    n, d = N//S, D//S
    Y = min(2*d, n)
    Y = Y - (Y % 2 != 0 and d > S)
    i = 1
#   if N - D < S:
#       return (D // S + (N % S == 0)) * S

    while i * i <= Y:
        if Y // i <= d + i and Y % (Y // i) == 0:
            return S * Y
        i += 1
    return S if Y == 0 else S * (Y - 1)


N, D, S = map(int, input().split())
print(solve(N, D, S))
