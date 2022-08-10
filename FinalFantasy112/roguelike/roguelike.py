"""
Rogue-like terrain generation algorithm which will create a 
2d list of walls. 
"""
import random
import math

from utils import unaliased2dList, print2d, surroundingCells

class Room:
    def __init__(self, size: int,
            topLeftX: int, topLeftY: int,
            textureValue: int=1) -> None:

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

class Tunnel:
    """
    Tunnel between two rooms. takes two tunnel cells and a map
    """
    def __init__(self, 
            start: tuple, 
            end: tuple,
            map: list,
            textureValue: int=1) -> None:
        self.start = start
        self.end = end
        self.map = map + []
        self.textureValue = textureValue
        self.tunnelCells = set()
        self.tunnelCells.add(start)
        self.tunnelCells.add(end)

        #Calculate a path from start to end,
        #not going through walls
        #and add the cells to the tunnelCells set
        #Use breadth first search (https://www.geeksforgeeks.org/shortest-distance-two-cells-matrix-grid/)
        #to find the shortest path
        path = [self.start]
        visited = set()
        visited.add(self.start)
        while path[-1] != self.end: pass


        

    def setTunnelToMap(self, map) -> None:
        """
        The actual tunnel cells stored in tunnelCells are the 
        WALKABLE cells in the map. I want to modify the cells AROUND 
        the tunnel cells to make the tunnel walls so its still walkable
        """

        #Lay eight walls around each tunnel cell in each direction
        #If the cell that would be placed is a walkable cell, do not 
        #place a wall
        print("tunnelCells: ", self.tunnelCells)
        for walkable in self.tunnelCells:
            for wall in surroundingCells(walkable[0], walkable[1]):
                if wall in self.map and wall not in self.tunnelCells:
                    map[wall[1]][wall[0]] = self.textureValue
    
def createRoom(map: list):
    """
    Create a room: (NxN) empty square of walls
            at a random point in a list map
            that does not overlap with any other 
            filled in squares on the board.
    """
    done = False
    upperBoundSize = len(map) // 6
    lowerBoundSize = len(map) // 10
    while not done:
        size = random.randint(lowerBoundSize, upperBoundSize)
        topLeftX = random.randint(0, len(map[0])-size-1)
        topLeftY = random.randint(0, len(map)-size-1)
        room = Room(size, topLeftX, topLeftY)
        if all(map[y][x] == 0 for x,y in room.walls):
            done = True
            for x,y in room.walls:
                map[y][x] = room.textureValue
    return room

class Level:
    def __init__(self, 
            rows: int,
            cols: int, 
            rooms: int,
            tunnels: int,
            textureValue=1):
        self.map = unaliased2dList(rows, cols, textureValue)
        self.roomWallSets = [createRoom(self.map).walls for i in range(rooms)] #list of sets of (x,y) pairs
        self.tunnels = []
        halfLen = len(self.roomWallSets) // 2
        for s in range(len(self.roomWallSets)) // 2:
            start = random.choice(list(self.roomWallSets[s])) #get a random wall from one room
            end = random.choice(list(self.roomWallSets[s+halfLen])) #get a random wall from the other room
            self.tunnels.append(Tunnel(start, end, self.map, textureValue))
            self.tunnels[-1].setTunnelToMap(self.map)



def createTunnels(map: list):
    """
    Create tunnels between rooms so that all rooms are connected
    """
    pass

if __name__ == "__main__":
    #Test room
    rooms = 25
    m = unaliased2dList(50, 50)
    for r in range(rooms):
        room = createRoom(m)
        
    print2d(m)