import math


def snowflake(number_of_generations):
    grid = []
    grid_size = (number_of_generations*2)-1
    half_number_of_generations = math.ceil(grid_size/2)
    if number_of_generations > 0:
        grid = add_center_row(grid, number_of_generations)
        grid = build_rows_below_center(grid, half_number_of_generations)
        grid = build_rows_above_center(grid, half_number_of_generations)
        filled_rows = fill_rows_with_zeros(grid, half_number_of_generations)

        print(grid)
        return grid
    else:
        return grid
        

def add_center_row(grid, number_of_generations):
    center_row = [1 for i in range(number_of_generations*2-1)]
    grid.append(center_row)
    return grid


def build_rows_below_center(grid, half_number_of_generations):
    for i in range(half_number_of_generations-1):
        grid.append([1])
    return grid


def build_rows_above_center(grid, half_number_of_generations):
    for i in range(half_number_of_generations-1):
        grid.insert(0, [1])
    return grid


def fill_rows_with_zeros(grid, half_number_of_generations):
    for i in range(half_number_of_generations-1):
        for row in grid:
            if row == grid[1]:
                pass
            else:
                row.insert(0, 0)
                row.append(0)
    return grid