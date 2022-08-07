"""
The environment is rendered as a series of vertical lines,
so using images is very difficult to do.

Instead, in order to make the environment look more interesting,
I will use a list of colors in order. This can be used to 
create a texture that looks like say, wood planks or bricks
or some kind of stone.

Adding some kind of horizontal lines will be fairly difficult 
to do in a manner that does not have issues with the raycasting. 
Drawing horizontal lines over the vertical textures and vice versa 
is defintely possible, but I do not see a way to do it without either
doubling the raycasting runtime or not raycasting and having very awkaward 
and clunky textures.
"""

WOOD_PLANK = [
    "black",
    "tan4",
    "sienna4",
    "sienna3",
    "chocolate3",
    "DarkOrange4",
    "tan4",
    "sienna4",
    "sienna3",
    "chocolate3",
    "DarkOrange4",
    "tan4",
    "sienna4",
    "sienna3",
    "chocolate3",
    "DarkOrange4",
    "tan4",
    "sienna4",
    "sienna3",
    "chocolate3",
    "DarkOrange4",
    "tan4",
    "sienna4",
    "sienna3",
    "chocolate3",
    "DarkOrange4",
    "tan4",
    "sienna4",
    "sienna3",
    "chocolate3",
    "DarkOrange4",
    "tan4",
    "sienna4",
    "sienna3",
    "chocolate3",
    "DarkOrange4",
    "tan4",
    "sienna4",
    "sienna3",
    "chocolate3",
    "DarkOrange4",
    "black"
]

STONE_BRICK = [
    "black",
    "gray",
    "gray",
    "gray",
    "gray",
    "gray",
    "gray",
    "gray",
    "gray",
    "gray",
    "gray",
    "gray",
    "gray",
    "gray",
    "gray",
    "gray",
    "black"
]

STONE_BRICK_GRADIENT = [
    "black",
    "#D3D3D3",
    "#D3D3D3",
    "#BDBDBD",
    "#BDBDBD",
    "#9E9E9E",
    "#9E9E9E",
    "#7D7D7D",
    "#7D7D7D",
    "#696969", #Nice.
    "#696969",
    "#D3D3D3",
    "#D3D3D3",
    "#BDBDBD",
    "#BDBDBD",
    "#9E9E9E",
    "#9E9E9E",
    "#7D7D7D",
    "#7D7D7D",
    "#696969", #Nice.
    "#696969",
    "black"
]

GRASS = [
    "#5FC314",
    "#5FC314",
    "#79D021",
    "#C1F376",
    "#55C233",
    "#37AE0F"
]

SKY = [
    "skyblue",
    "skyblue",
]

#Redder with more iterations
WOOD_PLANK_2 = [
    "tan4",
    "tan4"
]



RED_DIAMOND = [
    [None, None, None, "red", None, None, None],
    [None, None, "red", "red", "red", None, None],
    [None, "red", "red", "red", "red", "red", None],
    ["red", "red", "red", "red", "red", "red", "red"],
    [None, "red", "red", "red", "red", "red", None],
    [None, None, "red", "red", "red", None, None],
    [None, None, None, "red", None, None, None]
]

class Sprite:
    def __init__(self,
            texture: list,
            xPos: float,
            yPos: float,
            scaleFactor: float
        ) -> None:
        self.texture = texture
        self.xPos = xPos
        self.yPos = yPos

        self.screenStartY = 0
        
        #float in range(0, 1) is the percentage of the wall  
        #That the sprite is on.
        self.scaleFactor = scaleFactor

