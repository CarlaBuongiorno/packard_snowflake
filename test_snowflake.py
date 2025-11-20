import pytest

from snowflake import snowflake, should_cell_be_colored_over


def test_snowflake_exists():
    assert snowflake


def test_snowflake_0_generations_empty_grid():
    assert snowflake(0) == []


def test_snowflake_1_generation_1_square():
    assert snowflake(1) == [[1]]


def test_snowflake_2_generations_3_x_3():
    assert snowflake(2) ==  [
                                [0, 2, 0],
                                [2, 1, 2],
                                [0, 2, 0],
                            ]


GEN_2 = [[0, 0, 0], 
         [0, 1, 0], 
         [0, 0, 0]]

GEN_3 = [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 1, 1, 1, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0]]

GEN_4 = [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0],
         [0, 1, 1, 1, 1, 1, 0],
         [0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]]

GEN_5 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 1, 0, 1, 0, 1, 0, 0],
         [0, 1, 1, 1, 1, 1, 1, 1, 0],
         [0, 0, 1, 0, 1, 0, 1, 0, 0],
         [0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]

GEN_6 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
         [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
         [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

@pytest.mark.parametrize('grid, y, x, expected', [
            ([[1]], 0, 0, False),
            (GEN_2, 0, 0, False),
            (GEN_2, 0, 1, True),
            (GEN_2, 0, 2, False),
            (GEN_2, 1, 0, True),
            (GEN_2, 1, 2, True),
            (GEN_2, 2, 0, False),
            (GEN_2, 2, 1, True),
            (GEN_2, 2, 2, False),
            ([[0, 1, 0], 
              [0, 1, 0], 
              [0, 0, 0]], 0, 2, True),
            ([[0, 1, 0, 0], 
              [0, 0, 0, 1], 
              [0, 1, 0, 0], 
              [0, 0, 0, 0]], 1, 0, False),
            ([[0, 0, 0, 0], 
              [0, 0, 0, 1], 
              [0, 1, 0, 0], 
              [1, 0, 0, 0]], 0, 0, False),
            ([[0, 0, 0, 0], 
              [0, 0, 0, 1], 
              [0, 1, 0, 0], 
              [0, 1, 0, 0]], 0, 1, False),
            (GEN_3, 0, 0, False),
            (GEN_3, 0, 1, False),
            (GEN_3, 0, 2, True),
            (GEN_3, 0, 3, False),
            (GEN_3, 0, 4, False),
            (GEN_3, 1, 0, False),
            (GEN_3, 1, 1, False),
            (GEN_3, 1, 2, False),
            (GEN_3, 1, 3, False),
            (GEN_3, 1, 4, False),
            (GEN_3, 2, 0, True),
            (GEN_3, 2, 1, False),
            (GEN_3, 2, 3, False),
            (GEN_3, 2, 4, True),
            (GEN_3, 3, 0, False),
            (GEN_3, 3, 1, False),
            (GEN_3, 3, 2, False),
            (GEN_3, 3, 3, False),
            (GEN_3, 3, 4, False),
            (GEN_3, 4, 0, False),
            (GEN_3, 4, 1, False),
            (GEN_3, 4, 2, True),
            (GEN_3, 4, 3, False),
            (GEN_3, 4, 4, False),
            (GEN_4, 0, 0, False),
            (GEN_4, 0, 1, False),
            (GEN_4, 0, 2, False),
            (GEN_4, 0, 3, True),
            (GEN_4, 0, 4, False),
            (GEN_4, 0, 5, False),
            (GEN_4, 0, 6, False),
            (GEN_4, 1, 0, False),
            (GEN_4, 1, 1, False),
            (GEN_4, 1, 2, True),
            (GEN_4, 1, 3, False),
            (GEN_4, 1, 4, True),
            (GEN_4, 1, 5, False),
            (GEN_4, 1, 6, False),
            (GEN_4, 2, 0, False),
            (GEN_4, 2, 1, True),
            (GEN_4, 2, 2, False),
            (GEN_4, 2, 3, False),
            (GEN_4, 2, 4, False),
            (GEN_4, 2, 5, True),
            (GEN_4, 2, 6, False),
            (GEN_4, 3, 0, True),
            (GEN_4, 3, 1, False),
            (GEN_4, 3, 2, False),
            (GEN_4, 3, 3, False),
            (GEN_4, 3, 4, False),
            (GEN_4, 3, 5, False),
            (GEN_4, 3, 6, True),
            (GEN_4, 4, 0, False),
            (GEN_4, 4, 1, True),
            (GEN_4, 4, 2, False),
            (GEN_4, 4, 3, False),
            (GEN_4, 4, 4, False),
            (GEN_4, 4, 5, True),
            (GEN_4, 4, 6, False),
            (GEN_4, 5, 0, False),
            (GEN_4, 5, 1, False),
            (GEN_4, 5, 2, True),
            (GEN_4, 5, 3, False),
            (GEN_4, 5, 4, True),
            (GEN_4, 5, 5, False),
            (GEN_4, 5, 6, False),
            (GEN_4, 6, 0, False),
            (GEN_4, 6, 1, False),
            (GEN_4, 6, 2, False),
            (GEN_4, 6, 3, True),
            (GEN_4, 6, 4, False),
            (GEN_4, 6, 5, False),
            (GEN_4, 6, 6, False),
            (GEN_5, 0, 0, False),
            (GEN_5, 0, 1, False),
            (GEN_5, 0, 2, False),
            (GEN_5, 0, 3, False),
            (GEN_5, 0, 4, True),
            (GEN_5, 0, 5, False),
            (GEN_5, 0, 6, False),
            (GEN_5, 0, 7, False),
            (GEN_5, 0, 8, False),
            (GEN_6, 0, 0, False),
            (GEN_6, 0, 1, False),
            (GEN_6, 0, 2, False),
            (GEN_6, 0, 3, False),
            (GEN_6, 0, 4, False),
            (GEN_6, 0, 5, True),
            (GEN_6, 0, 6, False),
            (GEN_6, 0, 7, False),
            (GEN_6, 0, 8, False),
            (GEN_6, 0, 9, False),
            (GEN_6, 0, 10, False),
            (GEN_6, 1, 0, False),
            (GEN_6, 1, 1, False),
            (GEN_6, 1, 2, False),
            (GEN_6, 1, 3, False),
            (GEN_6, 1, 4, True),
            (GEN_6, 1, 5, False),
            (GEN_6, 1, 6, True),
            (GEN_6, 1, 7, False),
            (GEN_6, 1, 8, False),
            (GEN_6, 1, 9, False),
            (GEN_6, 1, 10, False),
])
def test_check_one_touches_one(grid, y, x, expected):
    assert should_cell_be_colored_over(grid, y, x) == expected


def test_snowflake_3_generations_5_x_5():
    assert snowflake(3) ==  [
                                [0, 0, 3, 0, 0],
                                [0, 0, 2, 0, 0],
                                [3, 2, 1, 2, 3],
                                [0, 0, 2, 0, 0],
                                [0, 0, 3, 0, 0],
                            ]


def test_snowflake_4_generations_7_x_7():
    assert snowflake(4) ==  [
                                [0, 0, 0, 4, 0, 0, 0],
                                [0, 0, 4, 3, 4, 0, 0],
                                [0, 4, 0, 2, 0, 4, 0],
                                [4, 3, 2, 1, 2, 3, 4],
                                [0, 4, 0, 2, 0, 4, 0],
                                [0, 0, 4, 3, 4, 0, 0],
                                [0, 0, 0, 4, 0, 0, 0],
                            ]


def test_snowflake_5_generations_9_x_9():
    assert snowflake(5) ==  [
                                [0, 0, 0, 0, 5, 0, 0, 0, 0],
                                [0, 0, 0, 0, 4, 0, 0, 0, 0],
                                [0, 0, 0, 4, 3, 4, 0, 0, 0],
                                [0, 0, 4, 0, 2, 0, 4, 0, 0],
                                [5, 4, 3, 2, 1, 2, 3, 4, 5],
                                [0, 0, 4, 0, 2, 0, 4, 0, 0],
                                [0, 0, 0, 4, 3, 4, 0, 0, 0],
                                [0, 0, 0, 0, 4, 0, 0, 0, 0],
                                [0, 0, 0, 0, 5, 0, 0, 0, 0],
                            ]
  

def test_snowflake_6_generations_11_x_11():
    assert snowflake(6) ==  [
                                [0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 6, 5, 6, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 4, 3, 4, 0, 0, 0, 0],
                                [0, 6, 0, 4, 0, 2, 0, 4, 0, 6, 0],
                                [6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6],
                                [0, 6, 0, 4, 0, 2, 0, 4, 0, 6, 0],
                                [0, 0, 0, 0, 4, 3, 4, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 6, 5, 6, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0],
                            ]