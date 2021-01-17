#
#
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?


import datetime

start = datetime.datetime.now()
print(start)


grid_size = 20
x_len = y_len = grid_size + 1


grid = [[0 for col in range(x_len)] for row in range(y_len)]


def possible_paths_at_vertex(x, y):
    global grid
    if grid[y][x] != 0:
        return grid[y][x]

    possible_paths = 0
    if x + 1 < x_len:
        if grid[y][x + 1] != 0:
            possible_paths += grid[y][x + 1]
        else:
            possible_paths += 1
    if y + 1 < y_len:
        if grid[y + 1][x] != 0:
            possible_paths += grid[y + 1][x]
        else:
            possible_paths += 1

    grid[y][x] = possible_paths
    return possible_paths


# print(f"Going X")
for x in range(grid_size, -1, -1):
    possible_paths_at_vertex(x, grid_size)
# print(f"Going Y")
for y in range(grid_size, -1, -1):
    possible_paths_at_vertex(grid_size, y)

# print(f"Going inner")
for x in range(grid_size, -1, -1):
    for y in range(grid_size, -1, -1):
        possible_paths_at_vertex(x, y)


# [print(row) for row in grid]  # printing this with a large grid can lock your env
print(f"FINISHED: {grid[0][0]}")
end = datetime.datetime.now() - start
print(end)

# runtime 0:00:00.000354