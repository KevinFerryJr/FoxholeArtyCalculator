import pygame

class Grid:
    def __init__(self, screen, camera):
        self.gridSize = 18
        self.gridColor = (200, 200, 200)
        self.xAxisColor = (255, 0, 0)
        self.yAxisColor = (0, 255, 0)
        self.camera = camera

        self.screen = screen
        self.screenWidth, self.screenHeight = screen.get_size()
        self.screenCenter = (self.screenWidth // 2, self.screenHeight // 2)
        self.lineWidth = 2
        self.numLinesX = (self.screenWidth // self.gridSize)*100
        self.numLinesY = (self.screenHeight // self.gridSize)*100

    def to_world_space(self, x, y):
        x -= self.screenWidth / 2
        y -= self.screenHeight / 2
        return x, y

    def to_screen_space(self, x, y):
        y *= -1
        x += self.screenWidth / 2
        y += self.screenHeight / 2
        return x, y

    def drawHorizontalLines(self, lineWidth=1):
        color = self.gridColor
        for y in range(-self.numLinesY // 2, self.numLinesY // 2 + 1):
            
            if y % 10 == 0:
                color = (150,150,150)    
            elif self.gridSize < 10:
                continue
            else:
                color = self.gridColor

            left_point = (0, self.screenCenter[1] + y * self.gridSize + self.camera.offsetY)
            right_point = (self.screenWidth, self.screenCenter[1] + y * self.gridSize + self.camera.offsetY)
            pygame.draw.line(self.screen, color, left_point, right_point, lineWidth * lineWidth)
        color = self.gridColor
        
    def drawVerticalLines(self, lineWidth=1):
        color = self.gridColor
        
        for x in range(-self.numLinesX // 2, self.numLinesX // 2 + 1):
            if x % 10 == 0:
                color = (150,150,150)
            elif self.gridSize < 10:
                continue
            else:
                color = self.gridColor

            bottomPoint = (self.screenCenter[0] + x * self.gridSize + self.camera.offsetX, self.screenHeight)
            topPoint = (self.screenCenter[0] + x * self.gridSize + self.camera.offsetX, 0)
            pygame.draw.line(self.screen, color, topPoint, bottomPoint, lineWidth * lineWidth)
    
    def drawGrid(self, lineWidth=1):
        self.drawVerticalLines(lineWidth)
        self.drawHorizontalLines(lineWidth)
        self.draw_axis(lineWidth)

    def plot_point(self, coords, color, size=4):
        gridX = coords[0] * self.gridSize + self.camera.offsetX
        gridY = coords[1] * self.gridSize - self.camera.offsetY
        pygame.draw.circle(self.screen, color, self.to_screen_space(gridX, gridY), size)

    def graph_line(self, pointA, pointB, color=(200,50,30), stroke=2):
        aX, aY = self.to_screen_space(pointA[0]*self.gridSize + self.camera.offsetX, pointA[1]*self.gridSize - self.camera.offsetY)
        bX, bY = self.to_screen_space(pointB[0]*self.gridSize + self.camera.offsetX, pointB[1]*self.gridSize - self.camera.offsetY)
        pointA = (aX, aY)
        pointB = (bX, bY)
        pygame.draw.line(self.screen, color, pointA, pointB, stroke)

    def draw_axis(self, lineWidth):
        # Draw X-axis
        xAxisLeft = (0, self.screenCenter[1] + self.camera.offsetY)
        xAxisRight = (self.screenWidth, self.screenCenter[1] + self.camera.offsetY)
        pygame.draw.line(self.screen, self.xAxisColor, xAxisLeft, xAxisRight, lineWidth * 2)

        # Draw Y-axis
        yAxisTop = (self.screenCenter[0] + self.camera.offsetX, self.screenHeight)
        yAxisBottom = (self.screenCenter[0] + self.camera.offsetX, 0)
        pygame.draw.line(self.screen, self.yAxisColor, yAxisTop, yAxisBottom, lineWidth * 2)
