from typing import Tuple
from mathlib import Sinwave
import pygame
import math

class Button:

    def __init__(self, text: str, position: Tuple[int, int], fontSize: int):
        self.buttonFont = pygame.font.Font('Fonts\\ThaleahFat.ttf', fontSize)
        self.buttonPosition = position
        self.buttonText = text
        self.renderText = self.buttonFont.render(self.buttonText, True, (201, 201, 201))
        self.rect = self.renderText.get_rect()
        self.color = (201, 201, 201)

    def render(self, surface, time):
        self.renderText = self.buttonFont.render(self.buttonText, True, self.color)
        self.rect = self.renderText.get_rect(center=(self.buttonPosition[0] / 2, Sinwave(self.buttonPosition[1], 55, time)))
        surface.blit(self.renderText, self.rect)

    def setColor(self, col):
        self.color = col

    def isInsideOf(self, point):
        return self.rect.collidepoint(point)
