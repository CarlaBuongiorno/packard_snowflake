'''Modify the snowflake program to take an additional argument:

python main.py --to-pgm <FILENAME>.pgm 7

If the --to-pgm argument is given, the program should output a representation
of the snowflake in PGM format to the given filename. It should do this in addition
to outputting the snowflake to the terminal.
The PGM (Portable Graymap) format is a very simple graphics format which can be
loaded in most image viewers or graphics programs. You can read all about it on
Wikipedia: https://en.wikipedia.org/wiki/Netpbm.'''


'''Add argument --to-pgm to argparser
This triggers the pgm_converter function 
create a file with .pgm extension
Write to file:

P2
2 2 (width / height)
1 (centre number)
0 1 0 (snowflake from original program)
1 1 1
0 1 0'''



from snowflake import snowflake


def convert_to_pgm(snowflake, number_of_generations):
    return 'P2\n1 1\n1\n1\n'