'''A cool problem I found from https://youtu.be/m4Uth-EaTZ8.
The purpose of this to create an interactive text simulation which allows the 
user to explore by seeing valid options for this problem. The code will be a
set of functions that act on a list of stones

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

The board state will be a dictionary of coordinates and values. The value 1
represents starting stones.
A valid board has at least 1 starting stone on it {(0,0): 1}
'''

from typing import final


offsets = [
    (1,-1),
    (1,1),
    (1,0),
    (0,-1),
    (0,1),
    (-1,-1),
    (-1,1),
    (-1,0),
]

# finds all legal moves for a valid board:
def getMoves(board):
    current = max([*board.values()]) + 1
    sumMap = {}
    for e in board:
        for offset in offsets:
            if (e[0] + offset[0], e[1] + offset[1]) in sumMap:
                sumMap[(e[0] + offset[0], e[1] + offset[1])] += board[e]
            else:
                sumMap[(e[0] + offset[0], e[1] + offset[1])] = board[e]
    
    newPoints = []
    for e in sumMap:
        if sumMap[e] == current:
            newPoints.append(e)
    
    finalPoints = []
    for e in newPoints:
        if e not in board:
            finalPoints.append(e)
    return finalPoints

# returns a new board with the move made. if move not valid, returns the old board
# move is tuple (x, y)
def makeMove(board, move):
    validMoves = getMoves(board)
    if move in validMoves:
        board[move] = max([*board.values()]) + 1
    
    return board
    

test = {
    (0, 0): 1,
    (2, 2): 1,
}
