from pgm_converter import convert_to_pgm


def test_pgm_converter_exists():
    assert convert_to_pgm


def test_snowflake_1_becomes_a_string():
    assert convert_to_pgm([[1]], 1) == 'P2\n1 1\n1\n1\n'
