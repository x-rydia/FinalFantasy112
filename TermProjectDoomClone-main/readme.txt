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



    


