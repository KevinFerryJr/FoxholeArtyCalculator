import pygame

class Grid:
    def __init__(self, screen, camera, grid_size):
        self.grid_size = grid_size
        self.grid_color = (200, 200, 200)
        self.x_axis_color = (255, 0, 0)
        self.y_axis_color = (0, 255, 0)
        self.camera = camera

        self.screen = screen
        self.screen_width, self.screen_height = screen.get_size()
        self.screen_center = (self.screen_width // 2, self.screen_height // 2)
        self.line_width = 2
        self.num_lines_x = (self.screen_width // self.grid_size)*20
        self.num_lines_y = (self.screen_height // self.grid_size)*20

    def to_world_space(self, x, y):
        x -= self.screen_width / 2
        y -= self.screen_height / 2
        return x, y

    def to_screen_space(self, x, y):
        y *= -1
        x += self.screen_width / 2
        y += self.screen_height / 2
        return x, y

    def draw_grid(self, camera, line_width=1):
        # Draw horizontal grid lines
        color = self.grid_color
        for y in range(-self.num_lines_y // 2, self.num_lines_y // 2 + 1):
            
            # Check if the current line is at a multiple of 5 units
            if y % 5 == 0:
                color = (150,150,150)
            else:
                color = self.grid_color

            left_point = (0, self.screen_center[1] + y * self.grid_size + self.camera.offset_y)
            right_point = (self.screen_width, self.screen_center[1] + y * self.grid_size + self.camera.offset_y)
            pygame.draw.line(self.screen, color, left_point, right_point, line_width * line_width)

        # Draw vertical grid lines
        for x in range(-self.num_lines_x // 2, self.num_lines_x // 2 + 1):
            # Check if the current line is at a multiple of 5 units
            if x % 5 == 0:
                color = (150,150,150)
            else:
                color = self.grid_color

            bottom_point = (self.screen_center[0] + x * self.grid_size + self.camera.offset_x, self.screen_height)
            top_point = (self.screen_center[0] + x * self.grid_size + self.camera.offset_x, 0)
            pygame.draw.line(self.screen, color, top_point, bottom_point, line_width * line_width)

            self.draw_axis(line_width)

    def plot_point(self, coords, color, size=2):
        grid_x = coords[0] * self.grid_size + self.camera.offset_x
        grid_y = coords[1] * self.grid_size - self.camera.offset_y
        pygame.draw.circle(self.screen, color, self.to_screen_space(grid_x, grid_y), size)

    def graph_line(self, point_a, point_b, color=(200,50,30), stroke=2):
        a_x, a_y = self.to_screen_space(point_a[0]*self.grid_size + self.camera.offset_x, point_a[1]*self.grid_size - self.camera.offset_y)
        b_x, b_y = self.to_screen_space(point_b[0]*self.grid_size + self.camera.offset_x, point_b[1]*self.grid_size - self.camera.offset_y)
        point_a = (a_x, a_y)
        point_b = (b_x, b_y)
        pygame.draw.line(self.screen, color, point_a, point_b, stroke)

    def draw_axis(self, line_width):
        # Draw X-axis
        x_axis_left = (0, self.screen_center[1] + self.camera.offset_y)
        x_axis_right = (self.screen_width, self.screen_center[1] + self.camera.offset_y)
        pygame.draw.line(self.screen, self.x_axis_color, x_axis_left, x_axis_right, line_width * 2)

        # Draw Y-axis
        y_axis_top = (self.screen_center[0] + self.camera.offset_x, self.screen_height)
        y_axis_bottom = (self.screen_center[0] + self.camera.offset_x, 0)
        pygame.draw.line(self.screen, self.y_axis_color, y_axis_top, y_axis_bottom, line_width * 2)
