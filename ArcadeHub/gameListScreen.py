import pygame
import os
from Text import Text

#TO DO:
#Add a modular button system that automatically adds buttons as games are added.

def mainScene():
    
    pygame.init()

    screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    backgroundColor = (32, 32, 32)

    width = pygame.display.Info().current_w
    height = pygame.display.Info().current_h

    headerFont = pygame.font.Font('Fonts\\ThaleahFat.ttf', 80)
    header = Text('Games', (width, height / 3), headerFont)

    while True:
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
                  
            
        screen.fill(backgroundColor)
        header.render(screen)

        pygame.display.flip()
        clock.tick(60)