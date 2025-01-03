def digital_str_maximize(s):
    for i in range(len(s)):
        best = int(s[i])
        pos = i
        for j in range(i, min(i + 10, len(s))):
            if int(s[j]) - (j - i) > best:
                best = int(s[j]) - (j - i)
                pos = j
        while pos > i:
            s = s[:pos] + s[pos - 1] + s[pos + 1:]
            pos -= 1
        s = s[:i] + str(best) + s[i + 1:]
    print(s)

t = int(input())
test_cases = [input().strip() for _ in range(t)]
for s in test_cases:
    digital_str_maximize(s)

