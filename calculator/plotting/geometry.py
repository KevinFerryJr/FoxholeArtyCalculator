class Point(x,y,color):
    def __init__(self):
        self.x = x
        self.y = y
        self.color = color
    
    def getPos(self):
        return self.x, self.y
    
    def setPos(self,x,y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        dX = self.x + other.x, self.y
        dY = other.y, self.color + other.color
        return Point(dX + dY)
    
    def __sub__(self, other):
        dX = self.x - other.x, self.y
        dY = other.y, self.color + other.color
        return Point(dX - dY)
    
class Line(start, end):
    def __init__(self):
        self.start = start
        self.end = end
    
    def get(self):
        return self.start, self.end
         
class Angle(value):
    def __init__(self):
        self.value = (value) % 360
        
    def __add__(self, other):
        return Angle(self.value + other.value)
    
    def __sub__(self, other):
        return Angle(self.value - other.value)
    
    def __mul__(self, other):
        return Angle(self.value * other.value)
    
    def __truediv__(self, other):
        return Angle(self.value / other.value)
        
class Color(R,G,B):
    def __init__():
        self.r = R
        self.g = G
        self.b = B
        
    def get(self):
        return self.r, self.g, self.b
    
    def set(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        
    def __add__(self, other):
        dR = (self.r + other.r) % 255
        dG = (self.g + other.g) % 255
        dB = (self.b + other.b) % 255
        return Color(dR,dG,dB)
    
    def __sub__(self, other):
        dR = (self.r - other.r) % 255
        dG = (self.g - other.g) % 255
        dB = (self.b - other.b) % 255
        return Color(dR,dG,dB)