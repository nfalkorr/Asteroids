import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y) #init position
        self.velocity = pygame.Vector2(0, 0) #init speed
        self.radius = radius # init size

    def draw(self, screen): #show on screen
        pass

    def update(self, dt): #update according to clock tick
        pass
