class Point(x,y,color):
    def __init__(self):
        self.x = x
        self.y = y
        self.color = color
    
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
        
class Angle(value):
    def __init__(self):
        self.value = (value) % 360
        
    def __add__(self, other):
        return Angle(self.value + other.value)
    
    def __sub__(self, other):
        return Angle(self.value - other.value)
        
class Color(R,G,B):
    def __init__():
        self.r = R
        self.g = G
        self.b = B
        
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