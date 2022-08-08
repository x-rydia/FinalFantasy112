import math


def cast(app) -> list:
    """
    return the list of all the lines to be drawn as
    determined by raycasting 

    https://lodev.org/cgtutor/raycasting.html
    
    https://en.wikipedia.org/wiki/Digital_differential_analyzer_(graphics_algorithm)
    """
    coordinates = []
    for i in range(app.view._width): 
        mapX = int(app.view.posX)
        mapY = int(app.view.posY)
        plrX = (2*i) / app.view._width - 1
        rayDirX = app.view.dirX + app.view.absX * plrX + 0.00001

        #avoid zero division error with raydiry
        rayDirY = app.view.dirY + app.view.absY * plrX + 0.00001 

        #calculate slope of ray
        dx = math.sqrt(1 + rayDirY**2/rayDirX**2)
        dy = math.sqrt(1 + rayDirX**2/rayDirY**2)
        
        #Handle negative slopes
        if rayDirX < 0:
            stepX = -1
            sideDistX = (app.view.posX - mapX) * dx
        else:
            stepX = 1
            sideDistX = (mapX + 1.0 - app.view.posX) * dx
        if rayDirY < 0:
            stepY = -1
            sideDistY = (app.view.posY - mapY) * dy
        else:
            stepY = 1
            sideDistY = (mapY + 1.0 - app.view.posY) * dy
        
        #Cast the ray
        contact = False
        while not contact:
            if sideDistX < sideDistY:
                sideDistX += dx
                mapX += stepX
                side = 0
            else:
                sideDistY += dy
                mapY += stepY
                side = 1
            if app.view.map[mapX][mapY] != 0:
                contact = True

        #Calculate the distance to the wall
        if side == 0:
            perpWallDist = abs((mapX - app.view.posX + (1 - stepX) / 2) / rayDirX)
        else:
            perpWallDist = abs((mapY - app.view.posY + (1 - stepY) / 2) / rayDirY)
        
        #Calculate the height of the line on the screen
        h = abs(int(app.view._height / (perpWallDist + 0.00001)))

        #Calculate the lowest and highest pixel to fill in the line
        drawStart = int(app.view._height / 2 - h / 2)
        drawEnd = int(app.view._height / 2 + h / 2)

        if drawStart < 0: 
            drawStart = 0
        if drawEnd >= app.view._height:
            drawEnd = app.view._height - 1
        
        #Return the coordinates of the line to be drawn 
        coordinates.append((i, drawStart, i, drawEnd, app.view.map[mapX][mapY]))
    print(f"CAST CALLED @: {app.view.posX}, {app.view.posY}")
    return coordinates