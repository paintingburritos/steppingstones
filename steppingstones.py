'''A cool problem I found from https://youtu.be/m4Uth-EaTZ8.
The purpose of this to create an interactive text simulation which allows the 
user to explore by seeing valid options for this problem

Rules:
The "game" takes place on an theortically infinite grid, but for the purpose of
simplicity this will take place on a finite m x m grid (50x50 default)

In this, you can place "brown" stones, or base stones, and your goal is to
place as many stone in sequential order for some n number of brown stones
and to reach the highest possible number. The rules for placing stones are
as follows:

1. Place n brown stones
2. Starting from 2, place stones in a manner such that the sum of the adjasent
    cells equal to the number.
    Adjacent cells are one orthogonally or diagonally
3. The goal is to reach the highest possible n

Once a stone is placed, you can distrubt it, and it no longer needs to have
a correct sum around it, all that matters is that the sum is correct when it
is placed.
'''