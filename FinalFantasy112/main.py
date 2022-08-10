
from combat.combat_events import combatKeyPressed, combatTimerFired, victoryKeyPressed
from graphics.view import View, randomEncounter, viewKeyPressed
from graphics.cast import cast
from cmu_112_graphics import *
from graphics.environments import *
import math
from graphics.textures import *
from tkinter import PhotoImage
from PIL import ImageTk
from levels.towerlevel import *
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



###### MODEL ######
def appStarted(app):
    app.view = View(WALLS, CEILING, FLOORS)
    app.player = Player(app.view, [], 25, 95, 3)
    app.playerName = "PLAYER_NAME"
    app.lines = cast(app)
    
    # app.enemy = Enemy("str", 10, 50, 3)
    # try:
    #     app.enemyimg = PhotoImage(file=f"images/{app.enemy.name}.png")
    # except Exception as e:
    #     print(e)
    #     app.enemyimg = PhotoImage(file="images/orc.png")
    #SET THE TEXTURE PACK
    app.tp = TEST1
    app.colors = app.tp.wallTextures
    app.floorTexture = app.tp.floor
    app.ceilingTexture = app.tp.ceiling

    app.complements = app.tp.horizontalWallTextures

    app.miniMapState = False
    app.miniMapCellWidth = 10
    app.miniMapCellHeight = 10


    #STATES 
    app.isCombat = False
    app.victory = False
    app.victoryMessage = ""
    app.player.gague = 10

#### END MODEL ####

##### CONTROLLER #####
def keyPressed(app, event):
    if event.key == "p":
        randomEncounter(app, app.player, p=1)
    if app.isCombat:
        combatKeyPressed(app, event)
    
    elif app.victory:
        victoryKeyPressed(app, event)

    elif  not app.isCombat:
        viewKeyPressed(app, event)
        app.lines = cast(app)

    

def timerFired(app):
    combatTimerFired(app)

#### END CONTROLLER ####

#### VIEW ####
def getMiniMapCellBounds(app, row, col) -> tuple:
    """
    Return the bounds of the cell in the minimap at the given row and column
    """
    return (
        col * app.miniMapCellWidth,
        row * app.miniMapCellHeight,
        (col + 1) * app.miniMapCellWidth,
        (row + 1) * app.miniMapCellHeight
    )

def drawMiniMap(app, canvas):
    """
    Portray the environment in a grid minimap in the upper left corner
    """
    for row in range(len(app.view.map)):
        for col in range(len(app.view.map[row])):
            x0, y0, x1, y1 = getMiniMapCellBounds(app, row, col)
            temp = app.colors[app.view.map[row][col]] 
            if type(temp) == list:
                color = temp[1]
            else:
                color = temp
            canvas.create_rectangle(x0, y0, x1, y1, fill=color)

    #Draw the player position in the minimap
    x0, y0, x1, y1 = getMiniMapCellBounds(app, 
            int(app.view.posX), int(app.view.posY))
    canvas.create_oval(x0, y0, x1, y1, fill="yellow")

    #Draw the player's view in the minimap as a line starting
    #at the players position going in the direction of the plaers visionx
    canvas.create_line(x0, y0, x1, y1, fill="yellow")
    
def drawCeiling(app, canvas):
    #Draw a horizontal line one pixel wide from the top of the screen
    #to halfway down the screen of each color in the ceiling texture
    # repeat the texture for half the height of the screen

    #Get the current player coords as idx
    x = int(app.view.posX)
    y = int(app.view.posY)

    #Get the current player's ceiling texture
    colors = app.colors[app.view.mapCeilings[x][y]]
    for pixel in range(app.height // 2):    
        cidx = pixel % len(colors)
        color = colors[cidx]
        canvas.create_line(0, pixel, app.width, pixel, fill=color)

def drawFloor(app, canvas):
    #Draw a horizontal line one pixel wide from the bottom of the screen
    #to halfway up the screen of each color in the floor texture
    # repeat the texture for half the height of the screen

    #Get the current player coords as idx
    x = int(app.view.posX)
    y = int(app.view.posY)
    #Get the current player's floor texture

    colors = app.colors[app.view.mapFloors[x][y]]
    for pixel in range(app.height // 2, app.height):    
        cidx = pixel % len(colors)
        color = colors[cidx]
        canvas.create_line(0, pixel, app.width, pixel, fill=color)

def drawLines(app, canvas):
    for line in app.lines:

        #Vertical line from raycasting
        startX = line[0]
        startY = line[1]
        endX = line[2]
        endY = line[3]
        color = app.colors[line[4]][app.lines.index(line) % len(app.colors[line[4]])]

        #Draw the Vertical texture
        canvas.create_line(startX, startY, endX, endY, fill=color)



def redrawAll(app, canvas):
    drawFloor(app, canvas)
    drawCeiling(app, canvas)
    drawLines(app, canvas)

    if app.miniMapState: 
        drawMiniMap(app, canvas)
    if app.isCombat and not app.victory:
        drawCombatHeadsUpDisplay(app, canvas, app.player, app.enemy)
    if app.victory:
        drawVictory(app, canvas, app.victoryMessage)

#### END VIEW #######

#main
def main():
    runApp(width=1024, height=768)

if __name__ == "__main__":
    main()