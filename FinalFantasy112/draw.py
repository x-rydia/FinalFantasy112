def getMiniMapCellBounds(app, row, col) -> tuple:
    """
    Return the bounds of the cell in the minimap at the given row and column
    """
    shift = app.width // 8
    return (
        shift + col * app.miniMapCellWidth,
        row * app.miniMapCellHeight,
        shift + (col + 1) * app.miniMapCellWidth,
        (row + 1) * app.miniMapCellHeight
    )

def drawMiniMap(app, canvas):
    """
    Portray the environment in a grid minimap in the upper left corner
    """
    for row in range(len(app.view.map)):
        for col in range(len(app.view.map[row])):
            x0, y0, x1, y1 = getMiniMapCellBounds(app, row, col)
            temp = app.colors[app.view.map[row][col]] if app.view.map[row][col] != 0 else "Black"
            if type(temp) == list:
                color = temp[1]
            else:
                color = temp
            canvas.create_rectangle(x0, y0, x1, y1, fill=color)

    #Draw the player position in the minimap
    x0, y0, x1, y1 = getMiniMapCellBounds(app, 
            int(app.view.posX), int(app.view.posY))
    canvas.create_oval(x0, y0, x1, y1, fill="yellow")

    
def drawCeiling(app, canvas):
    #draw a ceiling rectagle
    canvas.create_rectangle(0, 0, app.width, app.height // 2, fill="Black")

def drawFloor(app, canvas, img=False):
    #draw a floor rectagle
    if img:
        canvas.create_image(0, app.height // 2, image=app.floorImg, anchor="nw")
    else:
        canvas.create_rectangle(0, app.height // 2, app.width, app.height, fill="gray2")

def drawLines(app, canvas, image=False):
    for line in app.lines:

        #Vertical line from raycasting
        startX = line[0]
        startY = line[1]
        endX = line[2]
        endY = line[3]
        color = app.colors[line[4]][app.lines.index(line) % len(app.colors[line[4]])]

        #Draw the Vertical texture
        canvas.create_line(startX, startY, endX, endY, fill=color)
