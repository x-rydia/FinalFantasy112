"""
Rogue-like terrain generation algorithm which will create a 
2d list of walls. 
"""
import random
import math

from levelbuilder.utils import unaliased2dList, print2d, surroundingCells
from copy import deepcopy

class Room:
    def __init__(self, size: int,
            topLeftX: int, topLeftY: int,
            textureValue: int=3) -> None:

        self.size = size
        self.topLeftX = topLeftX
        self.topLeftY = topLeftY
        self.textureValue = textureValue

        #Populate a list of (x,y) pairs representing walls of room
        self.walls = set()
        self.tunnelCells = set()

        #add the top side
        for i in range(topLeftX, topLeftX+size):
            self.walls.add(
                (i, topLeftY)
            )
        
        #add the bottom side
        for i in range(topLeftX, topLeftX+size):
            self.walls.add(
                (i, topLeftY+size)
            )
        
        #add the left side
        for i in range(topLeftY, topLeftY+size):
            self.walls.add(
                (topLeftX, i)
            )
        
        #add the right side
        for i in range(topLeftY, topLeftY+size):
            self.walls.add(
                (topLeftX+size, i)
            )
        
        #add the bottom right corner
        self.walls.add(
            (topLeftX+size, topLeftY+size)
        )

    
    def __str__(self) -> str:
        return "Room: size: {}, topLeft: ({},{}), textureValue: {}".format(
            self.size, self.topLeftX, self.topLeftY, self.textureValue)
    
    def getTunnelCell(self) -> tuple:
        """
        Return a random wall in the room that is not a corner wall
        and is not already a tunnel cell
        """
        while True:
            wall = random.choice(list(self.walls))
            if ((wall[0] != self.topLeftX and wall[0] != self.topLeftX+self.size) and 
                (wall[1] != self.topLeftY and wall[1] != self.topLeftY+self.size)):
                    print("wall: ", wall)
                    if wall not in self.tunnelCells:
                        self.tunnelCells.add(wall)
                        return wall
    
    def getDirByCell(self, x, y) -> tuple:
        """
        Return the direction of the wall that the cell is on 
        as a (dx, dy) tuple
        """
        if (x, y) not in self.walls: 
            raise Exception("Cell is not in room")
        
        left = (x-1, y) in self.walls
        right = (x+1, y) in self.walls
        top = (x, y-1) in self.walls
        bottom = (x, y+1) in self.walls
        if left or right:
            if (x-self.size) < 0:
                return (1, 0)
            else:
                return (-1, 0)
        elif top or bottom:
            if (y-self.size) < 0:
                return (0, 1)
            else:
                return (0, -1)
        

    
def createRoom(map: list):
    """
    Create a room: (NxN) empty square of walls
            at a random point in a list map
            that does not overlap with any other 
            filled in squares on the board.
    """
    done = False
    upperBoundSize = len(map[0]) // 4
    lowerBoundSize = len(map[0]) // 8
    while not done:
        size = random.randint(lowerBoundSize, upperBoundSize)
        topLeftX = random.randint(0, len(map[0])-size-1)
        topLeftY = random.randint(0, len(map)-size-1)
        room = Room(size, topLeftX, topLeftY)
        if all(map[y][x] == 0 for x,y in room.walls):
            done = True
            for x,y in room.walls:
                map[y][x] = room.textureValue
    room.walls.pop()
    return room


class Level:
    def __init__(self, 
            rows: int,
            cols: int, 
            rooms: int,
            holes: int=25,
            textureValue=1):
        self.rows = rows
        self.cols = cols
        self.map = unaliased2dList(rows, cols)
        self.rooms = []
        self.tunnels = []
        allWalls = set()

        for r in range(rooms):
            room = createRoom(self.map)
            self.rooms.append(room)
            allWalls.update(room.walls)





        #set all cells that are on an edge to be walls
        for x in range(len(self.map[0])):
            self.map[0][x] = textureValue
            self.map[-1][x] = textureValue
        for y in range(len(self.map)):
            self.map[y][0] = textureValue
            self.map[y][-1] = textureValue
        
        for allWall in allWalls:
            self.map[allWall[1]][allWall[0]] = textureValue

        nHoles = (holes * len(self.rooms)) // 100

        for r in range(nHoles):
            allList = list(allWalls)
            wall = random.choice(allList)
            self.map[wall[1]][wall[0]] = 0
        

        
    def __str__(self) -> str:
        return print2d(self.map)
    
    def getRoomByCoord(self, x, y):
        for room in self.rooms:
            if (x, y) in room.walls:
                return room
        return None


   