
import math, random
from combat.combat import *
from PIL import ImageTk
from cmu_112_graphics import *
from roguelike import *
class View:
    def __init__(self, body, x, y, app) -> None:
        self.app = app

        #map vars
        self._width = 1024
        self._height = 768 
        self.map = body 
        #player vars
        
        #These are constants
        self._movSpeed = .1
        self._rotSpeed = 0.075

        #These are not
        self.posX = x
        self.posY = y
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
        #Do a rotation matrix, but not in a matrix
        oldy = self.dirY
        #x1 = x0 * cos(theta) - y0 * sin(theta)
        self.dirX = self.dirX * math.cos(theta) - oldy * math.sin(theta)
        #y1 = x0 * sin(theta) + y0 * cos(theta)
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
    
    # def increaseCameraPitch(self):
    #     #Increase the camera pitch
    #     self.absY += self.regTurnY * self._movSpeed
    # def decreaseCameraPitch(self):
    #     #Decrease the camera pitch
    #     self.absY -= self.invTurnY * self._movSpeed


    def moveForward(self):
        #Move the player forward (NOT ROTATION)
        mapX = int(self.posX + self.dirX * self._movSpeed)
        mapY = int(self.posY + self.dirY * self._movSpeed)
        if self.map[mapX][mapY] == 0:
            self.posX += self.dirX * self._movSpeed
            self.posY += self.dirY * self._movSpeed

        if self.map[mapX][mapY] == 5:
            self.app.newLevel = True
            self.app.score += 1
    
    def moveBack(self):
        #Move the player backward (NOT ROTATION)
        mapX = int(self.posX - self.dirX * self._movSpeed)
        mapY = int(self.posY - self.dirY * self._movSpeed)
        if self.map[mapX][mapY] == 0:
            self.posX -= self.dirX * self._movSpeed
            self.posY -= self.dirY * self._movSpeed
        
        if self.map[mapX][mapY] == 5:
            self.app.newLevel = True
            self.app.score += 1 
            

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

def randomEncounter(app, player, p=0.005) -> None:
    """
    Given a random chance of fighting an enemy, 
    update the app state to reflect combat
    """
    if random.random() < p:
        app.enemy = Enemy(
            attack=10 + app.score,
            hitpoints=50 + 5*app.score,
            defense=0 
        )
        app.enemyimg = ImageTk.PhotoImage(app.loadImage(f"./images/{app.enemy.name.lower()}.png"))
        app.isCombat = True
        app.victory = False
        
    else:
        pass

def viewKeyPressed(app, event):
    if event.key == "w":
        app.view.moveForward()
        randomEncounter(app, app.player)
    elif event.key == "s":
        app.view.moveBack()
    elif event.key == "a":
        app.view.lookRight()
    elif event.key == "d":
        app.view.lookLeft()
    elif event.key == "m":
        app.miniMapState = not app.miniMapState
    elif event.key == "n":
        app.newLevel = True