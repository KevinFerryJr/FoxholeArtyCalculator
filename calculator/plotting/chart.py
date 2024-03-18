import pygame
import sys
import threading
import math
from .grid import Grid
from .camera import Camera

# Screen dimensions
screen_width = 800
screen_height = 600

grid_size = 18  # Adjust this value to change the grid size

class PygameWindow:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Plotting Chart")
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.camera = Camera(self.screen)
        self.grid = Grid(self.screen, self.camera, grid_size)
        self.is_running = True
        self.clock = pygame.time.Clock()
        self.solution = Solution()

    def run(self):
        # Game loop
        while self.is_running:
            self.screen.fill((255, 255, 255))

            self.handle_events()
            self.grid.draw_grid(self.camera)
            self.solution.drawSolution(self.solution.get(), self.grid)

            pygame.display.flip()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:  # Scroll up
                self.camera.zoom_in(self.grid)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:  # Scroll down
                self.camera.zoom_out(self.grid)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.camera.move(10, 0)  # Move left
                elif event.key == pygame.K_RIGHT:
                    self.camera.move(-10, 0)  # Move right
                elif event.key == pygame.K_UP:
                    self.camera.move(0, 10)  # Move up
                elif event.key == pygame.K_DOWN:
                    self.camera.move(0, -10)  # Move down

    def start(self):
        thread = threading.Thread(target=self.run)
        thread.start()
        self.thread = thread

    def end(self):
        self.is_running = False
        self.thread.join()
        pygame.quit()
        sys.exit()


class Solution():
    def __init__(self):
        self.point_a = (0,0)
        self.point_b = (0,0)
        self.point_c = (0,0)
    
    def set(self,gunDist,gunAngle,targDist,targAngle):
        cosA = math.cos(math.radians(gunAngle))
        sinA = math.sin(math.radians(gunAngle))
        
        cosB = math.cos(math.radians(targAngle))
        sinB = math.sin(math.radians(targAngle))
        
        # Example point plotting
        self.point_a = (cosA*gunDist, sinA*gunDist)
        self.point_b = (cosB*targDist, sinB*targDist)
        self.point_c = (0, 0)
        
    def get(self):
        return (self.point_a, self.point_b, self.point_c)
    
    def drawSolution(self, solution, grid):
        grid.graph_line(solution[0], solution[1])  
        grid.graph_line(solution[1], solution[2])  
        grid.graph_line(solution[2], solution[0])  
        grid.plot_point(solution[0], (0, 0, 255))  # Blue point
        grid.plot_point(solution[1], (255, 0, 0))  # Red point
        grid.plot_point(solution[2], (0, 255, 0))  # Green point