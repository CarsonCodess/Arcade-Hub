import os
import pygame

import gameListScreen
from Button import Button
from Text import Text
from mathlib import Sinwave

def main():
    # Title Screen
    pygame.init()

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    backgroundColor = (32, 32, 32)
    textColor = (201, 201, 201)

    width = pygame.display.Info().current_w
    height = pygame.display.Info().current_h

    playButton = Button('Play', (width, height), 96)
    exitButton = Button('Exit', (width, height + 250), 96)

    gameState = 0  # 0 Menu, 1 Game Select, 2 In Game

    while True:
        mouse = pygame.mouse.get_pos()

        ticks = pygame.time.get_ticks()

        title = Text('Arcade Hub', (width, Sinwave(height/2.5, 15, ticks)), 124)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONDOWN:
                if gameState == 0:
                    if playButton.isInsideOf(mouse):
                        gameListScreen.start()
                        gameState = 1
                    if exitButton.isInsideOf(mouse):
                        pygame.quit()
                if gameState == 1:
                    gameListScreen.onClick()

        screen.fill(backgroundColor)

        if gameState == 0:
            title.render(screen)

            if playButton.isInsideOf(mouse):
                playButton.setColor('black')
            else:
                playButton.setColor(textColor)
            if exitButton.isInsideOf(mouse):
                exitButton.setColor('black')
            else:
                exitButton.setColor(textColor)
            playButton.render(screen, ticks)
            exitButton.render(screen, ticks)
        if gameState == 1:
            gameListScreen.render()

        pygame.display.flip()
        clock.tick(60)

def onInGame():
    global gameState
    gameState = 2

if __name__ == "__main__":
    main()
