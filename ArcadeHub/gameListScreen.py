import pygame
import os
from Text import Text

#TO DO:
#Add a modular button system that automatically adds buttons as games are added.

def render(clock):
    screen = pygame.display.get_surface()

    width = pygame.display.Info().current_w
    height = pygame.display.Info().current_h

    header = Text('Games', (width, height / 7), 124)
    header.render(screen)