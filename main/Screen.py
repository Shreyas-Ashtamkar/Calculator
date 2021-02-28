from Components import RectangleComponent

class LCDScreen(RectangleComponent):
    def __init__(self, x=0, y=0, l=0, b=150, col=color(0,125,0), txt=0):
        RectangleComponent.__init__(self,x,y,l,b,col)
    
    def draw(self):
        RectangleComponent.draw(self, shadow=False)
