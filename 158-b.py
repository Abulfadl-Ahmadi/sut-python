from math import ceil

n = int(input())
S = list(map(int, input().split()))

G1 = S.count(1)
G2 = S.count(2)
G3 = S.count(3)
G4 = S.count(4)

t = G4

pair31 = min(G1, G3)

t += pair31

G1 -= pair31
G3 -= pair31

t += G3

t += G2 // 2
if G2 % 2 == 1:
    t += 1
    G1 = max(0, G1 - 2)

t += ceil(G1 / 4)

print(t)
