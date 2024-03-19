import pygame

class Grid:
    def __init__(self, screen, camera, gridSize = 18):
        self.gridSize = gridSize
        self.gridColor = (200, 200, 200)
        self.xAxisColor = (255, 0, 0)
        self.yAxisColor = (0, 255, 0)
        self.camera = camera

        self.screen = screen
        self.screenWidth, self.screen_height = screen.get_size()
        self.screenCenter = (self.screenWidth // 2, self.screen_height // 2)
        self.line_width = 2
        self.num_lines_x = (self.screenWidth // self.gridSize)*20
        self.num_lines_y = (self.screen_height // self.gridSize)*20

    def to_world_space(self, x, y):
        x -= self.screenWidth / 2
        y -= self.screen_height / 2
        return x, y

    def to_screen_space(self, x, y):
        y *= -1
        x += self.screenWidth / 2
        y += self.screen_height / 2
        return x, y

    def drawHorizontalLines():
        return
    def drawVerticalLines():
        return
    
    def draw_grid(self, line_width=1):
        # Draw horizontal grid lines
        color = self.gridColor
        for y in range(-self.num_lines_y // 2, self.num_lines_y // 2 + 1):
            
            # Check if the current line is at a multiple of 5 units
            if y % 5 == 0:
                color = (150,150,150)
            else:
                color = self.gridColor

            left_point = (0, self.screenCenter[1] + y * self.gridSize + self.camera.offsetY)
            right_point = (self.screenWidth, self.screenCenter[1] + y * self.gridSize + self.camera.offsetY)
            pygame.draw.line(self.screen, color, left_point, right_point, line_width * line_width)
        color = self.gridColor
        # Draw vertical grid lines
        for x in range(-self.num_lines_x // 2, self.num_lines_x // 2 + 1):
            # Check if the current line is at a multiple of 5 units
            if x % 5 == 0:
                color = (150,150,150)
            else:
                color = self.gridColor

            bottom_point = (self.screenCenter[0] + x * self.gridSize + self.camera.offsetX, self.screen_height)
            top_point = (self.screenCenter[0] + x * self.gridSize + self.camera.offsetX, 0)
            pygame.draw.line(self.screen, color, top_point, bottom_point, line_width * line_width)

            self.draw_axis(line_width)

    def plot_point(self, coords, color, size=4):
        grid_x = coords[0] * self.gridSize + self.camera.offsetX
        grid_y = coords[1] * self.gridSize - self.camera.offsetY
        pygame.draw.circle(self.screen, color, self.to_screen_space(grid_x, grid_y), size)

    def graph_line(self, point_a, point_b, color=(200,50,30), stroke=2):
        a_x, a_y = self.to_screen_space(point_a[0]*self.gridSize + self.camera.offsetX, point_a[1]*self.gridSize - self.camera.offsetY)
        b_x, b_y = self.to_screen_space(point_b[0]*self.gridSize + self.camera.offsetX, point_b[1]*self.gridSize - self.camera.offsetY)
        point_a = (a_x, a_y)
        point_b = (b_x, b_y)
        pygame.draw.line(self.screen, color, point_a, point_b, stroke)

    def draw_axis(self, line_width):
        # Draw X-axis
        x_axis_left = (0, self.screenCenter[1] + self.camera.offsetY)
        x_axis_right = (self.screenWidth, self.screenCenter[1] + self.camera.offsetY)
        pygame.draw.line(self.screen, self.xAxisColor, x_axis_left, x_axis_right, line_width * 2)

        # Draw Y-axis
        y_axis_top = (self.screenCenter[0] + self.camera.offsetX, self.screen_height)
        y_axis_bottom = (self.screenCenter[0] + self.camera.offsetX, 0)
        pygame.draw.line(self.screen, self.yAxisColor, y_axis_top, y_axis_bottom, line_width * 2)
