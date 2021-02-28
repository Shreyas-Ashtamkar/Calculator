#TEXT_SIZE = 48, fixed
class RectangleComponent:
    def __init__(self, x=0, y=0, l=None, b=None, col=None, txt=""):
        self.x, self.y = x, y
        
        self.l = l or ((len(txt)*29)+12)
        self.b = b or 70
            
        self.bgColor = col if col else color(255)
        self.textColor = color(0)
        
        self.TEXT_SIZE    = 48
        self.TEXT_PADD    = 6
        self.TEXT_FONT    = loadFont("Monospaced.plain-48.vlw")
        self.setText      = str(txt)
        
        self.visible      = True
        self.dynamicSize  = False
        
    
    def showText(self):
        #set text format
        textFont(self.TEXT_FONT)
        textSize(self.TEXT_SIZE)
        textAlign(LEFT, TOP)
        fill(self.textColor)
        
        #text placement
        x = (((2*self.x)+self.l)/2) - (((len(str(self.setText))*29)-1)/2)
        y = (((2*self.y)+self.b)/2) - 18
        
        #draw text
        text(self.setText, x, y)


    def draw(self, shadow=True):
        #if invisible then just return
        if not self.visible: return
        
        #dynamic set size
        if self.dynamicSize:
            self.l = ((len(self.setText)*29)+12)
            self.b = 70
        
        #draw shadow
        if shadow:
            fill(125)
            rect(self.x+5, self.y+5, self.l, self.b)
        
        #draw main button
        fill(self.bgColor)
        rect(self.x, self.y, self.l, self.b)
        
        #draw text
        self.showText()
        
        
        
        
        
