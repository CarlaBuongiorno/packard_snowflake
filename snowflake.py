from copy import deepcopy


def snowflake(number_of_generations):
    grid_size = number_of_generations*2-1
    center = number_of_generations-1

    if number_of_generations > 0:
        grid = build_grid(grid_size)
        grid[center][center] = 1
        
        new_grid = deepcopy(grid)
        for y in range(len(grid)):
            for x in range(len(grid)):
                if check_one_touches_one(grid, y, x):
                    new_grid[y][x] = 1

        print(new_grid)

        return new_grid
    else:
        return []


def build_grid(grid_size):
    grid = []
    for i in range(grid_size):
        grid.append([0 for i in range(grid_size)])
    return grid


def check_one_touches_one(grid, y, x):
    count = 0
    if grid[y][x] == 1:
        return True
    if len(grid)-1 > y and grid[y+1][x] == 1:
        count += 1
    if len(grid)-1 > x and grid[y][x+1] == 1:
        count += 1
    if y != 0 and grid[y-1][x] == 1:
        count += 1
    if x != 0 and grid[y][x-1] == 1:
        count += 1
    if count == 1:
        return True
    else:
        return False
