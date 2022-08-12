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
            canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=0)

    #Draw the player position in the minimap
    x0, y0, x1, y1 = getMiniMapCellBounds(app, 
            int(app.view.posX), int(app.view.posY))
    canvas.create_oval(x0, y0, x1, y1, fill="yellow", width = 0)

    
def drawCeiling(app, canvas):
    #draw a ceiling rectagle
    canvas.create_rectangle(0, 0, app.width, app.height // 2, fill="black")

def drawFloor(app, canvas, img=False):
    #draw a floor rectagle
    if img:
        canvas.create_image(0, app.height // 2, image=app.floorImg, anchor="nw")
    else:
        canvas.create_rectangle(0, app.height // 2, app.width, app.height, fill="snow3")

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


def titleRedrawAll(app, canvas, ):
    """
    draw a title screen for the game
    """
    canvas.create_rectangle(0, 0, app.width, app.height, fill="black")
    canvas.create_text(app.width // 2, app.height // 4, text="The Backrooms of 112", fill="white", font="Arial 30")

    #docs button
    canvas.create_rectangle(
        app.width // 2 - app.width // 4, 
        app.height // 2, 
        app.width // 2 + app.width // 4,
        app.height // 2 + app.height // 12, 
        fill="Black", outline="white", width=5
    )
    #Docs button text centered in the button
    canvas.create_text(
        app.width // 2,
        app.height // 2 + app.height // 24,
        text="Play Game",
        fill="white",
        font="Arial 20",
        anchor= "c"
    )

    # tutorial button
    canvas.create_rectangle(
        app.width // 2 - app.width // 4,
        app.height // 2 + app.height // 12 + app.height // 24,
        app.width // 2 + app.width // 4,
        app.height // 2 + 2 * (app.height // 12) + app.height // 24,
        fill="Black", outline="white", width=5
    )
    # tutorial button text centered in the button
    canvas.create_text(
        app.width // 2,
        #avg of the y0 y1 of the tutorial button,
        ((app.height // 2 + 2 * (app.height // 12) + app.height // 24) + (app.height // 2 + app.height // 12 + app.height // 24)) // 2,
        text="Read Tutorial",
        fill="white",
        font="Arial 20",
        anchor= "c"
    )

    # read docs button
    canvas.create_rectangle(
        app.width // 2 - app.width // 4,
        app.height // 2 + 2 * (app.height // 12) + 2 * app.height // 24,
        app.width // 2 + app.width // 4,
        app.height // 2 + 3 * (app.height // 12) + 2 * app.height // 24,
        fill="Black", outline="white", width=5
    )
    # read docs button text centered in the button
    canvas.create_text(
        app.width // 2,
        #avg of the y0 y1 of the read docs button,
        ((app.height // 2 + 3 * (app.height // 12) + 2 * app.height // 24) + (app.height // 2 + 2 * (app.height // 12) + 2 * app.height // 24)) // 2,
        text="Read Documenation",
        fill="white",
        font="Arial 20",
        anchor= "c"
    )

def titleMousePressed(app, event):
    x, y = event.x, event.y
    #detect if the user clicked on the docs button

    playMinY = app.height // 2
    playMaxY = app.height // 2 + app.height // 12

    tutorialMinY = app.height // 2 + app.height // 12 + app.height // 24
    tutorialMaxY = app.height // 2 + 2 * (app.height // 12) + app.height // 24

    readDocsMinY = app.height // 2 + 2 * (app.height // 12) + 2 * app.height // 24
    readDocsMaxY = app.height // 2 + 3 * (app.height // 12) + 2 * app.height // 24
    if x > app.width // 2 - app.width // 4 and x < app.width // 2 + app.width // 4:
        if playMinY < y < playMaxY:
            app.title = False
            app.isView = True 
        elif tutorialMinY < y < tutorialMaxY:
            app.title = False
            app.isTutorial = True
        elif readDocsMinY < y < readDocsMaxY:
            app.title = False
            app.isDocs = True

def drawViewHUD(app, canvas, player):
    """
    Draw a HUD for the main view that shows the 
    player's health bar, attack, and defense 
    """
    #draw container lines for the HUD
    canvas.create_line(0, app.height - app.height // 6, app.width, 
        app.height - app.height // 6, fill="Black", width=5)
        
    #Draw lines separating the hud into three regions
    #first is one sixth of the width,
    #second is one third of the width,
    #third is five sixths of the width
    canvas.create_line(app.width // 6, app.height - app.height // 6, app.width // 6, app.height, fill="Black", width=5)
    canvas.create_line(5 * app.width // 6, app.height - app.height // 6, 5 * app.width // 6, app.height, fill="Black", width=5)

    #draw the health bar in the middle of the second region
    healthx0 = app.width // 3
    healthx1 = 2 * app.width // 3
    healthy0 = app.height - app.height // 12
    healthy1 = app.height - app.height // 48
    canvas.create_rectangle(healthx0, healthy0, healthx1, healthy1, fill="Dark Red", outline="black", width=5)
    #draw the health bar fill
    canvas.create_rectangle(healthx0, healthy0, healthx0 + player.hitpoints * (healthx1 - healthx0) // player.maxHitpoints, healthy1, fill="red", outline="black", width=5)

    #draw the player name above the health bar
    canvas.create_text(app.width // 2, healthy0 - 15, text=app.playerName, fill="black", font="Arial 20 bold", anchor= "c")
    #draw the player's attack in the left section
    canvas.create_text(
        app.width // 12, app.height - app.height // 8, 
        text="ATTACK: " + str(player.attack), 
        fill="black", font="Arial 20 bold", anchor= "c"
        )
    #draw the player's defense in the left section below the attack
    canvas.create_text(
        app.width // 12, 
        app.height - app.height // 12 + app.height // 24, 
        text="DEFENSE: " + str(player.defense), 
        fill="black", font="Arial 20 bold", anchor= "c"
        )