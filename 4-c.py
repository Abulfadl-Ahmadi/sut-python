n = int(input())
DB = []
users = [input() for _ in range(n)]

for i in range(n):
    if not users[i] in DB:
        DB.add(users[i])
    else:
        for 


