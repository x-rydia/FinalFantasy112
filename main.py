"""
Main file for 15-112 term project, Doom clone
"""

from cmu_112_graphics import *

class Player:
    def __init__(self,
            pos: tuple(int, int),
            fov: float, #Degrees
        ) -> None:
        self.pos = pos
        self.fov = fov
        
    def castRays(self, app: App, n: int=10) -> list:
        """
        Cast n rays 
        """
        dAngle = self.fov / n
        

def appStarted(app):
    app.mapSqrSize = 10
    app.env = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
    #We need to cast "rays" in sixty degree FOV from a player position
    app.emptyColor = "White"
    app.envColor = "Blue"

def keyPressed(app, event):
    pass

def getMapCellBounds(app, row, col):
    x0 = col * app.mapSqrSize
    y0 = row * app.mapSqrSize
    x1 = (col+1) * app.mapSqrSize
    y1 = (row+1) * app.mapSqrSize
    return x0, y0, x1, y1


def drawEnvironment(app, canvas):
    """
    Draw the environment and player location in the upper left hand corner
    of the screen.
    """
    for row in range(len(app.env)):
        for col in range(len(app.env[row])):
            fill = app.envColor if app.env[row][col] else app.emptyColor
            x0, y0, x1, y1 = getMapCellBounds(app, row, col)
            canvas.create_rectangle(x0, y0, x1, y1, fill=fill)
            

def redrawAll(app, canvas):
    pass

def main():
    runApp(width=500, height=500)

if __name__ == "__main__":
    main()

