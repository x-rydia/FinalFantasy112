"""
Random stuff for roguelike terrain generation that feels
dirty to put in the other file
"""

import random

def print2d(L: list) -> None:
    for row in L:
        print(row, end=", \n")

def setSeed(seed: str) -> None:
    """
    Given a string, get the sum of the 
    ascii values and use that to seed the 
    random number generator
    """
    if type(seed) != str: 
        raise Exception("Seed must be str")

    s = sum([ord(c) for c in seed])
    random.seed(s)

def unaliased2dList(rows: int, cols: int) -> list:
    """
    return a colsxrows 2d list with 0 as values
    """
    res = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(0)
        res.append(row)
    return res

def surroundingCells(x: int, y: int) -> set:
    """
    Return a set of (x,y) indicies of cells that are
    adjacent to the given (x,y)
    """
    res = set()
    res.add((x-1, y))
    res.add((x+1, y))
    res.add((x, y-1))
    res.add((x, y+1))
    res.add((x-1, y-1))
    res.add((x+1, y-1))
    res.add((x-1, y+1))
    res.add((x+1, y+1))
    return res