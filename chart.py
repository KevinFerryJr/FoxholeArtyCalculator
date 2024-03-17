import pygame
import sys

class Grid:
    def __init__(self, screen, grid_size, grid_color, axis_color, y_axis_color):
        self.screen = screen
        self.grid_size = grid_size
        self.grid_color = grid_color
        self.axis_color = axis_color
        self.y_axis_color = y_axis_color
        self.screen_width, self.screen_height = screen.get_size()
        self.num_lines_x = self.screen_width // self.grid_size
        self.num_lines_y = self.screen_height // self.grid_size

    def to_world_space(self,x,y):
        x-= screen_width/2
        y-= screen_height/2
        return x, y
        
    def to_screen_space(self,x,y):
        x+= screen_width/2
        y+= screen_height/2
        return x, y
        
    def draw_grid(self):
        # Draw horizontal grid lines
        for y in range(self.num_lines_y + 1):
            pygame.draw.line(self.screen, self.grid_color, (0, y * self.grid_size), (self.screen_width, y * self.grid_size))

        # Draw vertical grid lines
        for x in range(self.num_lines_x + 1):
            pygame.draw.line(self.screen, self.grid_color, (x * self.grid_size, 0), (x * self.grid_size, self.screen_height))

        # Draw X-axis
        pygame.draw.line(self.screen, self.axis_color, (0, self.screen_height // 2), (self.screen_width, self.screen_height // 2), 2)

        # Draw Y-axis
        pygame.draw.line(self.screen, self.y_axis_color, (self.screen_width // 2, 0), (self.screen_width // 2, self.screen_height), 2)

    def plot_point(self, x, y, color):
        screen_x = x * self.grid_size
        screen_y = y * self.grid_size
        #pygame.draw.circle(self.screen, color, (int((self.screen_width // 2) + (x * self.grid_size)), int(self.screen_height // 2 - y * self.grid_size)), 5)
        pygame.draw.circle(self.screen, color, self.to_screen_space(screen_x,-(screen_y)), 5)

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Grid settings
grid_size = 50  # Adjust this value to change the grid size
grid_color = (200, 200, 200)  # Grid line color
axis_color = (255, 0, 0)  # X-axis color
y_axis_color = (0, 255, 0)  # Y-axis color

# Create the Pygame window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Grid with Plotting")

# Create a grid object
grid = Grid(screen, grid_size, grid_color, axis_color, y_axis_color)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    screen.fill((255, 255, 255))  # Fill the screen with white

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the grid and axes
    grid.draw_grid()

    # Example point plotting
    grid.plot_point(2, -2, (0, 0, 255))  # Blue point
    grid.plot_point(-1, 1, (255, 0, 0))  # Red point

    
    
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
