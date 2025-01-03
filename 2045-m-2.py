row, colunm = map(int, input().split())
matrix_map = [" " * (colunm + 2)]
for r in range(row):
    matrix_map.append(" " + input() + " ")
matrix_map.append(" " * (colunm + 2))



