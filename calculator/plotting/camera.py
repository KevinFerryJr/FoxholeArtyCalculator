class Camera:
    def __init__(self):
        self.offsetX = 0
        self.offsetY = 0
        self.targetX = 0
        self.targetY = 0
        self.followSpeed = 0.1
        self.moveSpeed = 5
        
        self.zoomFactor = 0.3
        self.minZoom = 0.1  # Minimum zoom factor
        self.maxZoom = 10.0  # Maximum zoom factor

    def zoom_in(self, grid):
        # Check if over min zoom
        if self.zoomFactor < self.maxZoom:
            self.zoomFactor *= 1.1  # Increase zoom by 10%

    def zoom_out(self, grid):
        # Check if under max zoom
        if self.zoomFactor > self.minZoom:
            self.zoomFactor /= 1.1  # Decrease zoom by 10%

    def move(self, dx, dy, grid):
        self.targetX += dx * self.moveSpeed
        self.targetY += dy * self.moveSpeed

    def update(self, grid):
        # Update grid properties based on camera settings
        self.updatePos()    
        self.updateZoom(grid)
        
    def updatePos(self):
        self.offsetX = self.lerp(self.offsetX, self.targetX, self.followSpeed)
        self.offsetY = self.lerp(self.offsetY, self.targetY, self.followSpeed)
    
    def updateZoom(self, grid):
        grid.gridSize = int(18 * self.zoomFactor)  # Adjust grid size based on zoom factor
        
    def lerp(self, start, end, alpha):
        # Linear interpolation function
        return start + alpha * (end - start)