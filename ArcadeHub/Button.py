from typing import Tuple
import pygame
import math

class Button:

    def __init__(self, text: str, position: Tuple[int, int], fontSize):
        self.buttonFont = pygame.font.Font('Fonts\\ThaleahFat.ttf', fontSize)
        self.buttonPosition = position
        self.buttonText = text
        self.renderText = self.buttonFont.render(self.buttonText, True, (201, 201, 201))
        self.rect = self.renderText.get_rect()
        self.color = (201, 201, 201)

    def render(self, surface, time):
        sinTime = math.sin((time / 400) * 2 / math.pi) * (self.buttonPosition[1] / 40)
        y = self.buttonPosition[1] / 2 + sinTime
        self.renderText = self.buttonFont.render(self.buttonText, True, self.color)
        self.rect = self.renderText.get_rect(center=(self.buttonPosition[0] / 2, y))
        surface.blit(self.renderText, self.rect)

    def setColor(self, col):
        self.color = col

    def isInsideOf(self, point):
        return self.rect.collidepoint(point)
