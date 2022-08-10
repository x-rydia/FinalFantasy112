Project Name and Description: 

Final Fantasy 112 will be a raycasted role playing game inspired by the late
eighties and early nineties games Final Fantasy 1, 2, 3, and 4

Structural Plan:
    - In order to keep things as clean as possible, different sets of 
      cmu_112_graphics functions for different areas of the game will 
      be separated. For example, I have a combatKeyPressed(app, event) 
      and a viewKeyPressed(app, event) so that I can call them directly 
      in KeyPressed depending on the state of the application.
    
    - The player View class will data on the player with respect to 
      raycasting (position, direction of view, etc) and will also have
      methods for controlling the movement of the player and collision 
      checks. 

    - The majority of the raycasting math will be preformed in the
      cast(view) function, which takes the player View object as a argument
      and returns a list of lines to be drawn on the screen, represented as 
      tuples (x0, y0, x1, y1, colorCode)
    
    - The world map will be represented as a series of two dimensional lists 
      of integers corresponding to textures. The textures will be lists of 
      colors that will form a pattern, Example:
            - map[row][col] == 3, textures["3"] == ["red","green","red"], 
              texture lines will have each pixel alternating colors as red,
              then green, then red.
      In order to quickly make and modify the world map, I have made another 
      app!! :) This is an unusable skeleton in the folder "levelbuilder" 
      as of right now it is not integratable into the larger project.

      But its a surprise tool that will help us later... 
    
    - The combat system will have its own classes for the player and enemy,
      which will inherit from an entity class. These classes  will have methods
      that take a target entity as an argument for things like attacking 
      and blocking and whatnot. Enemies will have a texture image that is 
      rendered in the center of the combat display.
    
    - Random encounters will be handled in the same file as the View class 
      because it will be a function called on movement. 



ALGORITHMIC PLANS:
    - raycasting (https://lodev.org/cgtutor/raycasting.html):
        We will calculate the length of a line on the screen 
        proportional to the distance from a wall using the 
        players position (fractional indicies of the map list) 
        and their direction (x, y) of view. 

        get a step angle for each pixel in the screen, 
        for each pixel on the screen,
          make a new ray represented by a slope given the players
          direction and the step angle and the pixel

          extend the perpendicular components of the ray 
          until they come into contact with a wall on the map,
          giving a distance to a wall

          use the distance to calculate the height of the line
          on the screen
    
    - rotating the player view for raycasting
        use rotation matricies to transform the points for the 
        direction of the players view by a given angle 

    - Movement:
        check to ensure that the target cell in the map is not a wall
        if not, add to the x and y positin by an amount proportional to the 
        direction the player is facing
    
    - terrain generation:
        - Procedurally generate two main buildings for the game,
        one allied and one enemy Building generation is as follows:
            - Take an NxN list:
                - in list, place K "boxes" of varying ODD NUMBERED random square dimensions.
                  determine a random row, col pair in the NxN and place the center of the box 
                  at that index 
                - for each box, 
                    pick a random index on two sides of the box 
                    calculate the path from this index on the side to its nearest
                    neighbor index from another box

                    take that path, surround it with walls, and bam theres a tunnel 
                    connecting rooms
        Between these two building dungeon things, have a wide open plain meant to 
        look like the outdoors with Procedurally placed trees.

    - Save files
        Upon saving, get all attributes of the Player and View classes and save them
        to a txt file 

        Upon loading, parse the txt file and reinitialize the classes with that 
        data. 
         









    


