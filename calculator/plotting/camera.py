class Camera:
    def __init__(self):
        self.posX = 0
        self.posY = 0
        self.targetX = 0
        self.targetY = 0
        self.followSpeed = 0.1
        self.moveSpeed = 5
        
        self.zoomFactor = 0.3
        self.zoomTarget = self.zoomFactor
        self.minZoom = 0.1
        self.maxZoom = 10.0
        self.zoomSpeed = 0.1

    def zoom_in(self):
        if self.zoomFactor < self.maxZoom:
            self.zoomTarget *= 1.1

    def zoom_out(self):
        if self.zoomFactor > self.minZoom:
            self.zoomTarget /= 1.1

    def move(self, dx, dy):
        self.targetX += dx * self.moveSpeed
        self.targetY += dy * self.moveSpeed

    def update(self, grid):
        self.updatePos()    
        self.updateZoom(grid)
        
    def updatePos(self):
        self.posX = self.lerp(self.posX, self.targetX, self.followSpeed)
        self.posY = self.lerp(self.posY, self.targetY, self.followSpeed)
    
    def updateZoom(self, grid):
        self.zoomFactor = self.lerp(self.zoomFactor, self.zoomTarget, self.zoomSpeed)
        grid.scale = self.zoomFactor * grid.tileSize
        
    def lerp(self, start, end, alpha):
        return start + alpha * (end - start)