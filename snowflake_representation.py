from random import randint


def representation(packard_snowflake, gen_colours, term):
    representation_for_each_generation = [get_representation_for_colour(colour, term) for colour in gen_colours]
    representation_for_each_generation[0] = ' '
    return [(''.join(representation_for_each_generation[generation] for generation in row)) for row in packard_snowflake]


def get_random_colours(number_of_generations):
    return [(randint(1, 255), randint(1, 255), randint(1, 255)) for gen in range(number_of_generations + 1)]


def get_representation_for_colour(colour, term):
    return term.color_rgb(colour[0], colour[1], colour[2]) + '█'
 