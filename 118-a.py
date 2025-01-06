user_input = input().lower()

vowels = [
    "a", "e", "u", "i", "o", "y"
]
ans = []
for c in list(user_input):
    if c not in vowels:
        ans.append(f".{c}")

print(*ans, sep="")
