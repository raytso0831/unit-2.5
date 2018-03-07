#Ray Tso
#2/8/18
#house.py

from ggame import *

blue = Color(0x0000FF,1)
black = Color(0x000000,1)
blackoutline = LineStyle(1,black)
bluesquare = RectangleAsset(200,200,blackoutline,blue)
bluetriangle = PolygonAsset([(25,150),(175,50),(325,150)],blackoutline,blue)
blackdoor = RectangleAsset(50,75,blackoutline,black)

Sprite(bluesquare, (75,150))
Sprite(bluetriangle,(30,50))
Sprite(blackdoor, (150,275))
App().run()