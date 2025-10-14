from snowflake import snowflake


def test_snowflake_exists():
    assert snowflake


def test_snowflake_0_generations_empty_grid():
    assert snowflake(0) == [[]]


def test_snowflake_1_generation_1_square():
    assert snowflake(1) == [[1]]
