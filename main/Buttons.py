#TEXT_SIZE = 48, fixed
from Components import RectangleComponent

class Button(RectangleComponent):
    def __init__(self, x=0, y=0, l=None, b=None, col=color(240), txt="Button", onClick=lambda:None):
        RectangleComponent.__init__(self,x,y,l,b,col,txt)
        self.onClick=onClick
    
    
    def isClicked(self):
        conditions = (
            mouseX >= self.x,
            mouseY >= self.y,
            mouseX <= self.x+self.l,
            mouseY <= self.y+self.b
        )
        
        return all(conditions)
    
    
    def draw(self):
        if mousePressed and self.isClicked():
            self.x += 5
            self.y += 5
            
            RectangleComponent.draw(self, shadow=False)
            
            self.x -= 5
            self.y -= 5
        else:
            RectangleComponent.draw(self)
