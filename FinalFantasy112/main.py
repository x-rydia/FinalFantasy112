
from combat.combat_events import combatKeyPressed, combatTimerFired, victoryKeyPressed
from graphics.view import View, randomEncounter, viewKeyPressed
from graphics.cast import cast, getImageLines
from cmu_112_graphics import *
from graphics.environments import *
import math
from graphics.textures import *
from tkinter import PhotoImage
from PIL import ImageTk

from combat.combat_view import *
from combat.combat import *
#There is an error in tkinter that causes a crash due
#to recursion depth. IT likely has something to do withw
#The number of lines on the screen.
#This is a workaround, I have yet to get the same error 
#now that I increased the limit

#This bug fix came from: https://stackoverflow.com/questions/3323001/what-is-the-maximum-recursion-depth-in-python-and-how-to-increase-it
import sys 
sys.setrecursionlimit(100000)

from levelbuilder.roguelike import *
from draw import *


###### MODEL ######
def appStarted(app, title=True):
    app.score = 0
    app.rows = 15 + 3*app.score
    app.cols = 15 + 3*app.score
    app.level = Level(app.rows, app.cols, 10, 100, 3)
    x, y = app.level.spawnPlayer()
    app.level.placeDoor()

    app.view = View(app.level.map, x, y, app)
    app.player = Player(app.view, [], 25, 95, 3)
    app.playerName = ""
    app.lines = cast(app)

    app.tp = TEST1
    app.colors = app.tp.wallTextures
    app.floorTexture = app.tp.floor
    app.ceilingTexture = app.tp.ceiling
    app.floorImg = ImageTk.PhotoImage(app.loadImage("images/floorimg.png"))

    if title: app.title = True 

    app.complements = app.tp.horizontalWallTextures

    app.miniMapState = False
    app.miniMapCellWidth = app.height // app.cols
    app.miniMapCellHeight = app.height // app.rows


    #STATES 
    app.isCombat = False
    app.victory = False
    app.isView = False if title == True else True 
    app.isDocs = False
    app.isTutorial = False
    app.gameOver = False
    app.victoryMessage = ""
    app.player.gague = 10
    app.newLevel = False

def partialRestart(app):
    """
    reset level but not player
    """
    app.rows = 15 + 3*app.score
    app.cols = 15 + 3*app.score
    app.level = Level(app.rows, app.cols, 10, 100, 3)
    app.miniMapCellWidth = app.height // app.cols
    app.miniMapCellHeight = app.height // app.rows

    x, y = app.level.spawnPlayer()
    app.level.placeDoor() 
    app.view = View(app.level.map, x, y, app)
    app.lines = cast(app)


#### END MODEL ####

##### CONTROLLER #####
def keyPressed(app, event):
    if app.title: 
        titleKeyPressed(app, event) 
    elif event.key == "g":
        app.gameOver = True
    elif app.newLevel: 
        app.newLevel = False
        partialRestart(app)
    elif app.isTutorial:
        tutorialKeyPressed(app, event)
    elif event.key == "n":
        appStarted(app, title=False)
    elif event.key == "p":
        randomEncounter(app, app.player, p=1)
    elif app.isCombat:
        combatKeyPressed(app, event)
    
    elif app.victory:
        victoryKeyPressed(app, event)
    elif app.gameOver:
        if event.key == "Space":
            print("restart")
            app.gameOver = False
            appStarted(app, title=True)
    else:
        viewKeyPressed(app, event)
        app.lines = cast(app)

def timerFired(app):
    combatTimerFired(app)

def mousePressed(app, event):
    if app.title: 
        titleMousePressed(app, event)

def redrawAll(app, canvas):
    if app.title:
        titleRedrawAll(app, canvas)

    elif app.isCombat:
        drawFloor(app, canvas, img=False)
        drawCeiling(app, canvas)
        drawLines(app, canvas, image=False)

        if app.isCombat and not app.victory:
            drawCombatHeadsUpDisplay(app, canvas, app.player, app.enemy)
    elif app.gameOver:
        drawGameOver(app, canvas)

    elif app.victory:
        drawFloor(app, canvas, img=False)
        drawCeiling(app, canvas)
        drawLines(app, canvas, image=False)
        drawVictory(app, canvas, app.victoryMessage)

    elif app.isView:
        drawFloor(app, canvas, img=False)
        drawCeiling(app, canvas)
        drawLines(app, canvas, image=False)
        drawViewHUD(app, canvas, app.player)
        if app.miniMapState:
            drawMiniMap(app, canvas)
    
    elif app.isDocs:
        pass

    elif app.isTutorial:
        drawTutorial(app, canvas)

#### END VIEW #######

#main
def main():
    runApp(width=1024, height=768)


if __name__ == "__main__":
    main()