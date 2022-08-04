


from cmu_112_graphics import *

def appStarted(app):
    app.nRows = 50
    app.nCols = 50
    app.cellSize = 17
    app.margin = 3

    app.currentGrid = "Walls"
    #define empty map
    app.mapWalls = [
        [0 for c in range(app.nCols)] for r in range(app.nRows)
    ]
    app.mapFloors = [
        [5 for c in range(app.nCols)] for r in range(app.nRows)
    ]
    app.mapCeilings = [
        [1 for c in range(app.nCols)] for r in range(app.nRows)
    ]

    app.gridDict = {
        "Walls": app.mapWalls,
        "Floors": app.mapFloors,
        "Ceilings": app.mapCeilings
    }

    #define current selected int  
    app.selectedTextureInt = 0
    app.textureDict = {
        0: "White",
        1: "Sky Blue",
        2: "Brown",
        3: "Gray",
        4: "Dark Gray",
        5: "Green",
        6: "Dark Green"
        7; "Sienna"
    }

def clickToGrid(app, x, y):
    #convert x,y to grid coords
    row = int((y // app.cellSize) - app.margin)
    col = int((x // app.cellSize) - app.margin)
    return row, col

def gridToPixel(app, row, col):
    #convert grid coords to pixel coords
    x = (col + app.margin) * app.cellSize
    y = (row + app.margin) * app.cellSize
    x1 = (col + app.margin + 1) * app.cellSize
    y1 = (row + app.margin + 1) * app.cellSize
    return x, y, x1, y1

def mousePressed(app, event):
    #set the grid cell to the selected texture
    row, col = clickToGrid(app, event.x, event.y)
    if row > len(app.gridDict[app.currentGrid]) - 1 or col > len(app.gridDict[app.currentGrid][row]) - 1:
        return
    if app.currentGrid == "Walls":
        app.mapWalls[row][col] = app.selectedTextureInt
    elif app.currentGrid == "Floors":
        app.mapFloors[row][col] = app.selectedTextureInt
    elif app.currentGrid == "Ceilings":
        app.mapCeilings[row][col] = app.selectedTextureInt
    else:
        pass

def keyPressed(app, event):
    if event.key == "p":
        #Print the current grid in a way that can be copied and pasted into a level
        print()
        for row in app.gridDict[app.currentGrid]:
            print(row, end=",\n")
    if event.key == "w":
        app.currentGrid = "Walls"
    elif event.key == "f":
        app.currentGrid = "Floors"
    elif event.key == "c":
        app.currentGrid = "Ceilings"
    elif event.key == "0":
        app.selectedTextureInt = 0
    elif event.key == "1":
        app.selectedTextureInt = 1
    elif event.key == "2":
        app.selectedTextureInt = 2
    elif event.key == "3":
        app.selectedTextureInt = 3
    elif event.key == "4":
        app.selectedTextureInt = 4
    elif event.key == "5":
        app.selectedTextureInt = 5
    
    else:
        pass


def drawCurrentGrid(app, canvas, mode):
    for r in range(len(app.gridDict[mode])):
        for c in range(len(app.gridDict[mode][r])):
            x0, y0, x1, y1 = gridToPixel(app, r, c)
            color = app.textureDict[app.gridDict[mode][r][c]]
            canvas.create_rectangle(x0, y0, x1, y1, fill=color)

def drawGridRowColIndexes(app, canvas):
    for r in range(len(app.gridDict[app.currentGrid])):
        canvas.create_text(app.margin * app.cellSize, (r + app.margin) * app.cellSize, text=str(r))
        canvas.create_text((app.nCols + app.margin) * app.cellSize, (r + app.margin) * app.cellSize, text=str(r), font="Arial 10")
    for c in range(len(app.gridDict[app.currentGrid][0])):
        canvas.create_text((c + app.margin) * app.cellSize, app.margin * app.cellSize, text=str(c))
        canvas.create_text((c + app.margin) * app.cellSize, (app.nRows + app.margin) * app.cellSize, text=str(c), font="Arial 10")
def drawInfo(app, canvas):
    canvas.create_text(3*app.width//4, 3*app.height//4, text="Current Grid: " + app.currentGrid)
    canvas.create_text(3*app.width//4, app.height//2 + 20, text="Current Texture: " + app.textureDict[app.selectedTextureInt])

def redrawAll(app, canvas):
    drawCurrentGrid(app, canvas, app.currentGrid)
    drawGridRowColIndexes(app, canvas)
    drawInfo(app, canvas)

if __name__ == "__main__":
    runApp(width=800, height=600)