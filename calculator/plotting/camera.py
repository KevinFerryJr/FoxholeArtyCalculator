class Camera:
    def __init__(self):
        self.offsetX = 0
        self.offsetY = 0
        self.targetX = 0
        self.targetY = 0
        self.moveSpeed = 0.01
        
        self.zoom_factor = 1.0
        self.min_zoom = 0.1  # Minimum zoom factor
        self.max_zoom = 10.0  # Maximum zoom factor

    def zoom_in(self, grid):
        # Check if over min zoom
        if self.zoom_factor < self.max_zoom:
            self.zoom_factor *= 1.1  # Increase zoom by 10%

    def zoom_out(self, grid):
        # Check if under max zoom
        if self.zoom_factor > self.min_zoom:
            self.zoom_factor /= 1.1  # Decrease zoom by 10%

    def move(self, dx, dy, grid):
        self.targetX += dx
        self.targetY += dy

    def update(self, grid):
        # Update grid properties based on camera settings
        self.updatePos()    
        self.updateZoom(grid)
        
    def updatePos(self):
        self.offsetX = self.lerp(self.offsetX, self.targetX, self.moveSpeed)
        self.offsetY = self.lerp(self.offsetY, self.targetY, self.moveSpeed)
    
    def updateZoom(self, grid):
        grid.gridSize = int(18 * self.zoom_factor)  # Adjust grid size based on zoom factor
        
    def lerp(self, start, end, alpha):
        # Linear interpolation function
        return start + alpha * (end - start)