def snowflake(number_of_generations):
    grid = []
    if number_of_generations > 0:
        center_row = [1 for i in range(number_of_generations*2-1)]
        grid.append(center_row)
        return grid
    else:
        return grid