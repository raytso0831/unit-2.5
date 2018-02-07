#Ray Tso
#2/7/18
#graphicsDemo.py- Intro to ggame

from ggame import *

red=Color(0xFF0000,1) #this is the color red
green=Color(0x00FF00,1)
blue=Color(0x0000FF,1)
black=Color(0x000000,1)

blackOutline=LineStyle(1, black)

redRectangle=RectangleAsset(200,100,blackOutline,red) #width, height, outline, fill
blueCircle=CircleAsset(50,blackOutline,blue) #Radius, outline, fill
greenEllipse=EllipseAsset(100,50,blackOutline,green)#width, height, outline, fill
blackline=LineAsset(50,160,blackOutline) #x_enpoint, Y_enpoint, lineStyle
redTriangle=PolygonAsset([(0,0),(120,180),(60,300)], blackOutline,red)


Sprite(redRectangle)
Sprite(blueCircle,(50,50))
Sprite(greenEllipse,(200,400))
Sprite(blackline)
Sprite(redTriangle)


App().run()


