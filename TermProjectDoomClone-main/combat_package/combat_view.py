"""
Functions to draw the combat view and experience   

The combat HUD will be 512x768 pixels.

 - drawPerimeter(app, canvas)

 - drawCombatHeadsUpDisplay(app, canvas)
    |- drawActionBar(app, cavas)
    |- drawPlayerStats(app, canvas)
    |- drawEnemyStats(app, canvas)
    |- drawPlayerHPBar(app, canvas)
    |- drawEnemyHPBar(app, canvas)
    |- drawBlockIndicator(app, canvas)
 - drawEnemy()
    |- drawEnemyTexture(app, canvas)
    |- drawEnemyHPBar(app, canvas)
    |- drawEnemyName(app, canvas)


Running this file tests the combat view on a black screen.

When actually run, this combat view will be displayed on 
top of the main view.
"""
from this import d
from cmu_112_graphics import *

class ComView:
    """
    When you want globals but the style guide 
    says no globals >:P
    """
    width = 512
    height = 768
    hudBorder = 5

    appWidth = 1024
    appHeight = 768

    backgroundColor = "black"
    hudColor = "white"
    activeColor = "red"
    combatFont = "Arial 15 bold"
    dialogueFont = "Arial 12 bold"

    
    #Action bar one, bottom left
    actionHeight = 128
    actionWidth = 80
    actionBarx0 = width // 2 + hudBorder * 2
    actionBarx1 = width // 2 + hudBorder * 2 + actionWidth
    actionBary0 = height - actionHeight
    actionBary1 = height - hudBorder * 3
    distBetweenActions = actionHeight // 2

    #Another action bar in the bottom right corner
    actionBarx2 = width // 2 + width - actionWidth - hudBorder * 2
    actionBary2 = height - actionHeight 
    actionBarx3 = actionBarx2 + actionWidth
    actionBary3 = actionBary2 + actionHeight - hudBorder * 3

    #Player stats, inbetween the action bars
    playerStatsx0 = actionBarx1 + hudBorder * 2
    playerStatsy0 = actionBary0  
    playerStatsx1 = actionBarx2 - hudBorder * 2
    playerStatsy1 = actionBary3

    healthBarWidth = (playerStatsx1 - playerStatsx0) - hudBorder * 2
    healthBarHeight = actionHeight // 2
    healthBarx0 = playerStatsx0 + hudBorder * 2
    healthBary0 = (playerStatsy0 + playerStatsy1) // 2
    healthBarx1 = healthBarx0 + healthBarWidth - hudBorder * 2
    healthBary1 = healthBary0 + healthBarHeight - hudBorder * 3

    combatGaguex0 = healthBarx0
    combatGaguey0 = healthBary0 - hudBorder * 2
    combatGaguex1 = healthBarx1
    combatGaguey1 = healthBary0 - hudBorder * 1

    #Upper border health bar
    upperStatsBorderx0 = actionBarx0 - hudBorder * 2
    upperStatsBordery0 = actionBary0 - hudBorder * 2 
    upperStatsBorderx1 = actionBarx3 + hudBorder * 2
    upperStatsBordery1 = actionBary2 - hudBorder * 2

    #Enemy image coords
    enemyImageWidth = 64
    enemyImgx0 = appWidth // 2 - 2 * enemyImageWidth  
    enemyImgy0 = appHeight // 2 - 2 * enemyImageWidth
    enemyImgx1 = appWidth // 2+ 2 * enemyImageWidth
    enemyImgy1 = appHeight // 2 + 2 * enemyImageWidth

    #Enemy stats
    enemyStatsx0 = width // 2 + hudBorder * 2
    enemyStatsy0 = hudBorder * 3
    enemyStatsx1 = 1.5 * width - hudBorder * 2
    enemyStatsy1 = actionHeight - hudBorder * 2

    #Enemy health bar
    enemyHealthBarx0 = playerStatsx0 + hudBorder * 2
    enemyHealthBary0 = (enemyStatsy0 + enemyStatsy1) // 2
    enemyHealthBarx1 = enemyHealthBarx0 + healthBarWidth - hudBorder * 2
    enemyHealthBary1 = enemyHealthBary0 + healthBarHeight - hudBorder * 4
    #Trans rights UwU <3

def drawPerimeter(app, canvas):
    """Draw the perimeter of the HUD"""
    canvas.create_line(
        ComView.width // 2,
        0 + ComView.hudBorder,
        ComView.width // 2,
        ComView.height - ComView.hudBorder,
        fill=ComView.hudColor,
        width=ComView.hudBorder
    )
    canvas.create_line(
        ComView.width // 2,
        0 + ComView.hudBorder,
        ComView.width // 2 + ComView.width,
        0 + ComView.hudBorder,
        fill=ComView.hudColor,
        width=ComView.hudBorder
    )
    canvas.create_line(
        ComView.width // 2 + ComView.width,
        0 + ComView.hudBorder,
        ComView.width // 2 + ComView.width,
        ComView.height - ComView.hudBorder,
        fill=ComView.hudColor,
        width=ComView.hudBorder
    )
    canvas.create_line(
        ComView.width // 2,
        ComView.height - ComView.hudBorder,
        ComView.width // 2 + ComView.width,
        ComView.height - ComView.hudBorder,
        fill=ComView.hudColor,
        width=ComView.hudBorder
    )
def drawActionBar(app, canvas, turn):
    """Draw the action bar containing actions "ATTACK" and "BLOCK"""
    color = ComView.hudColor if not turn else ComView.activeColor
    #Draw the box for it
    canvas.create_rectangle(
        ComView.actionBarx0, ComView.actionBary0,
        ComView.actionBarx1, ComView.actionBary1,
        fill=ComView.backgroundColor, 
        outline=ComView.hudColor, 
        width=ComView.hudBorder
    )
    #Draw the text for attack and defend buttons
    
    canvas.create_text(
        (ComView.actionBarx0 + ComView.actionBarx1) // 2,
        ((ComView.actionBary0 + ComView.actionBary1) // 2) - ComView.distBetweenActions // 2,
        text="1: ATTACK", 
        fill=color, 
        font=ComView.combatFont
    )
    canvas.create_text(
        (ComView.actionBarx0 + ComView.actionBarx1) // 2,
        ((ComView.actionBary0 + ComView.actionBary1) // 2) + ComView.distBetweenActions // 2,
        text="2: BLOCK", 
        fill=color, 
        font=ComView.combatFont
    )
def drawOtherActionBar(app, canvas, turn):
    """Draw another action bar in the bototm right corner"""
    color = ComView.hudColor if not turn else ComView.activeColor
    canvas.create_rectangle(
        ComView.actionBarx2, ComView.actionBary2,
        ComView.actionBarx3, ComView.actionBary3,
        fill=ComView.backgroundColor, 
        outline=ComView.hudColor, 
        width=ComView.hudBorder
    )
    canvas.create_text(
        (ComView.actionBarx2 + ComView.actionBarx3) // 2,
        ((ComView.actionBary2 + ComView.actionBary3) // 2) - ComView.distBetweenActions // 2,
        text="3: FLEE", 
        fill=color, 
        font=ComView.combatFont
    )
    canvas.create_text(
        (ComView.actionBarx2 + ComView.actionBarx3) // 2,
        ((ComView.actionBary2 + ComView.actionBary3) // 2) + ComView.distBetweenActions // 2,
        text="4: ITEMS", 
        fill=color, 
        font=ComView.combatFont
    )
def drawFullBackground(app, canvas):
    canvas.create_rectangle(
        0, 0,
        app.width, app.height,
        fill=ComView.backgroundColor, 
    )
def drawEnemyName(app, canvas, enemy):
    #Draw a rectangle for the enemy name
    canvas.create_rectangle(
        ComView.enemyStatsx0, ComView.enemyStatsy0,
        ComView.enemyStatsx1, ComView.enemyStatsy1,
        fill=ComView.backgroundColor,
        outline=ComView.hudColor,
        width=ComView.hudBorder
    )
    #Draw the enemy name
    canvas.create_text(
        #Center the text
        ((ComView.width // 2 + ComView.hudBorder * 2) + int(1.5 * ComView.width) - ComView.hudBorder * 2) // 2,
        ((ComView.hudBorder * 3 + ComView.actionHeight - ComView.hudBorder * 2) // 2) - ComView.hudBorder * 5,
        text=app.enemy.name,
        fill=ComView.hudColor,
        font=ComView.combatFont
    )
    canvas.create_text(
        #Center the text
        ((ComView.width // 2 + ComView.hudBorder * 2) + int(1.5 * ComView.width) - ComView.hudBorder * 2) // 2,
        ((ComView.hudBorder * 3 + ComView.actionHeight - ComView.hudBorder * 2) // 2) - ComView.hudBorder * 2,
        text=app.enemy.dialogue,
        fill=ComView.hudColor,
        font=ComView.combatFont
    )
def drawEnemyHealth(app, canvas, health, maxHealth=50):
    """Draw a health bar identical to the players health under the enemys name"""
    canvas.create_rectangle(
        ComView.enemyHealthBarx0, ComView.enemyHealthBary0,
        ComView.enemyHealthBarx1, ComView.enemyHealthBary1,
        fill="dark red",
        outline=ComView.backgroundColor,
        width=ComView.hudBorder
    )
    # Draw the current health under the health bar
    if health > 0:
        canvas.create_rectangle(
            ComView.enemyHealthBarx0, ComView.enemyHealthBary0,
            ComView.enemyHealthBarx0 + (health / maxHealth) * ComView.healthBarWidth, ComView.enemyHealthBary1,
            fill="red",
            outline=ComView.backgroundColor,
            width=ComView.hudBorder
        )

def drawVictory(app, canvas, message):
    """Draw the victory screen"""
    canvas.create_rectangle(
        0, 0,
        app.width, ComView.enemyHealthBary1,
        fill=ComView.backgroundColor, 
    )
    
    canvas.create_text(
        app.width // 2,
        ComView.enemyHealthBary1 // 2,
        text=message + " [Press Space to Continue]",
        fill=ComView.hudColor, 
        font=ComView.combatFont
        )

def drawBlinders(app, canvas):
    """Draw black rectangles on the left and right of the perimeter"""
    canvas.create_rectangle(
        0, 0,
        ComView.width // 2, app.height,
        fill="black",
        outline=ComView.hudColor,
        width=ComView.hudBorder
    )
    canvas.create_rectangle(
        ComView.width + ComView.width // 2, 0,
        app.width, app.height,
        fill="black",
        outline=ComView.hudColor,
        width=ComView.hudBorder
    )
def drawPlayerStats(app, canvas, health=90, maxHealth=100):
    """
    draw a rectangle containing player stats inbetween the action bars
    """
    canvas.create_rectangle(
        ComView.playerStatsx0, ComView.playerStatsy0,
        ComView.playerStatsx1, ComView.playerStatsy1,
        fill=ComView.backgroundColor, 
        outline=ComView.hudColor, 
        width=ComView.hudBorder
    )
    #Draw the max health under the health bar
    canvas.create_rectangle(
        ComView.healthBarx0, ComView.healthBary0,
        ComView.healthBarx1, ComView.healthBary1,
        fill="dark red",
        outline=ComView.backgroundColor,
        width=ComView.hudBorder
    )
    # Draw the current health under the health bar
    if health > 0:
        canvas.create_rectangle(
            ComView.healthBarx0, ComView.healthBary0,
            ComView.healthBarx0 + (health / maxHealth) * ComView.healthBarWidth - ComView.hudBorder, ComView.healthBary1,
            fill="red",
            outline=ComView.backgroundColor,
            width=ComView.hudBorder
        )
    canvas.create_line(
        ComView.upperStatsBorderx0, ComView.upperStatsBordery0,
        ComView.upperStatsBorderx1, ComView.upperStatsBordery1,
        fill=ComView.hudColor,
        width=ComView.hudBorder
    )
    #Draw the player's name
    canvas.create_text(
        (ComView.playerStatsx0 + ComView.playerStatsx1) // 2,
        ((ComView.playerStatsy0 + ComView.playerStatsy1) // 2) - ComView.distBetweenActions // 2,
        text=app.playerName,
        fill=ComView.hudColor,
        font=ComView.combatFont
    )
def drawEnemyImg(app, canvas, enemy):

    """Draw the enemy's image"""
    canvas.create_image(
        ComView.enemyImgx0, ComView.enemyImgy0,
        image=app.enemyimg,
        anchor=NW
    )

def drawCombatGague(app, canvas, player):
    #Max combat gauge
    canvas.create_rectangle(
        ComView.combatGaguex0, ComView.combatGaguey0,
        ComView.combatGaguex1, ComView.combatGaguey1,
        fill="Blue"
    )
    #Current combat gauge
    canvas.create_rectangle(
        ComView.combatGaguex0, ComView.combatGaguey0,
        ComView.combatGaguex0 + player.gague * ComView.hudBorder, ComView.combatGaguey1,
        fill="Sky Blue"
    )

def drawCombatHeadsUpDisplay(app, canvas, player, enemy):
    # drawFullBackground(app, canvas)
    drawEnemyName(app, canvas, enemy)
    drawEnemyHealth(app, canvas, enemy.hitpoints, enemy.maxHitpoints)
    drawPerimeter(app, canvas)
    drawActionBar(app, canvas, player.isTurn)
    drawOtherActionBar(app, canvas, player.isTurn)
    drawPlayerStats(app, canvas, player.hitpoints, player.maxHitpoints)
    drawBlinders(app, canvas)
    drawEnemyImg(app, canvas, app.enemyimg)
    drawCombatGague(app, canvas, player)
    if app.victory: drawVictory(app, canvas, app.victoryMessage)

def redrawAll(app, canvas):
    drawCombatHeadsUpDisplay(app, canvas, 50, 25)

if __name__ == "__main__":
    runApp(width=1024, height=768)
