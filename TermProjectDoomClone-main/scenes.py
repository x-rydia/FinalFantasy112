"""
FIle to contain functions that draw various scenes in the game.
"""
import time


def resetScreen(app, canvas):
    """
    For each pixel of the screen height, draw one horizontal line of length app.width
    from left to right every tenth of a second 
    """
    canvas.creae_rectangle(0, 0, app.width, app.height, fill="black")
