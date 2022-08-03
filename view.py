
import math

class View:
    def __init__(self, 
            body, 
            testBody=False) -> None:
        #Test map
        testMap = [ 
            [1,1,1,1,1,1,1,1,1,1,1,1],
            [2,0,0,0,0,0,0,0,0,0,0,3],
            [1,1,1,1,1,0,0,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1]
        ]

        #map vars
        self._width = 1024
        self._height = 768 
        self.map = body if not testBody else testMap
        
        #player vars
        
        #These are constants
        self._movSpeed = .25
        self._rotSpeed = 0.05

        #These are not
        self.posX = 1.0
        self.posY = 1.0
        self.dirX = 1.0
        self.dirY = 0.0
        self.absX = 0.0
        self.absY = .66

        #turning constants

        self.regTurnX = math.cos(self._rotSpeed)
        self.regTurnY = math.sin(self._rotSpeed)
        self.invTurnX = math.cos(-self._rotSpeed)
        self.invTurnY = math.sin(-self._rotSpeed)
    
    def rotate(self, theta):
        #Rotate the player view
        oldy = self.dirY
        self.dirX = self.dirX * math.cos(theta) - oldy * math.sin(theta)
        self.dirY = self.dirX * math.sin(theta) + oldy * math.cos(theta)
        #Rotate camera view
        oldAbsy = self.absY
        self.absX = self.absX * math.cos(theta) - oldAbsy * math.sin(theta)
        self.absY = self.absX * math.sin(theta) + oldAbsy * math.cos(theta)

    def lookLeft(self):
        #rotate the player view to the left
        stepAngle = self._rotSpeed
        self.rotate(stepAngle)
    
    def lookRight(self):
        #rotate the player view to the right
        stepAngle = -self._rotSpeed
        self.rotate(stepAngle)

    def moveForward(self):
        #Move the player forward (NOT ROTATION)
        #TODO: make this prettier and more readable
        if not self.map[int(self.posX + self.dirX * self._movSpeed)][int(self.posY)]:
            self.posX += self.dirX * self._movSpeed
        if not self.map[int(self.posX)][int(self.posY + self.dirY * self._movSpeed)]:
            self.posY += self.dirY * self._movSpeed
    
    def moveBack(self):
        #Move the player backward (NOT ROTATION)
        #TODO: make this prettier and more readable
        if not self.map[int(self.posX - self.dirX * self._movSpeed)][int(self.posY)]:
            self.posX -= self.dirX * self._movSpeed
        if not self.map[int(self.posX)][int(self.posY - self.dirY * self._movSpeed)]:
            self.posY -= self.dirY * self._movSpeed
    
    def moveLeft(self): 
        #Move the player left (NOT ROTATION)
        if not self.map[int(self.posX - self.dirX * self._movSpeed)][int(self.posY)]:
            self.posX -= self.dirX * self._movSpeed
        if not self.map[int(self.posX)][int(self.posY + self.dirY * self._movSpeed)]:
            self.posY += self.dirY * self._movSpeed
     
    def moveRight(self):
        #Move the player right (NOT ROTATION)
        if not self.map[int(self.posX + self.dirX * self._movSpeed)][int(self.posY)]:
            self.posX += self.dirX * self._movSpeed
        if not self.map[int(self.posX)][int(self.posY - self.dirY * self._movSpeed)]:
            self.posY -= self.dirY * self._movSpeed