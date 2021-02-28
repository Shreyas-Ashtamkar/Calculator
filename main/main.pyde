from Calculator import Calculator

mainCalculator = None

def setup():
    global mainCalculator
    size(500,600)
    
    mainCalculator = Calculator(x=10, y=10, l=width-20, b=height-20)

def draw():
    
    background(255)
    mainCalculator.draw()
    
def mouseClicked():
    mainCalculator.interact()
