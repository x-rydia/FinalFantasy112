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


testMap = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

#set of all (x,y) pairs representing walls
allWalls = set()
for r in range(len(testMap)):
    for c in range(len(testMap[r])):
        if testMap[r][c] == 1:
            allWalls.add((r,c))

dirs = [(1,0), (-1,0), (0,1), (0,-1)]
def backtrackingIsPath(r1, c1, r2, c2, visited=None, path=None):
    """
    Return True if there is a path from (r1,c1) to (r2,c2)
    that doesn't go through any walls
    """
    print(path)
    if visited is None:
        visited = set()
    if path is None:
        path = []
    path.append((r1,c1))
    visited.add((r1,c1))
    if (r1,c1) == (r2,c2):
        return True
    for (dr,dc) in dirs:
        newR = r1 + dr
        newC = c1 + dc
        if (newR, newC) in allWalls:
            continue
        if (newR, newC) in visited:
            continue
        if backtrackingIsPath(newR, newC, r2, c2, visited, path):
            return True
    path.pop()
    return False

def testBacktrackingIsPath():
    print("Testing backtrackingIsPath...")
    assert backtrackingIsPath(1,1,3,3) == True
    assert backtrackingIsPath(1, 1, 7, 7) == False
    print("Passed")

if __name__ == "__main__":
    testBacktrackingIsPath()
