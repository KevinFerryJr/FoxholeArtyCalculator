class Camera:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width, self.screen_height = screen.get_size()
        self.zoom_factor = 1.0
        self.offset_x = 0
        self.offset_y = 0

    def zoom_in(self, grid):
        # Check if over min zoom
        if grid.grid_size < 20:
            #self.zoom_factor *= 1.1
            grid.grid_size += 1

    def zoom_out(self, grid):
        # Check if under max zoom
        if grid.grid_size > 3:
            #self.zoom_factor /= 1.1
            grid.grid_size -= 1

    def move(self, dx, dy):
        self.offset_x += dx
        self.offset_y += dy