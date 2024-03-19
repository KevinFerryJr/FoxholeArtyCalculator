import math

class Solution():
    def __init__(self):
        self.point_a = (0,0)
        self.point_b = (0,0)
        self.point_c = (0,0)
    
    def set(self,gunDist,gunAngle,targDist,targAngle):
        cosA = math.cos(math.radians(gunAngle))
        sinA = math.sin(math.radians(gunAngle))
        
        cosB = math.cos(math.radians(targAngle))
        sinB = math.sin(math.radians(targAngle))
        
        # Example point plotting
        self.point_a = (cosA*gunDist, sinA*gunDist)
        self.point_b = (cosB*targDist, sinB*targDist)
        self.point_c = (0, 0)
        
    def get(self):
        return (self.point_a, self.point_b, self.point_c)
    
    def drawSolution(self, solution, grid):
        grid.graph_line(solution[0], solution[1])  
        grid.graph_line(solution[1], solution[2])  
        grid.graph_line(solution[2], solution[0])  
        grid.plot_point(solution[0], (0, 0, 255))  # Blue point
        grid.plot_point(solution[1], (255, 0, 0))  # Red point
        grid.plot_point(solution[2], (0, 255, 0))  # Green point