from view import View
from cast import cast
from cmu_112_graphics import *
from environments import *
import math

from textures import *

###### MODEL ######
def appStarted(app):
    app.view = View(map1, False)
    app.lines = cast(app)
    app.colors = {
        0: "white",
        1: WOOD_PLANK,
        2: STONE_BRICK,
        3: "blue",
    }
    app.miniMapState = False
    app.miniMapCellWidth = 10
    app.miniMapCellHeight = 10
#### END MODEL ####

##### CONTROLLER #####
def keyPressed(app, event):
    #Move or rotate the player and then cast new rays
    if event.key == "w":
        app.view.moveForward()

    elif event.key == "s":
        app.view.moveBack()

    elif event.key == "d":
        app.view.moveLeft()

    elif event.key == "a":
        app.view.moveRight()

    elif event.key == "Right":
        app.view.lookLeft()

    elif event.key == "Left":
        app.view.lookRight()

    elif event.key == "m":
        app.miniMapState = not app.miniMapState
    else:
        pass
    app.lines = cast(app)

# def timerFired(app):
#     app.lines = cast(app)

#### END CONTROLLER ####

#### VIEW ####
def drawFLoor(app, canvas):
    canvas.create_rectangle(0, app.height // 2, app.width, app.height, fill="black")

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
                color = temp[0]
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
    
def drawSky(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height // 2, fill="Sky Blue")

import random
def drawLines(app, canvas):
    for line in app.lines:
        startX = line[0]
        startY = line[1]
        endX = line[2]
        endY = line[3]
        color = app.colors[line[4]][app.lines.index(line) % len(app.colors[line[4]])]
        canvas.create_line(startX, startY, endX, endY, fill=color)

def redrawAll(app, canvas):

    drawFLoor(app, canvas)
    drawSky(app, canvas)
    drawLines(app, canvas)
    if app.miniMapState: #if the minimap is open
        drawMiniMap(app, canvas)
#### END VIEW #######

#main
def main():
    runApp(width=1024, height=768)

if __name__ == "__main__":
    main()