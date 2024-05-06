import pygame  
  
class Character:  
    def __init__(self, image, width, height, x, y):  
        self.image = pygame.image.load(image)  
        self.image = pygame.transform.scale(self.image, (width, height))  
        self.width = width  
        self.height = height  
        self.x = x  
        self.y = y  
      
    def render(self, screen):  
        screen.blit(self.image, (self.x, self.y))