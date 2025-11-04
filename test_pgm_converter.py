from pgm_converter import convert_to_pgm


def test_pgm_converter_exists():
    assert convert_to_pgm


def test_snowflake_1_becomes_a_string():
    assert convert_to_pgm([[1]], 1) == 'P2\n1 1\n1\n1\n'


def test_snowflake_2_becomes_a_string():
    assert convert_to_pgm(
        [
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 0]
        ],
        2
    ) == (
            'P2\n3 3\n1\n'
            '0 1 0\n'
            '1 1 1\n'
            '0 1 0\n'
         )


def test_snowflake_3_becomes_a_string():
    assert convert_to_pgm(
        [
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [1, 1, 1, 1, 1],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
        ],
        3
    ) == (
            'P2\n5 5\n1\n'
            '0 0 1 0 0\n'
            '0 0 1 0 0\n'
            '1 1 1 1 1\n'
            '0 0 1 0 0\n'
            '0 0 1 0 0\n'
         )