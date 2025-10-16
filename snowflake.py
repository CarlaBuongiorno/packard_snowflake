import math


def snowflake(number_of_generations):
    grid = []
    grid_size = (number_of_generations*2)-1
    center_cross = math.ceil(grid_size/2)
    if number_of_generations > 0:
        grid = add_center_row(grid, number_of_generations)
        print(grid)
        return grid
    else:
        return grid
        

def add_center_row(grid, number_of_generations):
    center_row = [1 for i in range(number_of_generations*2-1)]
    grid.append(center_row)
    return grid