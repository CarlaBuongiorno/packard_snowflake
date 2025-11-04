from copy import deepcopy


def snowflake(number_of_generations):
    grid_size = number_of_generations*2-1
    center = number_of_generations-1

    if number_of_generations > 0: # To pass empty grid test
        grid = build_grid(grid_size)
        grid[center][center] = 1 # center is 1
        
        count = 2
        while count <= number_of_generations:
            new_grid = deepcopy(grid) # old grid doesnt change
            for y in range(len(grid)):
                for x in range(len(grid)):
                    if should_cell_be_filled_in(grid, y, x):
                        new_grid[y][x] = 1

                    # if check_one_touches_one(grid, y, x):
                    #     new_grid[y][x] = 1
            count += 1
            grid = new_grid
        return grid
    else:
        return []


def build_grid(grid_size):
    grid = []
    for i in range(grid_size):
        grid.append([0 for i in range(grid_size)])
    return grid
    

# should a cell (x, y) be filled in in the next generation?
def should_cell_be_filled_in(grid, y, x):
    if is_given_cell_filled_in(grid, y, x):
        return True
    return check_if_only_1_neighbour_is_filled_in(grid, y, x)
    # check if the given cell is filled in
    # if it is:
        # yes!
    # if not:
        # check if only one neighbour is filled in
            # if so:
                # yes!
            # if not:
                # no!

def is_given_cell_filled_in(grid, y, x):
    return (y >= 0 and y < len(grid) and x >= 0 and x < len(grid)) and grid[y][x] == 1

def check_if_only_1_neighbour_is_filled_in(grid, y, x):
    return sum([is_given_cell_filled_in(grid, y-1, x),
        is_given_cell_filled_in(grid, y+1, x),
        is_given_cell_filled_in(grid, y, x-1),
        is_given_cell_filled_in(grid, y, x+1)]) == 1

# check if only one neighbour is filled in
    # check cell is within the boundaries
    # check if one above is filled x=0 y=-1
    # check if one below is filled
    # check if one to the left is filled
    # check if one to the right is filled
    # count how many are filled -> is it only one?

# check cell is within the boundaries:
    # one above x=0 y=-1
    # one below x=0 y=+1
    # on to the left x=-1 y=0
    # on to the right x=+1 y=0



# def check_one_touches_one(grid, y, x):
#     check_list = [
#         len(grid)-1 > y and grid[y+1][x],
#         len(grid)-1 > x and grid[y][x+1],
#         y != 0 and grid[y-1][x],
#         x != 0 and grid[y][x-1]
#     ]
#     return sum(check_list) == 1 or grid[y][x] == 1


def check_one_touches_one(grid, y, x):
    '''Return True if a cell touches exactly one '1' (or is itself a '1').'''
    return sum(
        check_boundaries(grid, y, x, offset_y, offset_x)
        and grid[y+offset_y][x+offset_x]
        for offset_y, offset_x in [(-1, +0), (+1, +0), (+0, -1), (+0, +1)]
    ) == 1 or grid[y][x]


def check_boundaries(grid, y, x, y_boundary, x_boundary):
    '''Return True if (y+y_boundary, x+x_boundary) is within the grid bounds.'''
    return (
        (y+y_boundary >= 0 and y+y_boundary < len(grid))
        and (x+x_boundary >= 0 and x+x_boundary < len(grid))
    )
