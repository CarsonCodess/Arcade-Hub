import pygame

class Text:
    def __init__(self, text, position, fontSize):
        self.font = pygame.font.Font('Fonts\\ThaleahFat.ttf', fontSize)
        self.text = text
        self.pos = position
        self.color = (201, 201, 201)

    def render(self, surface):
        renderText = self.font.render(self.text, True, self.color)
        rect = renderText.get_rect()
        rect.center = (self.pos[0] / 2, self.pos[1] / 2)
        surface.blit(renderText, rect)

    def setColor(self, col):
        self.color = col
