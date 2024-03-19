import math

class Solution():
    def __init__(self):
        self.pointA = (0,0)
        self.pointB = (0,0)
        self.pointC = (0,0)
    
    def set(self,gunDist,gunAngle,targDist,targAngle):
        cosA = math.cos(math.radians(gunAngle))
        sinA = math.sin(math.radians(gunAngle))
        
        cosB = math.cos(math.radians(targAngle))
        sinB = math.sin(math.radians(targAngle))
        
        # Example point plotting
        self.pointA = (cosA*gunDist, sinA*gunDist)
        self.pointB = (cosB*targDist, sinB*targDist)
        self.pointC = (0, 0)
        
    def get(self):
        return (self.pointA, self.pointB, self.pointC)
    
    def drawSolution(self, solution, grid):
        grid.graph_line(solution[0], solution[1])  
        grid.graph_line(solution[1], solution[2])  
        grid.graph_line(solution[2], solution[0])  
        grid.plot_point(solution[0], (0, 0, 255))  # Blue point
        grid.plot_point(solution[1], (255, 0, 0))  # Red point
        grid.plot_point(solution[2], (0, 255, 0))  # Green point