n = int(input())
DB = {}
ans = []
for i in range(n):
    user_name = input()
    if user_name in DB:
        val = DB.get(user_name)
        DB.update({user_name: val + 1})
        ans.append(f"{user_name}{val}")
    else:
        DB[user_name] = 1
        ans.append("OK")

print(*ans, sep="\n")



