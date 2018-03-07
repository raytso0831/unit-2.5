#Ray Tso
#2/8/18
#house.py

from ggame import *

red = Color(0xFF3333,1)
black = Color(0x000000,1)
blackoutline = LineStyle(1,black)
redsquare = RectangleAsset(200,200,blackoutline,red)
redtriangle = PolygonAsset([(25,150),(175,50),(325,150)],blackoutline,red)
blackdoor = RectangleAsset(50,75,blackoutline,black)

Sprite(redsquare, (75,150))
Sprite(redtriangle,(30,50))
Sprite(blackdoor, (150,275))
App().run()