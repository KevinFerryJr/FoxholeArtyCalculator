import pygame
import sys
import threading
from grid import Grid

# Screen dimensions
screen_width = 800
screen_height = 600

grid_size = 40  # Adjust this value to change the grid size

class PygameWindow:
    def __init__(self):
        #self.root
        #self.root.title("Pygame and Tkinter")
        #self.root.geometry("800x600")

        # Initialize pygame
        pygame.init()
        
        # Create the Pygame window and grid obj
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Grid with Plotting")    
        self.grid = Grid(self.screen, grid_size)
        self.is_running = True
        self.clock = pygame.time.Clock()
    
    def run(self):
        # Game loop
        while self.is_running:
            self.screen.fill((255, 255, 255))  # Fill the screen with white

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False

            # Draw the grid and axes
            self.grid.draw_grid()
            
            # Example point plotting
            point_a = (1, -1)
            point_b = (-1, -3)
            self.grid.graph_line(point_a, point_b)      # Connecting line
            self.grid.plot_point(point_a, (0, 0, 255))  # Blue point
            self.grid.plot_point(point_b, (255, 0, 0))  # Red point
            
            
            
            pygame.display.flip()
            self.clock.tick(60)

        # Quit Pygame
        pygame.quit()
        sys.exit()
        
    def start(self):
        thread = threading.Thread(target=self.run)
        thread.start()
        
#window = PygameWindow()
#window.start()