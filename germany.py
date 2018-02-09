#Ray Tso
#2/9/18
#house.py

from ggame import *

black=Color(0x000000,1) #this is the color turoquise
red=Color(0xFF0000,1)
yellow=Color(0xFFFF00,1)

blackOutline=LineStyle(1, black)

blackRectangle=RectangleAsset(550,100,blackOutline,black) #width, height, outline, fill
redRectangle=RectangleAsset(550,100,blackOutline,red) #width, height, outline, fill
yellowRectangle=RectangleAsset(550,100,blackOutline,yellow) #width, height, outline, fill


Sprite(blackRectangle,(225,200))
Sprite(redRectangle,(225,300))
Sprite(yellowRectangle,(225,400))


App().run()
