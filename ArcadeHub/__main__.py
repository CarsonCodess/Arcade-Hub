import os
import pygame
from gameListScreen import mainScene
from Button import Button

def main():
    # Title Screen
    pygame.init()

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    backgroundColor = (32, 32, 32)
    textColor = (201, 201, 201)

    width = pygame.display.Info().current_w
    height = pygame.display.Info().current_h

    titleFont = pygame.font.Font('ThaleahFat.ttf', 124)
    titleText = titleFont.render('Arcade Hub', True, textColor)
    titleTextRect = titleText.get_rect()
    titleTextRect.center = (width/2, height/5)

    buttonFont = pygame.font.Font('ThaleahFat.ttf', 72)

    playButton = Button('Play', (width, height), buttonFont)
    exitButton = Button('Exit', (width, height + 175), buttonFont)

    while True:
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButton.isInsideOf(mouse):
                    mainScene()
                if exitButton.isInsideOf(mouse):
                    pygame.quit()

        screen.fill(backgroundColor)
        screen.blit(titleText, titleTextRect)

        if playButton.isInsideOf(mouse):
            playButton.setColor('black')
        else:
            playButton.setColor(textColor)
        if exitButton.isInsideOf(mouse):
            exitButton.setColor('black')
        else:
            exitButton.setColor(textColor)

        playButton.render(screen)
        exitButton.render(screen)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
