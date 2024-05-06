from Game import Game
import pygame

class a(Game):
    def __init__(self):
        super.__init__()
    def startGame(self):
        print("aaknds")
    def render(self, screen: pygame.surface):
        clock = pygame.time.Clock()
        backgroundColor = (32, 32, 32)
        screen.fill(backgroundColor)
        pygame.display.flip()
        clock.tick(60)