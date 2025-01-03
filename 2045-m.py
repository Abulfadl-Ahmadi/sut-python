class Map:
    def __init__(self, row, column, matrix):
        self.row = row
        self.column = column
        self.matrix = matrix

    def __str__(self):
        res = ""
        for row in self.matrix:
            res += "".join(row) + "\n"
        return res[:-1]

    def __rep__(self):
        return str(self)


class Poton():
    def __init__(self, position:touple):
        self.position = position
        # TODO: calculate the initial direction based on the initial position


class Miror():
    def __init__(self, direction:str, position:touple):
        self.direction = direction
        self.is_touched = False
        self.position = position

    def direct(self, origin:touple):
        poton_direction = (origin[0] - self.position[0], origin[1] - self.position[1])
        if self.direction == "/":
            if poton_direction == (0, 1):
                distination = 
        else:
    



row, column = map(int, input().split())

map_matrix_data = [input() for _ in range(row)]

my_map = Map(row, column, map_matrix_data)
print(my_map)

