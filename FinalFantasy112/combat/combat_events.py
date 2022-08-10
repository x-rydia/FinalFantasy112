"""
Store functions that will be called in main events depending on the
state of the app.

If the app has state combat=True, then the functions in this module
will be called in KeyPressed and mousePressed.
"""

from combat.combat import Player, Enemy 

def combatKeyPressed(app, event):
    if app.enemy.isDead():
        app.victory = True
        return 

    if event.key == "2":
        if app.player.isTurn:
            #Player turn
            app.player.toggleBlock()
            app.player.resetGague()
            #Enemy turn
            app.enemy.attackEntity(app.player)

    elif event.key == "1":
        if app.player.isTurn:
            #Player turn
            damage = app.player.attackEntity(app.enemy)
            app.enemy.dialogue = f"You attacked dealing {damage} damage"
            app.player.resetGague()
            if app.enemy.isDead():
                app.victory = True
                app.victoryMessages = [
                    f"Congratulations, {app.playerName}! You have defeated {app.enemy.name}!",
                    f"This is another message from {app.enemy.name}",
                    f"This is a third message from {app.enemy.name}",
                    f"This is a fourth message from {app.enemy.name}"

                ]
                app.isCombat = False
                return 
                #Enemy turn
            app.enemy.attackEntity(app.player)
            
    
    elif event.key == "3":
        if app.player.isTurn:
            app.player.resetGague()
            app.enemy.attackEntity(app.player)
            if app.player.flee():
                app.isCombat = False
                return 
                
    
    elif event.key == "4":
        app.player.openInventory()
    
    elif event.key == "5":
        app.isCombat = False
    else:
        pass
    
def combatTimerFired(app):
    if not app.isCombat: 
        return
    if not app.player.isTurn: 
        app.player.gagueUp()


def victoryKeyPressed(app, event):
    if event.key == "Space":
        if len(app.victoryMessages) == 0:
            app.isCombat = False
            app.victory = False
            app.victoryMessage = ""
            return
        app.victoryMessage = app.victoryMessages.pop(0)
