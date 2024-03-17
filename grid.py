import pygame

class Grid:
    def __init__(self, screen, grid_size):
        self.grid_size = grid_size
        self.grid_color = (200, 200, 200)
        self.x_axis_color = (255, 0, 0)
        self.y_axis_color = (0, 255, 0)

        self.screen = screen
        self.screen_width, self.screen_height = screen.get_size()
        self.line_width = 2
        self.num_lines_x = self.screen_width // self.grid_size
        self.num_lines_y = self.screen_height // self.grid_size

    def to_world_space(self, x, y):
        x -= self.screen_width / 2
        y -= self.screen_height / 2
        return x, y

    def to_screen_space(self, x, y):
        y *= -1
        x += self.screen_width / 2
        y += self.screen_height / 2
        return x, y

    def draw_grid(self, line_width=1):
        screen_center_x = self.screen_width // 2
        screen_center_y = self.screen_height // 2

        # Draw horizontal grid lines
        for y in range(-self.num_lines_y // 2, self.num_lines_y // 2 + 1):
            left_point = (0, screen_center_y + y * self.grid_size)
            right_point = (self.screen_width, screen_center_y + y * self.grid_size)
            pygame.draw.line(self.screen, self.grid_color, left_point, right_point, line_width)

        # Draw vertical grid lines
        for x in range(-self.num_lines_x // 2, self.num_lines_x // 2 + 1):
            top_point = (screen_center_x + x * self.grid_size, self.screen_height)
            bottom_point = (screen_center_x + x * self.grid_size, 0)
            pygame.draw.line(self.screen, self.grid_color, top_point, bottom_point, line_width)

        # Draw X-axis
        pygame.draw.line(self.screen, self.x_axis_color, (0, screen_center_y), (self.screen_width, screen_center_y), line_width * 2)

        # Draw Y-axis
        pygame.draw.line(self.screen, self.y_axis_color, (screen_center_x, self.screen_height), (screen_center_x, 0), line_width * 2)

    def plot_point(self, coords, color, size=5):
        grid_x = coords[0] * self.grid_size
        grid_y = coords[1] * self.grid_size
        pygame.draw.circle(self.screen, color, self.to_screen_space(grid_x, grid_y), size)

    def graph_line(self, point_a, point_b, color=(200,50,30), stroke=2):
        a_x, a_y = self.to_screen_space(point_a[0]*self.grid_size, point_a[1]*self.grid_size)
        b_x, b_y = self.to_screen_space(point_b[0]*self.grid_size, point_b[1]*self.grid_size)
        point_a = (a_x, a_y)
        point_b = (b_x, b_y)
        pygame.draw.line(self.screen, color, point_a, point_b, stroke)