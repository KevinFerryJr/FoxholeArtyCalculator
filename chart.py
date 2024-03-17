import pygame
import sys
import threading
from grid import Grid

# Screen dimensions
screen_width = 800
screen_height = 600

grid_size = 6  # Adjust this value to change the grid size

class PygameWindow:
    def __init__(self):
        pygame.init()
        
        # Create the Pygame window and grid obj
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Grid with Plotting")    
        self.grid = Grid(self.screen, grid_size)
        self.is_running = True
        self.clock = pygame.time.Clock()
    
    def chartSolution(self):
                    # Example point plotting
            point_a = (1, -1)
            point_b = (-10, -3)
            self.grid.graph_line(point_a, point_b)      # Connecting line
            self.grid.plot_point(point_a, (0, 0, 255))  # Blue point
            self.grid.plot_point(point_b, (255, 0, 0))  # Red point
    
    def run(self):
        # Game loop
        while self.is_running:
            self.screen.fill((255, 255, 255))
            
            self.handle_events()
            self.grid.draw_grid()
            self.chartSolution()
            
            pygame.display.flip()
            self.clock.tick(60)
        
        self.end()
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
        
    def start(self):
        thread = threading.Thread(target=self.run)
        thread.start()
        
    def end(self):
        self.is_running = False
        pygame.quit()
        sys.exit()
        
#window = PygameWindow()
#window.start()