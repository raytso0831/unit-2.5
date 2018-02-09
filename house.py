#Ray Tso
#2/8/18
#house.py

from ggame import *

turoquise=Color(0x00FFFF,1) #this is the color turoquise
purple=Color(0xCC00CC,1)
orange=Color(0xFF8000,1)

blackOutline=LineStyle(1, black)

turoquiseRectangle=RectangleAsset(150,100,blackOutline,turoquise) #width, height, outline, fill
orangeTriangle=PolygonAsset([(0,300),(120,180),(200,300)], blackOutline,orange)

Sprite(turoquiseRectangle,(225,400))
Sprite(orangeTriangle,(200,300))

App().run()

