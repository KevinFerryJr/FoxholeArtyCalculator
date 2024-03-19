import pygame
import sys
import threading
from .grid import Grid
from .camera import Camera
from .solution import Solution

class PygameWindow:
    def __init__(self, screenWidth, screenHeight):
        pygame.init()
        pygame.display.set_caption("Plotting Chart")
        self.screen = pygame.display.set_mode((screenWidth, screenHeight))
        self.camera = Camera()
        self.grid = Grid(self.screen, self.camera)
        self.is_running = True
        self.clock = pygame.time.Clock()
        self.solution = Solution()

    def run(self):
        # Game loop
        while self.is_running:
            self.screen.fill((255, 255, 255))
            self.camera.update(self.grid)
            self.handle_events()
            self.grid.draw_grid()
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
                    self.camera.move(10, 0, self.grid)  # Move left
                elif event.key == pygame.K_RIGHT:
                    self.camera.move(-10, 0, self.grid)  # Move right
                elif event.key == pygame.K_UP:
                    self.camera.move(0, 10, self.grid)  # Move up
                elif event.key == pygame.K_DOWN:
                    self.camera.move(0, -10, self.grid)  # Move down

    def start(self):
        thread = threading.Thread(target=self.run)
        thread.start()
        self.thread = thread

    def end(self):
        self.is_running = False
        self.thread.join()
        pygame.quit()
        sys.exit()