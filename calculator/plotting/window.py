import pygame
import sys
import threading
from .grid import Grid
from .camera import Camera
from .solution import Solution

class PygameWindow:
    def __init__(self, title, screenWidth, screenHeight):
        self.width = screenWidth
        self.height = screenHeight
        self.title = "Pygame Window"
        
    def update(self):
        self.camera.update(self.grid)
    
    def draw(self):
        self.grid.drawGrid()
        self.solution.drawSolution(self.solution.get(), self.grid)
    
    def events(self):
            self.handleEvents()
            self.handleKeyPressedEvents()
    
    def run(self):
        # Game loop
        while self.is_running:
            self.screen.fill((255, 255, 255))

            self.events()
            self.update()
            self.draw()

            pygame.display.flip()
            self.clock.tick(60)

    def handleKeyPressedEvents(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.camera.move(1, 0, self.grid)
        if keys[pygame.K_RIGHT]:
            self.camera.move(-1, 0, self.grid)
        if keys[pygame.K_UP]:
            self.camera.move(0, 1, self.grid)
        if keys[pygame.K_DOWN]:
            self.camera.move(0, -1, self.grid)
            
        if keys[pygame.K_a]:
            self.camera.move(1, 0, self.grid)
        if keys[pygame.K_d]:
            self.camera.move(-1, 0, self.grid)
        if keys[pygame.K_w]:
            self.camera.move(0, 1, self.grid)
        if keys[pygame.K_s]:
            self.camera.move(0, -1, self.grid)        

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:  # Scroll up
                self.camera.zoom_in(self.grid)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:  # Scroll down
                self.camera.zoom_out(self.grid)

    def start(self):
        pygame.init()
        pygame.display.set_caption(self.title)
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.camera = Camera()
        self.grid = Grid(self.screen, self.camera)
        self.solution = Solution()
        self.is_running = True
        self.clock = pygame.time.Clock()
        
        thread = threading.Thread(target=self.run)
        thread.start()
        self.thread = thread

    def end(self):
        self.is_running = False
        self.thread.join()
        pygame.quit()
        sys.exit()