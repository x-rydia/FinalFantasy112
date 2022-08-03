"""
The environment is rendered as a series of vertical lines,
so using images is very difficult to do.

Instead, in order to make the environment look more interesting,
I will use a list of colors in order. This can be used to 
create a texture that looks like say, wood planks or bricks
or some kind of stone.

Adding some kind of horizontal lines will be fairly difficult 
to do in a manner that does not have issues with the raycasting. 
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