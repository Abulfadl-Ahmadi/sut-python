from copy import copy
row, colunm = map(int, input().split())
matrix_map = [" " * (colunm + 2)]
mirrors_init = {}
for r in range(row):
    matrix_map.append(" " + input() + " ")
    for c in range(colunm):
        if matrix_map[r+1][c+1] != '.':
            mirrors_init[f"{r+1},{c+1}"] = False
matrix_map.append(" " * (colunm + 2))

# (0, 1)    EAST
# (0, -1)   WEST
# (-1, 0)    NORTH
# (1, 0)   SOUTH
def director(pos, dir, m):
    while True:
        if matrix_map[pos[0]][pos[1]] == '/':
            m[f"{pos[0]},{pos[1]}"] = True
            match dir:
                case (0, 1):
                    dir = (-1, 0)
                case (-1, 0):
                    dir = (0, 1)
                case (0, -1):
                    dir = (1, 0)
                case (1, 0):
                    dir = (0, -1)
        if matrix_map[pos[0]][pos[1]] == '\\':
            m[f"{pos[0]},{pos[1]}"] = True
            match dir:
                case (0, 1):
                    dir = (1, 0)
                case (-1, 0):
                    dir = (0, -1)
                case (0, -1):
                    dir = (-1, 0)
                case (1, 0):
                    dir = (0, 1)
        pos[0] += dir[0]
        pos[1] += dir[1]
        if pos[0] == 0 or pos[0] == row + 1:
            break
        if pos[1] == 0 or pos[1] == colunm + 1:
            break
    for is_touched in m.values():
        if not is_touched:
            return False
    return True
ans = []
for r in range(row):
    if director([r + 1, 0], [0, 1], copy(mirrors_init)):
        ans.append(f'W{r + 1}')
    if director([r + 1, colunm + 1], [0, -1], copy(mirrors_init)):
        ans.append(f"E{r + 1}")

for c in range(colunm):
    if director([0, c + 1], [1, 0], copy(mirrors_init)):
        ans.append(f"N{c + 1}")
    if director([row + 1, c + 1], [-1, 0], copy(mirrors_init)):
        ans.append(f"S{c + 1}")

print(len(ans))
print(*ans, sep=" ")
