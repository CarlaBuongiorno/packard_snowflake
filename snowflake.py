def snowflake(number_of_generations):
    grid_size = number_of_generations*2-1
    center = number_of_generations-1
    if number_of_generations > 0:
        grid = build_grid(grid_size)
        grid[center][center] = 1
        
        for y in range(len(grid)):
            for x in range(len(grid)):
                print(y, x)
                different_check(grid, y, x)

        print(grid)
        return grid
    else:
        return []


def build_grid(grid_size):
    grid = []
    for i in range(grid_size):
        grid.append([0 for i in range(grid_size)])
    return grid


def different_check(grid, y, x):
    if len(grid) > 1 and grid[y+1][x] == 1:
        grid[y][x] = 1
    if len(grid)-1 > x and grid[y][x+1] == 1:
        grid[y][x] = 1
    return grid
