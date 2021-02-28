from Components import RectangleComponent
from Buttons import Button

class Keypad(RectangleComponent):
    def __init__(self, keyValues, x=0, y=0, l=0, b=0, cols=3, bgColor=color(0,0,0,0), keyColor=color(240)):
        RectangleComponent.__init__(self, x, y, l, b, col=bgColor)
        
        self.keyColor    = keyColor
        self.keyColumns  = cols
        
        self.keyWidth    = (l/cols)
        rows = (len(keyValues)//cols) + (1 if  len(keyValues)%cols!=0 else 0)
        self.keyHeight   = (b/rows)
        
        self.keyGrid     = []
        
        for i, k in enumerate(keyValues):
            if (i%cols == 0):
                self.keyGrid.append([])
            
            lx = self.x+(self.keyWidth *len(self.keyGrid[-1]))
            ly = self.y+(self.keyHeight*(len(self.keyGrid)-1))
            
            self.keyGrid[-1].append(
                Button(
                    x = lx + 10,
                    y = ly + 10,
                    l = self.keyWidth  - 20,
                    b = self.keyHeight - 20,
                    onClick = lambda:None,
                    txt = str(k),
                    col = color(255, 20, 20) if k == "C" else self.keyColor
                )
            )

    def interact(self):
        for r in self.keyGrid:
            for k in r:
                if k.isClicked():
                    return k.setText
        else:
            return None
    
    def draw(self):
        for r in self.keyGrid:
            for c in r:
                c.draw()
                if c.setText == "C":
                    c.textColor = color(255)
        #create buttons grid wise and store. onClick should return their text value
        
    
        
