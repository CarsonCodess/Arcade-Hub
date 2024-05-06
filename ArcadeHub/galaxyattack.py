import os
import pygame

import gameListScreen
from Character import Character
from Button import Button
from Text import Text

def galaxyattack():

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    backgroundColor = (32, 32, 32)
    textColor = (201, 201, 201)

    width = pygame.display.Info().current_w
    height = pygame.display.Info().current_h

    keysPressed = {}
    bullets = []

    lastBulletTime = 0
    bulletDelay = 120

    bulletPicture = pygame.image.load('galaxyattackbullet.png')

    player = Character('galaxyattackspaceship.png', width/8, width/8, width/2.25, height/1.4)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            elif event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_ESCAPE):
                    print("Go to gameListScreen")
                keysPressed[event.key] = True
            elif event.type == pygame.KEYUP:
                keysPressed[event.key] = False

        if keysPressed.get(pygame.K_w) and player.y >= height/1.5:
            player.y -= width/300
        if keysPressed.get(pygame.K_s) and player.y <= height - player.height:
            player.y += width/300
        if keysPressed.get(pygame.K_a) and player.x >= 0:
            player.x -= width/300
        if keysPressed.get(pygame.K_d) and player.x <= width - player.width:
            player.x += width/300

        screen.fill(backgroundColor)
        player.render(screen)


        #Spawns in Bullets ----------------------------------------
        for bullet in bullets:
            bullet[1] -= 10

        bullets = [bullet for bullet in bullets if bullet[0] > 0]

        currentTime = pygame.time.get_ticks()
        if keysPressed.get(pygame.K_SPACE) and currentTime - lastBulletTime > bulletDelay:
            bullets.append([player.x + player.width / 2 - 16, player.y])
            lastBulletTime = currentTime

        screen.fill(backgroundColor)
        player.render(screen)
        for bullet in bullets:
            screen.blit(bulletPicture, (bullet[0], bullet[1]))
        #----------------------------------------------------------

        pygame.display.flip()
        clock.tick(60)

galaxyattack()
