"""
Environment class will contain the geography of the 
level, the floor texture, the ceiling texture, and 
any sprites or entities.

Built in texture packs will be made as globals here
"""

from graphics.textures import *


class TexturePack:
    def __init__(self, 
            floor: list,
            ceiling: list,
            wallTextures: 'dict[list]',
            horizontalWallTextures: 'dict[list]',
            hasDayNight: bool=False,
            dayCeiling: list=None,
            nightCeiling: list=None) -> None:
        
        # Floor and ceiling are two rectangles drawn as the first
        # Layer of the screen with floor occupying the bottom half
        # of the screen and ceiling occupying the top half. Walls
        # are rendered on top of the floor and ceiling.

        # The floor and ceiling textures will be represented as 
        # a list of colors (string names or hexadecimal values,
        # doesnt matter) that will be repeatedly drawn in order 
        # to create the floor and ceiling.
        self.floor = floor
        self.ceiling = ceiling
        
        # Wall textures is a dict of integer keys and list values. 
        # The list values will be a list of colors that will be 
        # drawn repeatedly in order to texture the walls. 
        # The integer keys will be the values of the 2d list for the map, 
        # Allowing the map to access these textures
        self.wallTextures = wallTextures
        self.horizontalWallTextures = horizontalWallTextures

        # HasDayNight is a boolean that will be used to determine
        # if the ceiling has a day and night texture.
        # This would be useful for making a more realistic  
        # outdoor map OR a map that buffs enemies or increass the 
        # spawn rate at night
        self.hasDayNight = hasDayNight
        if self.hasDayNight:
            self.dayCeiling = dayCeiling
            self.nightCeiling = nightCeiling

    def toggleDayNight(self): 
        """
        ONLY toggle the ceiling texture if the texture pack has
        separate day and night textures.
        """
        if self.hasDayNight:
            if self.ceiling == self.dayCeiling:
                self.ceiling = self.nightCeiling
            else:
                self.ceiling = self.dayCeiling


def replace(list, int1, int2):
    """
    Given a 2d list, replace all instances of int1 with int2

    This is used to replace all instances of a texture with another
    texture in map generation.
    """
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j] == int1:
                list[i][j] = int2
    return list



TEST1 = TexturePack(
    floor=GRASS,
    ceiling=SKY,
    wallTextures={
        0: GRASS, # 0 is the value of the map for the floor
        1: SKY,
        2: WOOD_PLANK,
        3: STONE_BRICK,
        4: STONE_BRICK_GRADIENT,
        5: GRASS,
        7: WOOD_PLANK_2
    },

    #Horizontal lines to overlay the wall textures with
    #This 
    horizontalWallTextures={
        0: ["Dark Green", "Dark Green"], #Complement for grass
        1: ["White", "White"],
        2: ["Black", "Black", "Black", "Black"],
        3: ["Black", "Black", "Black", "Black"],
        4: ["Black", "Black", "Black", "Black"],
        5: ["Dark Green", "Dark Green", "Dark Green", "Dark Green"],
        7: ["Black", "Black", "Black", "Black"]
    },
    hasDayNight=False
)


