'''Mathematical snowflakes!
You get some graph paper, and some colored pens. 
 - Color in one square in the middle of the paper.
 - Then, in a different color, you color in every square that touches an existing square on only one side.
 - Then, in a different color, you color in every square that touches an existing square on only one side.
 - Then, but in a different color, you color in every square that touches an existing square on only one side.
 - Keep going

If you do this, you end up with some very pretty patterns.
This is a class of 'celluar automata' called the Packard Snowflake.
If you look in the packard_snowflakes directory of this repository, you'll find photographs of the first eight steps of the snowflake.

Write a program to print out a mathematical snowflake.
Take a number on the command line which is the number of generations to run, and then output it to the terminal.
Hint; you can use the █ character to represent a colored-in square.

Is that too easy? Bonus points available:

    Save the snowflake to a PGM file, as above.
    Use the Blessed library to print the snowflakes out in different colors.
    Use Blessed, and animate the printing of the snowflake;
    print out the first generation, wait a second, print the next generation, wait, print the next...
    Save the snowflake as a PPM file; i.e. the color version of PGM https://en.wikipedia.org/wiki/Netpbm
    Look up 'cellular automata'. Do you see any famous examples you recognize?
    Do you see similarities between that and the snowflakes?
    Could you generalize your program to produce both?
'''

from snowflake import snowflake


def main():
    packard_snowflake = snowflake()
    print(packard_snowflake)

if __name__ == '__main__':
    main()