from Components import RectangleComponent
from Screen import LCDScreen
from Keypad import Keypad

class Calculator(RectangleComponent):
    def __init__(self,  x=10, y=10, l=520, b=120, col=color(200)):
        RectangleComponent.__init__(self,x,y,l,b,col)
        self.buffer = "0"
        
        self.outputScreen   = LCDScreen(x=self.x+10, y=self.y+10, l=self.l-20, b=100)
        
        keyArrangement = [
             1 ,  2 ,  3 , "C",
             4 ,  5 ,  6 , "+",
             7 ,  8 ,  9 , "-", 
            "/",  0 , "*", "="
        ]
        
        self.mainKeypad     = Keypad(keyValues=keyArrangement, x=self.x-5, y=self.y+110, l=self.l, b=self.b-110, cols=4)
    
    def interact(self):
        i = self.mainKeypad.interact()
        
        if i == None:return
        
        buffer = self.buffer
        
        if "ERROR" in buffer:
            buffer = "0"
        
        elif i in "0123456789":
            if buffer  == "0" or buffer == "ERROR":
                buffer =  ""
            buffer+=i
        elif i == 'C':
            buffer = "0"
        elif i in "+*/-=":
            if buffer[-1] in "+-*/":
                buffer=buffer[:-1]
            if "+" in buffer:
                buffer = buffer.split("+")
                buffer = str(float(buffer[0])+float(buffer[1]))
            elif "-" in buffer:
                buffer = buffer.split("-")
                buffer = str(float(buffer[0])-float(buffer[1]))
            elif "*" in buffer:
                buffer = buffer.split("*")
                buffer = str(float(buffer[0])*float(buffer[1]))
            elif "/" in buffer:
                buffer = buffer.split("/")
                if float(buffer[1])!=0:
                    buffer = str(float(buffer[0])/float(buffer[1]))
                else:
                    buffer = "ERROR"
            if i!="=":
                buffer+=i
            
        self.buffer = str(buffer)
        
    
    def draw(self):
        RectangleComponent.draw(self, shadow=False)
        self.outputScreen.setText = self.buffer
        self.outputScreen.draw()
        self.mainKeypad.draw()
